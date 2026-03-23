"""
This borrows heavily from the BinaryPlist package
https://github.com/tyrone-sudeium/st3-binaryplist
"""

import sublime
from sublime import Region
import sublime_plugin
from sublime_plugin import EventListener
from sublime_plugin import TextCommand
import os
import re
import platform
import subprocess
import tempfile

# GLOBAL STUFF
SYNTAX_FILE = "Packages/AppleScript Extensions/AppleScript (Binary).sublime-syntax"
END_REGEX = r"f\s?a\s?d\s?e\s?d\s?e\s?a\s?d\s?\Z"
SUBPROCESS_TIMEOUT = 30


class SaveCursorPositionsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selections = self.view.sel()

        if any(region.size() > 0 for region in selections):
            # Save selections
            cursor_data = [(region.a, region.b) for region in selections]
        else:
            # Save cursor positions
            cursor_data = [(region.a,) for region in selections]

        # Store in view-specific settings instead of global
        self.view.settings().set('saved_cursor_data', cursor_data)


class RestoreCursorPositionsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Retrieve from view-specific settings
        saved_cursor_data = self.view.settings().get('saved_cursor_data', [])

        if saved_cursor_data:
            self.view.sel().clear()

            for data in saved_cursor_data:
                if len(data) == 2:
                    # Restore selection
                    self.view.sel().add(sublime.Region(data[0], data[1]))
                else:
                    # Restore cursor position
                    self.view.sel().add(sublime.Region(data[0]))

            # Optional: clean up after restoring
            self.view.settings().erase('saved_cursor_data')


def is_syntax_set(view=None):
    if view is None:
        view = sublime.active_window().active_view()
    return "AppleScript (Binary).sublime-syntax" in view.settings().get("syntax")


def is_binary(view):
    tail = view.substr(Region(max(0, view.size() - 30), view.size()))
    return re.search(END_REGEX, tail)


def _is_scpt(view):
    file_name = view.file_name()
    return file_name and file_name.endswith(".scpt")


class ScptBinaryCommand(EventListener):
    def on_load(self, view):
        if not _is_scpt(view):
            return
        # Check if binary, convert to plain-text, mark as "was binary"
        if is_binary(view):
            view.run_command("binary_toggle")

    def on_post_save(self, view):
        if not _is_scpt(view):
            return
        # Convert back to plain-text
        if view.get_status("is_binary"):
            view.run_command("save_cursor_positions")
            view.run_command("binary_toggle", {"force_to": True})
            view.run_command("restore_cursor_positions")

    def on_modified(self, view):
        if not _is_scpt(view):
            return
        freshly_written = view.settings().get("freshly_written")
        if freshly_written and is_binary(view):

            view.run_command("save_cursor_positions")
            view.run_command("binary_toggle")
            view.run_command("restore_cursor_positions")

            view.settings().erase("freshly_written")


class BinaryToggleCommand(TextCommand):
    def decode_script(self, edit, view):
        """Reads in the view's file, converts it to plain and replaces the view's
        buffer with the plain-text."""
        file_name = view.file_name()

        if file_name and os.path.isfile(file_name) and file_name.endswith(".scpt"):
            cmd = ["osadecompile", file_name]
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                full_text, err = p.communicate(timeout=SUBPROCESS_TIMEOUT)
            except subprocess.TimeoutExpired:
                p.kill()
                p.communicate()
                sublime.error_message("osadecompile timed out for: " + file_name)
                return

            if p.returncode != 0:
                sublime.error_message(
                    "osadecompile failed:\n" + err.decode("utf-8", errors="replace")
                )
                return

            view.set_encoding("UTF-8")
            view.replace(edit, Region(0, view.size()), full_text.decode("utf-8"))
            view.set_status("is_binary", "Decompiled File")
            view.set_scratch(True)

    def encode_script(self, view):
        """Converts the view's plain-text back to a binary script and writes it out
        to the view's file."""
        file_name = view.file_name()

        if file_name and os.path.isfile(file_name):
            content = view.substr(Region(0, view.size())).encode("utf-8").rstrip()
            try:
                # Write to a temp file to avoid corrupting the original on failure
                tmp_fd, tmp_path = tempfile.mkstemp(suffix=".applescript")
                try:
                    with os.fdopen(tmp_fd, "wb") as f:
                        f.write(content)

                    cmd = ["osacompile", "-o", file_name, tmp_path]
                    p = subprocess.Popen(
                        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                    )
                    try:
                        out, err = p.communicate(timeout=SUBPROCESS_TIMEOUT)
                    except subprocess.TimeoutExpired:
                        p.kill()
                        p.communicate()
                        sublime.error_message(
                            "osacompile timed out for: " + file_name
                        )
                        return

                    if p.returncode != 0:
                        sublime.error_message(
                            "osacompile failed:\n"
                            + err.decode("utf-8", errors="replace")
                        )
                        return

                    view.settings().set("freshly_written", True)
                    view.sel().clear()
                finally:
                    if os.path.exists(tmp_path):
                        os.unlink(tmp_path)
            except Exception as e:
                sublime.error_message(str(e))
                raise e

    def run(self, edit, force_to=False):
        if platform.system() != "Darwin":
            sublime.error_message("Binary AppleScript can only be edited on macOS")
            return

        if is_binary(self.view) and not force_to:
            self.decode_script(edit, self.view)
            if not is_syntax_set(self.view):
                self.view.set_syntax_file(SYNTAX_FILE)
        else:
            self.encode_script(self.view)

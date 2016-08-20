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

# GLOBAL STUFF
SYNTAX_FILE = 'Packages/AppleScript Extensions/AppleScript (Binary).sublime-syntax'
END_REGEX = r'f\s?a\s?d\s?e\s?d\s?e\s?a\s?d\s?\Z'

def is_syntax_set(view=None):
    if view is None:
        view = sublime.active_window().active_view()
    return 'AppleScript (Binary).sublime-syntax' in view.settings().get('syntax')

def is_binary(view):
    selection = view.substr(Region(0, view.size()))
    return (re.search(END_REGEX, selection))

class ScptBinaryCommand(EventListener):
    def on_load(self, view):
        # Check if binary, convert to plain-text, mark as "was binary"
        if is_binary(view):
            view.run_command('binary_toggle')
        
    def on_post_save(self, view):
        # Convert back to plain-text
        if view.get_status('is_binary'):
            view.run_command('binary_toggle', {'force_to': True})

    def on_new(self, view):
        pass

    def on_clone(self, view):
        pass

    def on_pre_close(self, view):
        pass

    def on_close(self, view):
        pass

    def on_pre_save(self, view):
        pass

    def on_modified(self, view):
        freshly_written = view.settings().get('freshly_written')
        if freshly_written and is_binary(view):
            view.run_command('binary_toggle')
            view.settings().erase('freshly_written')

    def on_activated(self, view):
        pass

class BinaryToggleCommand(TextCommand):
    def decode_script(self, edit, view):
        """Reads in the view's file, converts it to plain and replaces the view's
        buffer with the plain-text."""
        file_name = view.file_name()        

        if file_name and file_name != '' and os.path.isfile(file_name) == True and file_name.endswith('.scpt'):
            cmd = ['osadecompile', file_name]
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            full_text, err = p.communicate()
            view.set_encoding('UTF-8')
            view.replace(edit, Region(0, view.size()), str(full_text.decode('utf-8')))
            view.end_edit(edit)
            view.set_status('is_binary', 'Saving As Binary Property List')
            view.set_scratch(True)

    def encode_script(self, view):
        """Converts the view's plain-text back to a binary script and writes it out
        to the view's file."""
        file_name = view.file_name()

        if file_name and file_name != '' and os.path.isfile(file_name) == True:
            bytes = view.substr(Region(0, view.size())).encode('utf-8').rstrip()
            try:
                with open(file_name, 'wb') as f:
                    f.write(bytes)
                cmd = ['osacompile', '-o', file_name, file_name]
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = p.communicate()
                    

                view.settings().set('freshly_written', True)
            except Exception as e:
                sublime.error_message(str(e))
                raise e

    def run(self, edit, force_to=False):
        if platform.system() != 'Darwin':
            sublime.error_message("Binary AppleScript can only be edited on macOS")
            return

        if is_binary(self.view) and not force_to:
            self.decode_script(edit, self.view)
            if not is_syntax_set(self.view):
                self.view.set_syntax_file(SYNTAX_FILE)
        else:
            self.encode_script(self.view)

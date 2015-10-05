# AppleScript Extensions for Sublime Text

[![The MIT License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](http://opensource.org/licenses/MIT)
[![Package Control](https://packagecontrol.herokuapp.com/downloads/AppleScript%20Extensions.svg?style=flat-square)](https://packagecontrol.io/packages/AppleScript%20Extensions)
[![GitHub tag](https://img.shields.io/github/tag/idleberg/AppleScript-Sublime-Text.svg?style=flat-square)](https://github.com/idleberg/AppleScript-Sublime-Text/tags)
[![Travis](https://img.shields.io/travis/idleberg/AppleScript-Sublime-Text.svg?style=flat-square)](https://travis-ci.org/idleberg/AppleScript-Sublime-Text)

This [Sublime Text](http://www.sublimetext.com/) package adds completions, snippets and build tools for [AppleScript](https://developer.apple.com/library/mac/documentation/applescript/conceptual/applescriptlangguide/introduction/ASLR_intro.html).

![Screenshot](https://raw.github.com/idleberg/AppleScript-Sublime-Text/master/screenshot.gif)

*Screenshot of AppleScript in Sublime Text with [Hopscotch](https://github.com/idleberg/Hopscotch) color scheme*

## Installation

### Package Control

1. Make sure you already have [Package Control](https://packagecontrol.io/) installed
2. Choose “*Install Package*” from the Command Palette (<kbd>Super</kbd>+<kbd>Shift</kbd>+<kbd>p</kbd>)
3. Select “*AppleScript Extensions*”” and press <kbd>Enter</kbd>

### GitHub

1. Change to your Sublime Text `Packages` directory
2. Clone repository `git clone https://github.com/idleberg/AppleScript-Sublime-Text.git 'AppleScript Extensions'`

### Manual installation

1. Download the latest [stable release](https://github.com/idleberg/AppleScript-Sublime-Text/releases)
2. Unzip the archive to your Sublime Text `Packages` directory

## Usage

### Completions

Many commands can simply be triggered by completing a standard AppleScript command. Commands such as `try`, `if`, `repeat`, or `set` will create a code block. Use the `Tab` key to jump between input-fields.

### Snippets

There are several snippets included to generate license-texts enclosed in a comment. To trigger these, try the `comment` command with license names as parameter. You could, for example, use `comment:mit` to add an *MIT License* text, or `comment:gpl2` for the *GNU General Public License* in version 2.0. Use the `Tab` key to jump between input-fields.

You can directly address several Mac OS X applications to have them perform some action. For instance you can scaffold a script using `Mail:Send message`, telling Mail to send a message. You can use the `Tab` key to jump between recipient, subject and message fields. Other examples would be `System Preferences:Security` to open the according panel in System Preferences, or `iTunes:Open file` to play a piece of music in iTunes.

More examples:

* `Calendar:Add event`
* `Finder:Open location`
* `OS:Notification Message`
* `Safari:Open location`

### Build System

A build system works on Mac OS X only and should be available by default. To run your script press <kbd>⌘</kbd>+<kbd>B</kbd> or build from the *Tools* menu.

## License

This work is licensed under the [The MIT License](LICENSE).

## Donate

You are welcome support this project using [Flattr](https://flattr.com/submit/auto?user_id=idleberg&url=https://github.com/idleberg/AppleScript-Sublime-Text) or Bitcoin `17CXJuPsmhuTzFV2k4RKYwpEHVjskJktRd`

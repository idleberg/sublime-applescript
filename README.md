# AppleScript Extensionsfor Sublime Text [![Build Status](https://secure.travis-ci.org/idleberg/AppleScript-Sublime-Text.svg)](http://travis-ci.org/idleberg/AppleScript-Sublime-Text)

This [Sublime Text](http://www.sublimetext.com/) package adds completions, snippets and build tools for [AppleScript](https://developer.apple.com/library/mac/documentation/applescript/conceptual/applescriptlangguide/introduction/ASLR_intro.html).

![Screenshot](https://raw.github.com/idleberg/AppleScript-Sublime-Text/master/screenshot.gif)

*Screenshot of AppleScript in Sublime Text with [Hopscotch](https://github.com/idleberg/Hopscotch) color scheme*

## Installation

### Package Control

1. Make sure you already have [Package Control](http://wbond.net/sublime_packages/package_control/) installed
2. Choose “*Install Package*” from the Command Palette (`Ctrl+Shift+P` on Windows/Linux, `⇧⌘P` on OS X)
3. Select “*AppleScript Extensions*” and press `Enter`

### GitHub

1. Change to your Sublime Text `Packages` directory
2. Clone repository `git clone https://github.com/idleberg/AppleScript-Sublime-Text.git`

### Manual installation

1. Download the files using the GitHub .zip download option
2. Unzip the files to your Sublime Text `Packages` directory

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

A build system works on Mac OS X only and should be available by default. To run your script press `⌘+B` or build from the *Tools* menu.

## License

The MIT License (MIT)

Copyright (c) 2014 Jan T. Sott

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Donate

You are welcome support this project using [Flattr](https://flattr.com/submit/auto?user_id=idleberg&url=https://github.com/idleberg/AppleScript-Sublime-Text) or Bitcoin `17CXJuPsmhuTzFV2k4RKYwpEHVjskJktRd`

 /*
 * sublimetext-gulpfile.js
 * https://github.com/idleberg/sublimetext-gulpfile.js
 *
 * Copyright (c) 2014-2018 Jan T. Sott
 * Licensed under the MIT license.
 */

// Dependencies
const gulp = require('gulp'),
  debug = require('gulp-debug'),
  jsonLint = require('gulp-jsonlint');
  ymlVal = require('gulp-yaml-validate');
  xmlVal = require('gulp-xml-validator');

// Supported files
const jsonFiles = [
  '**/*.JSON-sublime-syntax',
  '**/*.JSON-tmLanguage',
  '**/*.JSON-tmTheme',
  '**/*.sublime-build',
  '**/*.sublime-commands',
  '**/*.sublime-completions',
  '**/*.sublime-keymap',
  '**/*.sublime-macro',
  '**/*.sublime-menu',
  '**/*.sublime-settings',
  '**/*.sublime-theme',
  'messages.json',
  '!node_modules/**/*'
];

const xmlFiles = [
  '**/*.plist',
  '**/*.PLIST-sublime-syntax',
  '**/*.PLIST-tmLanguage',
  '**/*.PLIST-tmTheme',
  '**/*.sublime-snippet',
  '**/*.tmCommand',
  '**/*.tmLanguage',
  '**/*.tmPreferences',
  '**/*.tmSnippet',
  '**/*.tmTheme',
  '**/*.xml',
  '!node_modules/**/*'
];

var ymlFiles = [
  '**/*.sublime-syntax',
  '**/*.YAML-tmLanguage',
  '**/*.YAML-tmTheme',
  '!node_modules/**/*'
];

// Lint JSON
gulp.task('lint:json', (done) => {
  gulp.src(jsonFiles)
    .pipe(debug({title: 'lint:json'}))
    .pipe(jsonLint())
    .pipe(jsonLint.failAfterError())
    .pipe(jsonLint.reporter());

  done();
});

// Validate XML
gulp.task('lint:xml', (done) => {
  gulp.src(xmlFiles)
    .pipe(debug({title: 'lint:xml'}))
    .pipe(xmlVal());

  done();
});

// Validate YAML
gulp.task('lint:yml', (done) => {
  gulp.src(ymlFiles)
    .pipe(debug({title: 'lint:yml'}))
    .pipe(ymlVal({ safe: true }));

  done();
});

// Available tasks
gulp.task('lint', gulp.parallel('lint:json', 'lint:xml', 'lint:yml', (done) => {
  done();
}));

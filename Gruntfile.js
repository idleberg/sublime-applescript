 /*
 * sublimetext-gruntfile.js
 * https://github.com/idleberg/sublimetext-gruntfile.js
 *
 * Copyright (c) 2014 Jan T. Sott
 * Licensed under the MIT license.
 */
 
 module.exports = function(grunt) {

 	var jsonFiles = [
        '**/*.JSON-tmLanguage',
        '**/*.sublime-build',
        '**/*.sublime-commands',
        '**/*.sublime-completions',
        '**/*.sublime-keymap',
        '**/*.sublime-macro',
        '**/*.sublime-menu',
        '**/*.sublime-settings',
        '**/*.sublime-theme',
        'messages.json'
    ];

    var xmlFiles = [
    	'**/*.plist',
    	'**/*.sublime-snippet',
    	'**/*.tmCommand',
    	'**/*.tmLanguage',
    	'**/*.tmPreferences',
    	'**/*.tmSnippet'
    ];

 	grunt.initConfig({

 		// default task
		jsonlint: {
		  files: {
		    src: jsonFiles
		  }
		},

 		xml_validator: {
 			files: {
 				src: xmlFiles
 			},
 		},

		// watch task
        watch: {
		    json: {
		        files: jsonFiles,
		        tasks: ['jsonlint']
		    },
		    xml: {
		        files: xmlFiles,
		        tasks: ['xml_validator']
		    }
		}
 	});

 	grunt.loadNpmTasks('grunt-contrib-watch');
 	grunt.loadNpmTasks('grunt-xml-validator');
 	grunt.loadNpmTasks('grunt-jsonlint');
 	grunt.registerTask('default', ['jsonlint', 'xml_validator']);

    // task shortcuts
 	grunt.registerTask('json', 'jsonlint');
 	grunt.registerTask('xml', 'xml_validator');
 };
#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This Python script is written by Zhiyang Ong to test
		the parsing of a JSON file containing the configuration of
		parameters for this software.

	Synopsis:
	Test the parsing of a JSON file containing the configuration of
		parameters for this software.

	Notes/Assumptions:
	None at the moment.

	References:
	Citations/References that use the LaTeX/BibTeX notation are taken
    	from my BibTeX database (set of BibTeX entries).

	Revision History:
	September 28, 2018			Version 0.1, initial build.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'September 28, 2018'

#	The MIT License (MIT)

#	Copyright (c) <2018> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?



###############################################################
"""
	Import modules from The Python Standard Library.
	sys			Get access to any command-line arguments.
	os			Use any operating system dependent functionality.
	os.path		For pathname manipulations.

	subprocess -> call
						To make system calls.
	time				To measure elapsed time.
	warnings			Raise warnings.
	re					Use regular expressions.
	filecmp				For file comparison.
	shutil.copyfile		Copy a file from [source] to [destination]
	json				For parsing JSON files and processing JSON-based data.
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
# Copy a file from [source] to [destination]
from shutil import copyfile
import json

###############################################################
#	Import Custom Python Modules

"""
	Package and module to print statistics of software testing
		results.
"""
from statistics.test_statistics import statistical_analysis
"""
	Package and module to configure the software application's
		parameters.
"""
from utilities.configuration_manager import config_manager
# Package and module to perform file I/O operations.
from utilities.file_io import file_io_operations
# Package and module to transform JSON objects to Python objects.
from parsers.json_object import json_obj
# Package and module to parse JSON configuration files.
from parsers.config_file_parser import config_parser

###############################################################
"""
	Module to test JSON parser for the configuration file that
		parameterizes this software.
"""
class config_parser_tester:
	## =========================================================
	#	Method to test how the JSON configuration file is parsed,
	#		and how the config_manager is updated.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_json_config_file_parser():

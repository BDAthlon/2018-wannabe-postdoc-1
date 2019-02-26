#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to implement
		a custom graph_exception that extends the default Python
		exception class.

	Synopsis:
	Raises an error when a run-time error specific to graph
		implementations occurs.

	Notes/Assumptions:
	#### TO BE COMPLETED

	References:
	Citations/References that use the LaTeX/BibTeX notation are taken
		from my BibTeX database (set of BibTeX entries).

	\cite[from Learn Python Programming -- The Definitive Guide: Python Custom Exceptions]{ParewaLabsStaff20XY}

	gahooa, Answer to ``Proper way to declare custom exceptions in modern Python?,'' Stack Exchange Inc., New York, NY, August 23, 2009. Available online from {\it Stack Exchange Inc.: Stack Overflow: Questions} at: \url{https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python} and \url{https://stackoverflow.com/revisions/1319675/7}; March 26, 2018 was the last accessed date.

"""

#	The MIT License (MIT)

#	Copyright (c) <2014> <Zhiyang Ong>

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
	time		To measure elapsed time.
	warnings	Raise warnings.
	re			Use regular expressions.
	filecmp		For file comparison.
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
import calendar


###############################################################
#	Import Custom Python Modules


###############################################################
#	Module of a custom graph_exception that extends the default
#		Python exception class.
class graph_exception(Exception):
	##	Standard constructor for the graph_exception class.
	#	@param self - This instance of the graph_exception class.
	#	@param error_message - Custom error message included when
	#		raising/throwing this graph_exception class.
	#	@param errors - Associted errors to this instance of the
	#		graph_exception.
	def __init__(self, error_message, errors):
		# Call base class, Exception, constructor with required
		#	parameters.
		super().__init__(error_message)
		# Custom code: Assign associated errors.
		self.errors = errors
	#
	# ============================================================
	##	Method to set the location of simulation/experimental results.
	#	@param location - Location of a directory.
	#	@return a boolean TRUE, if the location is a valid directory.
	#		Else, return FALSE.
	#	O(1) method.
	@staticmethod
	def set_result_repository(location):
		if not os.path.isabs(location):
			#print("	location is a relative path.")
			# Change the relative path to an absolute path.
			location = os.path.expanduser(location)
		#else:
		#	print("	location is an absolute path.")
		if os.path.isdir(location):
			#print("	location is a valid directory.")
			config_manager.result_repository = location
			return True
		else:
			#print("	location is an invalid directory.")
			return False
	# ============================================================
	##	Method to get the location of simulation/experimental results.
	#	@param - None.
	#	@return the location of simulation/experimental results.
	#	O(1) method.
	@staticmethod
	def get_result_repository():
		return config_manager.result_repository

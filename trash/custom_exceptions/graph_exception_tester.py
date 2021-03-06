#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3
###!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to test the
		custom graph_exception that extends the default Python
		exception class.

	Synopsis:
	Test the custom graph_exception class.

	Notes/Assumptions:
	None at the moment.


	References:
	Citations/References that use the LaTeX/BibTeX notation are taken
		from my BibTeX database (set of BibTeX entries).

	Revision History:
	August 1, 2018			Version 0.1, initial build.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'August 1, 2018'

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
# Copy a file from [source] to [destination]
from shutil import copyfile

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

###############################################################
"""
	Module to test the custom graph_exception class.
	Support for class instantiation is not provided, to avoid
		acquiring a collection of useless "graph_exception"
		objects.
"""
class graph_exception_tester:
	## =========================================================
	#	Method to test the usage of the custom graph_exception class.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_graph_exception():
		print("	Testing the graph_exception class/module.")
		prompt = "	... Test: Raise graph_exception		{}"
		statistical_analysis.increment_number_test_cases_used()
		try (config_manager.get_result_repository() == "Unknown location."):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		except graph_exception:
			print(prompt .format("FAIL!!!"))
			#print("location=",config_manager.get_result_repository(),"=")
		except:
			print(prompt .format("FAIL fail!!!"))
		absolute_path = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
		prompt = "	... Test: result_repository, check change to abs. path.	{}"
		statistical_analysis.increment_number_test_cases_used()
		if config_manager.set_result_repository(absolute_path):
			print("	result_repository is changed to an absolute path.")
		else:
			print("	result_repository is NOT changed to an absolute path.")
		if (config_manager.get_result_repository() == absolute_path):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			print("Actual location=",config_manager.get_result_repository(),"=")
		# ------------------------------------------------------------
		prompt = "	... Test: result_repository, check change to rel. path.	{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			Set "result_repository" to a relative path that is equivalent
				absolute path, "absolute_path".
		"""
		if config_manager.set_result_repository("~/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"):
			print("	result_repository is changed to an relative path.")
		else:
			print("	result_repository is NOT changed to an relative path.")
		"""
			"result_repository" is changed to an relative path.
			However, compare "result_repository" to the equivalent
				absolute path.
			This is because if a relative path is detected, it will be
				transform/changed to an absolute path, before being
				assigned to "result_repository".
		"""
		if (config_manager.get_result_repository() == absolute_path):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			print("Actual location=",config_manager.get_result_repository(),"=")
		# ------------------------------------------------------------
		prompt = "	... Test: result_repository, changing to invalid path.	{}"
		statistical_analysis.increment_number_test_cases_used()
		"""
			Set "result_repository" to an invalid path.
		"""
		if not config_manager.set_result_repository("~/This/is/an/invalid/path"):
			print("	result_repository is not changed to an invalid path.")
		else:
			print("	result_repository is CHANGED to an INVALID path.")
		"""
			"result_repository" should not be changed to an invalid path.
			Hence, it shall still refer to "absolute_path".
		"""
		if (config_manager.get_result_repository() == absolute_path):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			print("Actual location=",config_manager.get_result_repository(),"=")

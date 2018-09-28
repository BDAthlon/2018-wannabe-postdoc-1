#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This Python script is written by Zhiyang Ong to test
		the transformation of JSON objects to Python objects.

	Synopsis:
	Test transformation of JSON objects to Python objects.

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
# Package and module to process input arguments to the script/program.
#from utilities.queue_ip_arguments import queue_ip_args
# Package and module to perform file I/O operations.
from utilities.file_io import file_io_operations

# Package and module to transform JSON objects to Python objects.
from parsers.json_object import json_obj

###############################################################
"""
	Module with methods that transform JSON objects to Python
		objects.
	Test the accessibility of each field of the "json_object" class.
"""
class json_obj_tester:
	## =========================================================
	#	Method to test the "json_object" accessibility that
	#		transform JSON objects to Python objects.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_json_object_accessibility():
		# List of JSON files to test JSON-to-Python transformation.
		Congleton2017_json = "/Users/zhiyang/Documents/ricerca/gulyas-scripts/sandbox/python/json-files/Congleton2017.json"
		WikipediaContributors2018p_1_json = "/Users/zhiyang/Documents/ricerca/gulyas-scripts/sandbox/python/json-files/WikipediaContributors2018p-1.json"
		WikipediaContributors2018p_2_json = "/Users/zhiyang/Documents/ricerca/gulyas-scripts/sandbox/python/json-files/WikipediaContributors2018p-2.json"
		WikipediaContributors2018p_3_json = "/Users/zhiyang/Documents/ricerca/gulyas-scripts/sandbox/python/json-files/WikipediaContributors2018p-3.json"
		WikipediaContributors2018p_4_json = "/Users/zhiyang/Documents/ricerca/gulyas-scripts/sandbox/python/json-files/WikipediaContributors2018p-4.json"
		# -------------------------------------------------------
		print("	... Test transformation of JSON objects to Python objects.")
		prompt = "	Test: Congleton2017_json				{}"
		statistical_analysis.increment_number_test_cases_used()
		Congleton2017_json_fo = file_io_operations.open_file_object_read(Congleton2017_json)
		json_to_py_obj = json_obj(Congleton2017_json_fo)
		#print("=	Print the transformed JSON object.")
		#print(json_to_py_obj.__dict__)
		#print("=	Print the transformed JSON object: list format.")
		#print(json_to_py_obj.__list__)
		#print("=	Print the loaded JSON object.")
		# Why does this line work, and the next line doesn't?
		Congleton2017_json_dict = json.load(file_io_operations.open_file_object_read(Congleton2017_json))
		#Congleton2017_json_dict = json.load(Congleton2017_json_fo)
		#print(Congleton2017_json_dict)
		"""
			Compare contents of the Python Object with that from the
				json.load() operation.
		"""
		if json_to_py_obj.__list__ == Congleton2017_json_dict:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		file_io_operations.close_file_object(Congleton2017_json_fo)
		# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
		prompt = "	Test: WikipediaContributors2018p_1_json			{}"
		statistical_analysis.increment_number_test_cases_used()
		WikipediaContributors2018p_1_json_fo_1 = file_io_operations.open_file_object_read(WikipediaContributors2018p_1_json)
		WikipediaContributors2018p_1_json_fo_2 = file_io_operations.open_file_object_read(WikipediaContributors2018p_1_json)
		json_to_py_obj = json_obj(WikipediaContributors2018p_1_json_fo_1)
		WikipediaContributors2018p_1_json_dict = json.load(WikipediaContributors2018p_1_json_fo_2)
		"""
			Compare contents of the Python Object with that from the
				json.load() operation.
		"""
		if json_to_py_obj.__list__ == WikipediaContributors2018p_1_json_dict:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		file_io_operations.close_file_object(WikipediaContributors2018p_1_json_fo_1)
		file_io_operations.close_file_object(WikipediaContributors2018p_1_json_fo_2)
		"""
			This indicates that when a file object is created for a
				JSON load operation, it cannot be used for another JSON
				load operation.
			If I try to use a file object for multiple JSON load
				operations, a run-time json.decoder.JSONDecodeError will
				occur.
		"""
		# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
		prompt = "	Test: WikipediaContributors2018p_2_json			{}"
		statistical_analysis.increment_number_test_cases_used()
		WikipediaContributors2018p_2_json_fo_1 = file_io_operations.open_file_object_read(WikipediaContributors2018p_2_json)
		WikipediaContributors2018p_2_json_fo_2 = file_io_operations.open_file_object_read(WikipediaContributors2018p_2_json)
		json_to_py_obj = json_obj(WikipediaContributors2018p_2_json_fo_1)
		WikipediaContributors2018p_2_json_dict = json.load(WikipediaContributors2018p_2_json_fo_2)
		"""
			Compare contents of the Python Object with that from the
				json.load() operation.
		"""
		if json_to_py_obj.__list__ == WikipediaContributors2018p_2_json_dict:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		file_io_operations.close_file_object(WikipediaContributors2018p_2_json_fo_1)
		file_io_operations.close_file_object(WikipediaContributors2018p_2_json_fo_2)
		# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
		prompt = "	Test: WikipediaContributors2018p_3_json			{}"
		statistical_analysis.increment_number_test_cases_used()
		WikipediaContributors2018p_3_json_fo_1 = file_io_operations.open_file_object_read(WikipediaContributors2018p_3_json)
		WikipediaContributors2018p_3_json_fo_2 = file_io_operations.open_file_object_read(WikipediaContributors2018p_3_json)
		json_to_py_obj = json_obj(WikipediaContributors2018p_3_json_fo_1)
		WikipediaContributors2018p_3_json_dict = json.load(WikipediaContributors2018p_3_json_fo_2)
		"""
			Compare contents of the Python Object with that from the
				json.load() operation.
		"""
		if json_to_py_obj.__list__ == WikipediaContributors2018p_3_json_dict:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		file_io_operations.close_file_object(WikipediaContributors2018p_3_json_fo_1)
		file_io_operations.close_file_object(WikipediaContributors2018p_3_json_fo_2)
		# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
		prompt = "	Test: WikipediaContributors2018p_4_json			{}"
		statistical_analysis.increment_number_test_cases_used()
		WikipediaContributors2018p_4_json_fo_1 = file_io_operations.open_file_object_read(WikipediaContributors2018p_4_json)
		WikipediaContributors2018p_4_json_fo_2 = file_io_operations.open_file_object_read(WikipediaContributors2018p_4_json)
		json_to_py_obj = json_obj(WikipediaContributors2018p_4_json_fo_1)
		WikipediaContributors2018p_4_json_dict = json.load(WikipediaContributors2018p_4_json_fo_2)
		"""
			Compare contents of the Python Object with that from the
				json.load() operation.
		"""
		if json_to_py_obj.__list__ == WikipediaContributors2018p_4_json_dict:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		file_io_operations.close_file_object(WikipediaContributors2018p_4_json_fo_1)
		file_io_operations.close_file_object(WikipediaContributors2018p_4_json_fo_2)

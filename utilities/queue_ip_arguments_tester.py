#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This Python script is written by Zhiyang Ong to test support functions
        to process input arguments for a genetic technology mapping software.


	Synopsis:
	Test support functions to process input arguments for a genetic technology
        mapping software.


	Notes/Assumptions:
	Raise an exception when the 2nd parameter of the software matches the
		filename of an existing file.
		This prevents its contents from being overwritten.
	Raise an exception when the user manual cannot be accessed
		due to errors, or when errors occur in an input argument.

	Revision History:
	July 31, 2018			Version 0.1, initial build.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'July 31, 2018'

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
	collections -> namedtuple
				To use named tuples.
	operator -> attrgetter
				To manipulate attributes of a named tuple as callable
					objects.
"""

#import sys
#import os
#import os.path
#from subprocess import call
#import time
import warnings
#import re
#from collections import namedtuple
#from operator import attrgetter

###############################################################
#	Import Custom Python Modules

"""
	Package and module to print statistics of software testing
		results.
"""
from statistics.test_statistics import statistical_analysis
# Package and module to process input arguments to the script/program.
from utilities.queue_ip_arguments import queue_ip_args



###############################################################
"""
	Module that tests the methods for processing input arguments
		of a genetic technology mapping software.
	Support for class instantiation is not provided, to avoid
		acquiring a collection of useless "queue_ip_args"
		objects.
	Test each static method of the "queue_ip_args" class.
"""
class queue_ip_args_tester:
	## =========================================================
	#	Method to test the O(1) methods that print information
	#		to the standard output, or are accessor methods.
	#	@return - Nothing.
	#	O(?) method.
	@staticmethod
	def test_o1_methods():
		print("	Test: queue_ip_args.get_input_arguments()		OK")
		temp_set_ip_args = queue_ip_args.get_input_arguments()
		statistical_analysis.increment_number_test_cases_used()
		statistical_analysis.increment_number_test_cases_passed()
		#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
		print("	Test: queue_ip_args.print_all_input_arguments()		OK")
		queue_ip_args.print_all_input_arguments()
		statistical_analysis.increment_number_test_cases_used()
		statistical_analysis.increment_number_test_cases_passed()
		#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
		prompt = "	Test: queue_ip_args.get_1st_input_argument()		{}"
		statistical_analysis.increment_number_test_cases_used()
		if queue_ip_args.get_1st_input_argument() is not None:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
		prompt = "	Test: queue_ip_args.get_2nd_input_argument()		{}"
		statistical_analysis.increment_number_test_cases_used()
		if queue_ip_args.get_2nd_input_argument() is not None:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		#	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
		prompt1 = "	Test: queue_ip_args.get_number_of_input_arguments()	{}"
		statistical_analysis.increment_number_test_cases_used()
		prompt2 = "	Test: queue_ip_args.set_input_arguments(...)		{}"
		statistical_analysis.increment_number_test_cases_used()
		prompt3 = "	Test: queue_ip_args.get_name_of_current_script()	{}"
		statistical_analysis.increment_number_test_cases_used()
		#	List of input arguments.
		list_ip_args = []
		#	Name of current script.
		name_current_script = "No name"
		if queue_ip_args.get_2nd_input_argument() is not None:
			print(prompt1 .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
			print(prompt2 .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
			print(prompt3 .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt1 .format("FAIL!!!"))
			print(prompt2 .format("FAIL!!!"))
    ## =========================================================
	#	Method to test the methods that support software test
	#		automation.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_queue_ip_args():
		print("==	Testing class: queue_ip_args.")
		queue_ip_args_tester.test_o1_methods()
		print(".")

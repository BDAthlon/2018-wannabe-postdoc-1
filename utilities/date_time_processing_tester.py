#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to perform
		date and time operations.

	Synopsis:
	Test different/all date and time operations.

	Notes/Assumptions:




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

###############################################################
#	Import Custom Python Modules

"""
	Package and module to print statistics of software testing
		results.
"""
from statistics.test_statistics import statistical_analysis
# Package and module to process input arguments to the script/program.
from utilities.queue_ip_arguments import queue_ip_args
# Package and module to perform date and time operations.
from utilities.date_time_processing import date_time_operations

###############################################################
"""
	Module with methods that perform date and time operations.
	Support for class instantiation is not provided, to avoid
		acquiring a collection of useless "date_time_operations"
		objects.
	Test each static method of the "date_time_operations" class.
"""
class date_time_operations_tester:
	## =========================================================
	#	Method to test the methods that perform date and time
    #       operations.
    #	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_date_time_operations():
		print("==	Testing class: date_time_operations.")
		print("	Testing date_time_operations.is_valid_time() method.")
		prompt = "	... Test: single error, hh				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_time(34,5,3,124395):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: single error, mm				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_time(4,-8215,3,124395):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: single error, ss				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_time(4,15,586,124395):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: single error, us				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_time(4,15,56,123435435434395):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: double errors, ss and us			{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_time(4,15,956,123435435434395):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: multiple errors, hh, ss, and us		{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_time(42390534,15,956,123435435434395):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: no error					{}"
		statistical_analysis.increment_number_test_cases_used()
		if date_time_operations.is_valid_time(23,59,59,124395):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: no error					{}"
		statistical_analysis.increment_number_test_cases_used()
		if date_time_operations.is_valid_time(0,0,0,000000):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: no error					{}"
		statistical_analysis.increment_number_test_cases_used()
		if date_time_operations.is_valid_time(1,1,1,1):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		# -----------------------------------------------------------------
		print("	Testing date_time_operations.is_valid_date() method.")
		prompt = "	... Test: single error, dd				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_date(34,5,2017):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: single error, -dd				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_date(-6701,5,2017):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: single error, mm				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_date(24,15,2017):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: single error, mm				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_date(6,0,2017):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: single error, -mm				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_date(6,-20,2017):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: single error, yy				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_date(6,2,6017):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: single error, yy				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_date(6,2,1017):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: double errors, dd and yy			{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_date(29,2,2018):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: double errors, dd and yy			{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_date(30,2,1980):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: double errors, dd and mm			{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_date(31,4,2018):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: multiple errors, dd, mm, and yy		{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.is_valid_date(32,-4,1988):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: no error					{}"
		statistical_analysis.increment_number_test_cases_used()
		if date_time_operations.is_valid_date(31,7,2015):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: no error					{}"
		statistical_analysis.increment_number_test_cases_used()
		if date_time_operations.is_valid_date(30,6,2017):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		# -----------------------------------------------------------------
		print("	Testing date_time_operations.check_filename_date_time_format() method.")
		prompt = "	... Test: single error, dd				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.check_filename_date_time_format("54-9-2018-13-58-59-734507.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: single error, yy				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.check_filename_date_time_format("54-9-3018-13-58-59-734507.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: single error, mm				{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.check_filename_date_time_format("29-82-2018-13-58-59-734507.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: multiple errors, dd, mm, yy			{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.check_filename_date_time_format("29-2-2018-13-58-59-734507.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: multiple errors, dd, mm, yy			{}"
		statistical_analysis.increment_number_test_cases_used()
		if not date_time_operations.check_filename_date_time_format("30-2-2016-13-58-59-734507.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: valid date & time - leap year			{}"
		statistical_analysis.increment_number_test_cases_used()
		if date_time_operations.check_filename_date_time_format("29-2-2016-21-58-59-734507.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: valid date & time				{}"
		statistical_analysis.increment_number_test_cases_used()
		if date_time_operations.check_filename_date_time_format("28-2-2018-13-58-59-734507.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: valid date & time				{}"
		statistical_analysis.increment_number_test_cases_used()
		if date_time_operations.check_filename_date_time_format("31-5-2018-13-58-59-734507.txt"):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))

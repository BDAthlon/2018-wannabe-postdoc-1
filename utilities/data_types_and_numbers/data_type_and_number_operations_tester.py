#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to test operations
		with basic data types and numbers in the data_type_n_number_ops
		class.

	Synopsis:
	Test operations with basic data types and numbers in the
		data_type_n_number_ops class.


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
	calendar	For checking if given year is a leap year.
"""

import sys
#import os
import os.path
#from subprocess import call
import subprocess
#import time
import warnings
#import re
import calendar
import numpy as np

###############################################################
#	Import Custom Python Modules

"""
	Package and module to print statistics of software testing
		results.
"""
from statistics_pkg.test_statistics import statistical_analysis
"""
	Package and module to perform operations on basic data types
		and numbers.
"""
from utilities.data_types_and_numbers.data_type_and_number_operations import data_type_n_number_ops




###############################################################
##	Module that tests methods that perform operations on basic
#		data types and (integers and floating-point) numbers.
class data_type_n_number_ops_tester:
	## =========================================================
	#	Method to test the method determining if each object
	#		in a list is an integer or a floating-point number.
	#	@param - None.
	#	@return - Nothing.
	#	O(n) method, where "n" is the maximum size of the lists
	#		being tested.
	@staticmethod
	def test_is_list_of_numbers():
		print("	Testing is_list_of_numbers() method.")
		list_of_objs = None
		prompt = "	... Test: is_list_of_numbers(None) == False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(None):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		not_a_list_obj = data_type_n_number_ops()
		prompt = "	... Test: is_list_of_numbers(not_a_list_obj) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(not_a_list_obj):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: is_list_of_numbers([]) == False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers([]):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_not_pure_numbers_1 = [-221, 247, 0, "Ciao tutti!", 576372.32604]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_1) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(list_not_pure_numbers_1):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_not_pure_numbers_2 = ["Buona serata!"]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_2) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(list_not_pure_numbers_2):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_not_pure_numbers_3 = ["Laszlo Tabori is a world record holder!", 2673, 92.23, 7823, 10129, 478334]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_3) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(list_not_pure_numbers_3):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_not_pure_numbers_4 = [54.2, 0.232, 2439, 1392849, "Albert-László Barabási"]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_4) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(list_not_pure_numbers_4):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		a = data_type_n_number_ops()
		b = data_type_n_number_ops()
		c = data_type_n_number_ops()
		list_not_pure_numbers_5 = [2247, 273805, 0.23423, 9234.2347832, "network science", a, 785398, 0.23423, b, 45678, c, "data science", 5623]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_5) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(list_not_pure_numbers_5):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_1 = [4567809, 67890, 5678090, 1, 9, 436790]
		prompt = "	... Test: is_list...numb(lst_pure_pos_integers) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_1):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_2 = [-2569, -1, -62739, 0, -93, -864]
		prompt = "	... Test: is_list...numb(lst_integers_not_pos) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_2):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_3 = [-2569, -1, -62739, -0, -93, -864]
		prompt = "	... Test: is_list...numb(lst_integers_neg_0) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_3):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_4 = [0.437693, 1.3224, 346973.5679, -0.34367, -242.235623]
		prompt = "	... Test: is_list...numb(lst_pure_fp_num) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_4):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_5 = [-210.437693, -56971.3224, -9.5679, -0.45634367, -32242.235623]
		prompt = "	... Test: is_list...numb(lst_pure_neg_fp_num) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_5):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_6 = [0, 0, 0, 0, 0, 0 , 0]
		prompt = "	... Test: is_list...numb(lst_pure_0s) == True		{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_6):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_7 = [0]
		prompt = "	... Test: is_list...numb([0]) == True			{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_7):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_8 = [-56970]
		prompt = "	... Test: is_list...numb([-56970]) == True		{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_8):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_9 = [723]
		prompt = "	... Test: is_list...numb([723]) == True			{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_9):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		list_pure_numbers_10 = [54869, 2.23, 0.2345, 8203, 102.23, 12, 7.23, 923]
		prompt = "	... Test: is_list...numb(lst_fp_int_only) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_10):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the methods that operate on basic data
	#		types and numbers, which belong to the class
	#		data_type_n_number_ops.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_data_type_n_number_ops():
		print("")
		print("")
		print("==	Testing class: data_type_n_number_ops.")
		data_type_n_number_ops_tester.test_is_list_of_numbers()
		

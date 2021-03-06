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
	#	@param op_f_obj - output file object to print software
	#		testing results to.
	#	@return - Nothing.
	#	O(n) method, where "n" is the maximum size of the lists
	#		being tested.
	@staticmethod
	def test_is_list_of_numbers(op_f_obj):
		op_f_obj.write("	Testing is_list_of_numbers() method.")
		list_of_objs = None
		prompt = "	... Test: is_list_of_numbers(None) == False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(None):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		not_a_list_obj = data_type_n_number_ops()
		prompt = "	... Test: is_list_of_numbers(not_a_list_obj) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(not_a_list_obj):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: is_list_of_numbers([]) == False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers([]):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_not_pure_numbers_1 = [-221, 247, 0, "Ciao tutti!", 576372.32604]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_1) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(list_not_pure_numbers_1):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_not_pure_numbers_2 = ["Buona serata!"]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_2) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(list_not_pure_numbers_2):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_not_pure_numbers_3 = ["Laszlo Tabori is a world record holder!", 2673, 92.23, 7823, 10129, 478334]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_3) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(list_not_pure_numbers_3):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_not_pure_numbers_4 = [54.2, 0.232, 2439, 1392849, "Albert-László Barabási"]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_4) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(list_not_pure_numbers_4):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		a = data_type_n_number_ops()
		b = data_type_n_number_ops()
		c = data_type_n_number_ops()
		list_not_pure_numbers_5 = [2247, 273805, 0.23423, 9234.2347832, "network science", a, 785398, 0.23423, b, 45678, c, "data science", 5623]
		prompt = "	... Test: is_list...numb(lst_not_pure_numb_5) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_list_of_numbers(list_not_pure_numbers_5):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_pure_numbers_1 = [4567809, 67890, 5678090, 1, 9, 436790]
		prompt = "	... Test: is_list...numb(lst_pure_pos_integers) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_1):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_pure_numbers_2 = [-2569, -1, -62739, 0, -93, -864]
		prompt = "	... Test: is_list...numb(lst_integers_not_pos) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_2):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_pure_numbers_3 = [-2569, -1, -62739, -0, -93, -864]
		prompt = "	... Test: is_list...numb(lst_integers_neg_0) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_3):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_pure_numbers_4 = [0.437693, 1.3224, 346973.5679, -0.34367, -242.235623]
		prompt = "	... Test: is_list...numb(lst_pure_fp_num) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_4):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_pure_numbers_5 = [-210.437693, -56971.3224, -9.5679, -0.45634367, -32242.235623]
		prompt = "	... Test: is_list...numb(lst_pure_neg_fp_num) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_5):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_pure_numbers_6 = [0, 0, 0, 0, 0, 0 , 0]
		prompt = "	... Test: is_list...numb(lst_pure_0s) == True		{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_6):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_pure_numbers_7 = [0]
		prompt = "	... Test: is_list...numb([0]) == True			{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_7):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_pure_numbers_8 = [-56970]
		prompt = "	... Test: is_list...numb([-56970]) == True		{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_8):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_pure_numbers_9 = [723]
		prompt = "	... Test: is_list...numb([723]) == True			{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_9):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		list_pure_numbers_10 = [54869, 2.23, 0.2345, 8203, 102.23, 12, 7.23, 923]
		prompt = "	... Test: is_list...numb(lst_fp_int_only) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_list_of_numbers(list_pure_numbers_10):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method determining if the input parameter
	#		is a tuple and if each object of the tuple is a tuple, too.
	#	@param op_f_obj - output file object to print software
	#		testing results to.
	#	@return - Nothing.
	#	O(nm) method, where 'n' is the size of the the tuple of
	#		tuples (or number of subtuples/sub-tuples), and 'm' is
	#		the size of the largest tuple (or subtuples/sub-tuples)
	#		in the tuple of tuples.
	@staticmethod
	def test_is_tuple_of_tuples(op_f_obj):
		op_f_obj.write("	Testing is_tuple_of_tuples() method.")
		prompt = "	... Test: is_tuple_of_tuples(None) == False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_tuple_of_tuples(None):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		not_a_tuple_obj = data_type_n_number_ops()
		prompt = "	... Test: is_tuple_of_tuples(not_a_tuple_obj) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_tuple_of_tuples(not_a_tuple_obj):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: is_tuple_of_tuples(()) == False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_tuple_of_tuples(()):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		tup_of_tups = (1.9,2.8,3,7,4,6,5.5)
		prompt = "	... Test: is_tup_of_tups(tuple of numbers) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_tuple_of_tuples(tup_of_tups):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		tup_of_tups = (1.9,2.8,"Ciao mondo!",3,7,4,6,5.5,"Hola todos!")
		prompt = "	... Test: is...(tuple of numbers & strings) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_tuple_of_tuples(tup_of_tups):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		tup_of_tups = ((1.9,2.8,"Ciao mondo!",3,7,4,6,5.5,"Hola todos!"),)
		prompt = "	... Test: is_tup_of_tups(tuple of a tuple - 1) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_tuple_of_tuples(tup_of_tups):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		tup_of_tups = ((1.2,2.3,3.4),(9,8,7,6),(6,5))
		prompt = "	... Test: is_t_of_ts(tuple of a tuple - 2) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_tuple_of_tuples(tup_of_tups):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		a = data_type_n_number_ops()
		b = data_type_n_number_ops()
		c = data_type_n_number_ops()
		d = ((8,9.1,0.32),(a,b),(7,4,8,9,5),("Hola todos!",23,95.3,"Ciao mondo!"),(c,))
		prompt = "	... Test: is_t_of_ts(tuple of a tuple - 3) == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_tuple_of_tuples(d):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		d = ((8,9.1,0.32),(a,b),("Hola todos!",23,95.3,"Ciao mondo!"),c)
		prompt = "	... Test: is_t_of_ts(tup of tups & object) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_tuple_of_tuples(d):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		d = ((8,9.1,0.32),"Koszonom",("Hola todos!",23,95.3,"Ciao mondo!"))
		prompt = "	... Test: is_t_of_ts(tup of tups & string) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_tuple_of_tuples(d):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		d = ((8,9.1,0.32),586,("Hola todos!",23,95.3,"Ciao mondo!"))
		prompt = "	... Test: is_t_of_ts(tup of tups & number) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_tuple_of_tuples(d):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		d = ((8,9.1,0.32,834.21,4,21.1),(a,b,d),("Hola todos!",23,95.3,"Ciao mondo!"))
		prompt = "	... Test: is_t_of_ts(tup of tups) == True		{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_tuple_of_tuples(d):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		e = ((8,9.1,0.32,834.21,4,21.1),(a,b,d),("Hola todos!",23,95.3,"Ciao mondo!"),("Laszlo Tabori","Albert-Laszlo Barabasi",12.239,None),(32,54,76,(9.1,8.2,3.8)))
		prompt = "	... is_t_of_ts(t of ts) == True, subtup with tuple	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_tuple_of_tuples(d):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method determining if an element 'elem'
	#		is in the given input argument, which is a tuple of
	#		tuples.
	#	@param op_f_obj - output file object to print software
	#		testing results to.
	#	@return - Nothing.
	#	O(nm) method, where 'n' is the size of the the tuple of
	#		tuples (or number of subtuples/sub-tuples), and 'm' is
	#		the size of the largest tuple (or subtuples/sub-tuples)
	#		in the tuple of tuples.
	@staticmethod
	def test_is_elem_in_tuple_of_tuples(op_f_obj):
		op_f_obj.write("	Testing is_elem_in_tuple_of_tuples() method.")
		prompt = "	... i/p arguments: (None,None) => False			{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_elem_in_tuple_of_tuples(None,None):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		not_a_tuple_obj = data_type_n_number_ops()
		a_tuple = (1234,56.789,"Ciao mondo")
		prompt = "	... i/p args: (not_a_tuple_obj,tuple) => False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_elem_in_tuple_of_tuples(not_a_tuple_obj,a_tuple):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		a = data_type_n_number_ops()
		b = data_type_n_number_ops()
		c = data_type_n_number_ops()
		tuple_of_subtuples = ((19,28,37,46,5.5),("Ciao mondo!", "Koszonom", "Hola todos"),(a,b,not_a_tuple_obj,c))
		prompt = "	i/p args: (None,tuple_of_tuples) => False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_elem_in_tuple_of_tuples(None,tuple_of_subtuples):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	i/p args: ('not found',tuple_of_tuples) => False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_elem_in_tuple_of_tuples("not found",tuple_of_subtuples):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	i/p args: (21.3243,tuple_of_tuples) => False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_elem_in_tuple_of_tuples(21.3243,tuple_of_subtuples):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	i/p args: (6734,tuple_of_tuples) => False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_elem_in_tuple_of_tuples(6734,tuple_of_subtuples):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		d = data_type_n_number_ops()
		prompt = "	i/p args: (random_obj,tuple_of_tuples) => False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_elem_in_tuple_of_tuples(d,tuple_of_subtuples):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	i/p args: (not_a_tuple_obj,tuple_of_tuples) => True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_elem_in_tuple_of_tuples(not_a_tuple_obj,tuple_of_subtuples):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	i/p args: (46,tuple_of_tuples) => True			{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_elem_in_tuple_of_tuples(46,tuple_of_subtuples):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	i/p args: ('Hola todos',tuple_of_tuples) => True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_elem_in_tuple_of_tuples("Hola todos",tuple_of_subtuples):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	i/p args: (object_b,tuple_of_tuples) => True		{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_elem_in_tuple_of_tuples(b,tuple_of_subtuples):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		e = (tuple_of_subtuples,("Laszlo Tabori","Albert-Laszlo Barabasi",12.239,None))
		prompt = "	i/p args: (None,another_tuple_of_tuples) => True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_elem_in_tuple_of_tuples(None,e):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		e = (tuple_of_subtuples,("Laszlo Tabori","Albert-Laszlo Barabasi",12.239,None),(32,54,76,(9.1,8.2,3.8)))
		prompt = "	i/p args: (a_tuple,another_tuple_of_tuples) => True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_elem_in_tuple_of_tuples((9.1,8.2,3.8),e):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method to check if the input argument
	#		is a binary string.
	#	@param op_f_obj - output file object to print software
	#		testing results to.
	#	@return - Nothing.
	#	O(n) method, where "n" is the maximum size of the lists
	#		being tested.
	@staticmethod
	def test_is_binary_string(op_f_obj):
		#op_f_obj.write("	Testing is_binary_string() method.")
		op_f_obj.write("	Testing is_binary_string() method.")
		binary_string = None
		prompt = "	... Test: is_binary_string(None) == False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_binary_string(binary_string):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		not_a_bin_str = data_type_n_number_ops()
		prompt = "	... Test: is_binary_string(not_a_bin_str) == False	{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_binary_string(not_a_bin_str):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: is_binary_string('') == False			{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_binary_string(""):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: is_binary_string(23) == False			{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_binary_string(23):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: is_binary_string('23') == False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_binary_string("23"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: is_binary_string('0b728346') == False		{}"
		statistical_analysis.increment_number_test_cases_used()
		if False == data_type_n_number_ops.is_binary_string("0b728346"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: is_binary_string('0101101') == True		{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_binary_string("0101101"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: is_binary_string('0b0001101') == True		{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_binary_string("0b0001101"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: is_binary_string('1101') == True		{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_binary_string("1101"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: is_binary_string('0b10101011') == True	{}"
		statistical_analysis.increment_number_test_cases_used()
		if True == data_type_n_number_ops.is_binary_string("0b10101011"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the method to convert a binary string to a
	#		list of 0-1 integers.
	#	@param op_f_obj - output file object to print software
	#		testing results to.
	#	@return - Nothing.
	#	O(n) method, where "n" is the maximum size of the lists
	#		being tested.
	@staticmethod
	def test_convert_binary_string_to_list_of_0_1_integers(op_f_obj):
		#op_f_obj.write("	Testing convert_bin...str...to_list_of_0_1_int...() method.")
		op_f_obj.write("	Testing convert_bin_str_to_list_of_0s_1s() method.")
		binary_string = None
		#prompt = "	... Test: convert_bin_str_to_list_of_0_1_int(None) == None		{}"
		prompt = "	... Test: convert_bin_str_to_0_1_list(None) == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers(binary_string):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		not_a_bin_str = data_type_n_number_ops()
		#prompt = "	... Test: convert_bin_str_to_list_of_0_1_int(not_a_bin_str) == None	{}"
		prompt = "	... Test: conv_binstr_to_0_1_list(not_bin_str) == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers(not_a_bin_str):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: convert_bin_str_to_0_1_list('') == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers(""):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: convert_bin_str_to_list(23) == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers(23):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: convert_bin_str_to_list('23') == None		{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("23"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: convert_bin_str_to_list('1073262') == None	{}"
		statistical_analysis.increment_number_test_cases_used()
		if None == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("1073262"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: '0' == [0]					{}"
		statistical_analysis.increment_number_test_cases_used()
		if [0] == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("0"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: '010011' == [0,1,0,0,1,1]			{}"
		statistical_analysis.increment_number_test_cases_used()
		if [0,1,0,0,1,1] == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("010011"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: '00011011' == [0,0,0,1,1,0,1,1]		{}"
		statistical_analysis.increment_number_test_cases_used()
		if [0,0,0,1,1,0,1,1] == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("00011011"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: '0b0' == [0]					{}"
		statistical_analysis.increment_number_test_cases_used()
		if [0] == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("0b0"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: '0b01011' == [0,1,0,1,1]			{}"
		statistical_analysis.increment_number_test_cases_used()
		if [0,1,0,1,1] == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("0b01011"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: '110101' == [1,1,0,1,0,1]			{}"
		statistical_analysis.increment_number_test_cases_used()
		if [1,1,0,1,0,1] == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("110101"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: '1' == [1]					{}"
		statistical_analysis.increment_number_test_cases_used()
		if [1] == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("1"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: '11' == [1,1]					{}"
		statistical_analysis.increment_number_test_cases_used()
		if [1,1] == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("11"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: '0b1' == [1]					{}"
		statistical_analysis.increment_number_test_cases_used()
		if [1] == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("0b1"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: '0b1101' == [1,1,0,1]				{}"
		statistical_analysis.increment_number_test_cases_used()
		if [1,1,0,1] == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("0b1101"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
		prompt = "	... Test: '0b1000111' == [1,0,0,0,1,1,1]		{}"
		statistical_analysis.increment_number_test_cases_used()
		if [1,0,0,0,1,1,1] == data_type_n_number_ops.convert_binary_string_to_list_of_0_1_integers("0b1000111"):
			op_f_obj.write(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			op_f_obj.write(prompt .format("FAIL!!!"))
	## =========================================================
	#	Method to test the methods that operate on basic data
	#		types and numbers, which belong to the class
	#		data_type_n_number_ops.
	#	@param op_f_obj - output file object to print software
	#		testing results to.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_data_type_n_number_ops(op_f_obj):
		op_f_obj.write("")
		op_f_obj.write("")
		op_f_obj.write("==	Testing class: data_type_n_number_ops.")
		op_f_obj.write("")
		data_type_n_number_ops_tester.test_is_list_of_numbers(op_f_obj)
		op_f_obj.write("")
		data_type_n_number_ops_tester.test_is_tuple_of_tuples(op_f_obj)
		op_f_obj.write("")
		data_type_n_number_ops_tester.test_is_elem_in_tuple_of_tuples(op_f_obj)
		op_f_obj.write("")
		data_type_n_number_ops_tester.test_is_binary_string(op_f_obj)
		op_f_obj.write("")
		data_type_n_number_ops_tester.test_convert_binary_string_to_list_of_0_1_integers(op_f_obj)
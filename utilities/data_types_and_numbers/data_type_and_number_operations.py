#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to implement
		operations regarding basic data types and numbers supported
		by the Python Standard Library.
	1) Check if a list is a list of numbers.
	2) Convert a binary string to a list of integers.


	Synopsis:
	Perform operations on basic data types and numbers.


	


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
import os
import os.path
#from subprocess import call
import subprocess
#import time
import warnings
#import re
import calendar
from calendar import month_name

###############################################################
#	Import Custom Python Modules



###############################################################
##	Module with methods that perform operations regarding basic
#		data types and numbers.
class data_type_n_number_ops:
	# =========================================================
	#	Method to determine if each object in a list is an integer
	#		or a floating-point number.
	#	@param list - A list of objects, for which we want to
	#					determine if each of its elements is an
	#					integer or a floating-point number.
	#	@return - Boolean true if each element of the list is an
	#				integer or a floating-point number.
	#	O(n) method, where "n" is the size of the list.
	#	Tested.
	@staticmethod
	def is_list_of_numbers(list_of_objects=[]):
		# Is "list_of_numbers" a None object?
		if list_of_objects is None:
			# Yes. "list_of_numbers" is a None object.
			return False
		# Is "list_of_objects" not a list?
		elif not isinstance(list_of_objects, list):
			# Yes. "list_of_objects" is not a list.
			return False
		# Else, is list_of_objects an empty list?
		#elif 0 == len(list_of_objects):
		elif not list_of_objects:	# More Pythonic solution.
			return False
		else:
			for elem in list_of_objects:
				if not isinstance(elem, (int, float)):
					return False
				# Else, proceed to the next element.
			"""
				None of the elements in "list_of_objects"
					is an integer or a floating-point number.
			"""
			return True
	# =========================================================
	#	Method to convert a binary string to a list of 0-1
	#		integers.
	#	@param a_binary_string - binary string to be converted
	#		a list of 0-1 integers.
	#	@return - A list of 0-1 integers representing the binary
	#		string.
	#	@precondition - If the a_binary_string is not a string,
	#		including a None object, return a None object.
	#	O(n) method, where "n" is the number of bits of the
	#		binary string.
	#	Tested.
	@staticmethod
	def convert_binary_string_to_list_of_0_1_integers(a_binary_string):
		# Is the input argument a 'None' object?
		if a_binary_string is None:
			"""
				Yes. Don't try to convert the input argument to a
					list of 0-1 integers.
			"""
			return None
		# Is the input argument not a string?
		elif not isinstance(a_binary_string, str):
			"""
				Yes. Don't try to convert the input argument to a
					list of 0-1 integers.
			"""
			return None
		else:
			# Else, the input argument is a string. Get its length.
			number_of_bits_in_bin_str = len(a_binary_string)
			# Does the string start with "0b"?
			if a_binary_string.startswith("0b"):
				# Yes. Reduce its length by 2.
				number_of_bits_in_bin_str = number_of_bits_in_bin_str - 2
				# Is the number of characters of the string less than 1?
				if number_of_bits_in_bin_str < 1:
					"""
						Yes. Don't try to convert the input argument to a
							list of 0-1 integers.
					"""
					return None
				else:
					
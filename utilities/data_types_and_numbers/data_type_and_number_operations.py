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



	Important Notes:
	+ From \cite{ReinstateMonicaZeta2020}, there exists no basic
		data type for binary numbers.
		- Binary representations of numbers that begin with "0b"
			are integers;
			when the values of these integers are printed/read,
				the decimal (numeral system) values of these
				integers are printed.
		- To represent an integer as a binary number by default,
			I need to do so via a custom-defined class.
			* Since I do not want to extend the parent class
				'integer' and am only supporting a small number
				of functions, I am currently not defining a custom
				class to represent binary numbers.
		- Also, since I cannot easily obtain the binary representation
			of a number and operate with it (e.g., determining
			its base - that is, base 2), I am not providing a
			method to test if this integer is in its binary
			representation.

	



	References:
	+ \cite{WikipediaContributors2019i}
		- Wikipedia contributors, "CAR and CDR," in Wikipedia, The Free
			Encyclopedia: Lisp (programming language), Wikimedia Foundation,
			San Francisco, CA, August 28, 2019.
			Available online from Wikipedia, The Free Encyclopedia:
				Lisp (programming language) at: https://en.wikipedia.org/wiki/CAR_and_CDR;
				February 19, 2020 was the last accessed date.



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
	#	@param list_of_objects - A list of objects, for which we
	#		want to determine if each of its elements is an
	#		integer or a floating-point number.
	#	@return - Boolean true if each element of the list is an
	#				integer or a floating-point number.
	#	O(n) method, where "n" is the size of the list.
	#	Tested.
	@staticmethod
	def is_list_of_numbers(list_of_objects=[]):
		# Is "list_of_objects" a None object?
		if list_of_objects is None:
			# Yes. "list_of_objects" is a None object.
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
				Each elements in "list_of_objects" is an integer
					or a floating-point number.
			"""
			return True
	# =========================================================
	#	Method to determine if the input argument is a tuple,
	#		and if each object in the tuple is a tuple.
	#	@param tuple_of_tuples - A tuple of tuples, for which we
	#		want to determine if each of its elements is a tuple.
	#	@return - Boolean true if the input argument is a tuple,
	#		and each element of the tuple is a tuple, too.
	#	O(nm) method, where "n" is the size of the the tuple of
	#		tuples, and m is the size of the largest tuple in
	#		the tuple of tuples.
	#	Tested.
	@staticmethod
	def is_tuple_of_tuples(tuple_of_tuples=()):
		# Is "tuple_of_tuples" a None object?
		if tuple_of_tuples is None:
			# Yes. "tuple_of_tuples" is a None object.
			return False
		# Is "tuple_of_tuples" not a tuple?
		elif not isinstance(tuple_of_tuples, tuple):
			# Yes. "tuple_of_tuples" is not a tuple.
			return False
		# Else, is tuple_of_tuples an empty tuple?
		#elif 0 == len(tuple_of_tuples):
		elif not tuple_of_tuples:	# More Pythonic solution.
			return False
		else:
			# For each element in the tuple of tuples...
			for elem in tuple_of_tuples:
				# Is this element a tuple?
				if not isinstance(elem, tuple):
					# No.
					return False
				# Else, proceed to the next element.
				else:
					continue
			#Each element in "tuple_of_tuples" is a tuple.
			return True
	# =========================================================
	#	Method to determine if each object in a list is an
	#		integer or a floating-point number in its low or high
	#		value for a RTW signal or a bit vector.
	#	@param list - A list of objects, for which we want to
	#		determine if each of its elements is a low or high
	#		value of a RTW signal or a bit vector.
	#	@low_high_values - A tuple of tuples, such that each tuple
	#		is a tuple of low value and high value for a random
	#		process/signal, specifically for a RTW signal or bit
	#		vector (or 0s and 1s).
	#	@return - boolean True if each element of the list is a
	#		low or high value of a RTW signal or a bit vector;
	#		else, return boolean False.
	#	O(n) method, where "n" is the size of the list.
	#
	#	Notes:
	#	+ Use low_high_values=(low value, high value) as a tuple,
	#		or low_high_values = ((low value 1, high value 1),
	#		(low value 2, high value 2), ...,
	#		(low value n, high value n)) as a tuple of tuples,
	#		representing the low and high values of a RTW signal
	#		or a bit vector.
	#		That way, (low value, high value) implies that the
	#			random process/signal/string represents only a
	#			random process/signal/string.
	#
	#	[Wikipedia contributors2019]
	#
	#	Not Tested.
	@staticmethod
	#def is_list_of_low_high_values(list_of_objects=[], low_high_values=((-1,0.5), (-1,1), (-0.5,0.5), (-0.5,1), (0,1)):
	def is_list_of_low_high_values(list_of_objects=[], low_high_values=(-1,0.5)):
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
			# Yes.
			return False
		# Else, the list of objects is not an empty list.
		else:
			# For each object in the list.
			for elem in list_of_objects:
				# Is this object an integer or floating-point number?
				if not isinstance(elem, (int, float)):
					# No.
					return False
				# Else, proceed to the next element.
				elif elem not in low_high_values:
					return False
				# Else, proceed to the next element.
				else:
					# Now, pass or continue.
					continue
			"""
				None of the elements in "list_of_objects"
					is an integer or a floating-point number.
			"""
			return True
	# =========================================================
	#	Method to test if the input argument is a binary string.
	#	@param possible_bin_str - An input argument to be checked
	#		if it is a binary string.
	#	@return - boolean True, if 'possible_bin_str' is a binary
	#		string; else, return boolean False.
	#	@preconditions - If 'possible_bin_str' is not a string,
	#		including a None object, return False.
	#	O(n) method, where "n" is the number of characters in the
	#		string, or is the number of bits of the binary string.
	#	Not Tested.
	@staticmethod
	def is_binary_string(possible_bin_str):
		# Is the input argument a 'None' object?
		if possible_bin_str is None:
			# Yes.
			return False
		# Else, is the input argument not a string?
		elif not isinstance(possible_bin_str, str):
			# Yes.
			return False
		# This input argument is a string.
		#	Is this string empty?
		elif not possible_bin_str:
			# Yes.
			return False
		else:
			"""
				Else, the input argument is a string.
				Does the string start with "0b"?
			"""
			if possible_bin_str.startswith("0b"):
				# Yes. Trim/remove the 1st 2 chgaracters from it.
				possible_bin_str = possible_bin_str[2:]
			"""
				Initialize list to store 0, 1 integers from the
					binary string.
			"""
			list_of_int_representation_of_bv = []
			# Enumerate each character in the binary string.
			for current_character in possible_bin_str:
				# Is the current character is not '0' nor '1'?
				if ('0' != current_character) and ('1' != current_character):
					# Yes.
					return False
			# Each character in this string is binary.
			return True
	# =========================================================
	#	Method to convert a binary string to a list of 0-1
	#		integers.
	#	@param a_binary_string - binary string to be converted
	#		a list of 0-1 integers.
	#	@return - A list of 0-1 integers representing the binary
	#		string.
	#	@preconditions - If 'a_binary_string' is not a binary string,
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
		# Else, is the input argument not a string?
		elif not isinstance(a_binary_string, str):
			"""
				Yes. Don't try to convert the input argument to a
					list of 0-1 integers.
			"""
			return None
		# Else, is this string empty? 
		elif not a_binary_string:
			# Yes.
			return None
		else:
			"""
				Else, the input argument is a string.
				Does the string start with "0b"?
			"""
			if a_binary_string.startswith("0b"):
				# Yes. Trim/remove the 1st 2 chgaracters from it.
				a_binary_string = a_binary_string[2:]
			"""
				Initialize list to store 0, 1 integers from the
					binary string.
			"""
			list_of_int_representation_of_bv = []
			# Enumerate each character in the binary string.
			for current_character in a_binary_string:
				# If the current character is not '0' and '1'?
				if ('0' != current_character) and ('1' != current_character):
					# 
					return None
				"""
					Cast it into an integer and add it to the
						list representation of the binary string.
				"""
				list_of_int_representation_of_bv.append(int(current_character))
			return list_of_int_representation_of_bv
	# =========================================================
	#	Method to check if an element is in a tuple of tuples.
	#	@param elem - An element that we want to check if it is in
	#		the tuple of tuples, tuple_of_tuples.
	#	@param tuple_of_tuples - A tuple of tuples to be converted
	#		a list of 0-1 integers.
	#	@return - boolean True, if 'elem' is in 'tuple_of_tuples';
	#		else, return boolean False.
	#	@preconditions - If 'tuple_of_tuples' is not a tuple of tuples,
	#		return False.
	#	O(nm) method, where 'n' is the number of subtuples/sub-tuple
	#		of the tuple and 'm' is the number of elements in the
	#		largest subtuples/sub-tuple.
	#	Tested.
	@staticmethod
	def is_elem_in_tuple_of_tuples(elem,tuple_of_tuples):
		"""
		if elem is not None:
			return False
		"""
		# Is 'tuple_of_tuples' a tuple of tuples?
		if not data_type_n_number_ops.is_tuple_of_tuples(tuple_of_tuples):
			# No.
			return False
		else:
			# Yes. Enumerate each subtuple/sub-tuple in the tuple.
			for index, cur_tuple in enumerate(tuple_of_tuples):
				if elem in cur_tuple:
					# 'elem' exists in 'tuple_of_tuples'.
					return True
				else:
					# Or, continue
					"""
						print(">	elem is:", elem,"=")
						print(">	cur_tuple is:", cur_tuple,"=")
					"""
					pass
			# 'elem' does not exist in 'tuple_of_tuples'.
			return False
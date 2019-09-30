#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3


"""
	This Python script is written by Zhiyang Ong to perform
		miscellaneous tasks in analyzing data.


	Synopsis:
	Perform miscellaneous tasks in data analysis.


	Revision History:
	December 15, 2017			Version 0.1, initial build.



	Reference:
	\cite{WikipediaContributors2019g}
		@misc{WikipediaContributors2019g,
			Address = {San Francisco, {CA}},
			Author = {{Wikipedia contributors}},
			Howpublished = {Available online from {\it Wikipedia, The Free Encyclopedia: Measurement} at: \url{https://en.wikipedia.org/wiki/Relative_change_and_difference}; October 1, 2019 was the last accessed date},
			Month = {September 25},
			Publisher = {Wikimedia Foundation},
			Title = {Relative change and difference},
			Url = {https://en.wikipedia.org/wiki/Relative_change_and_difference},
			Year = {2019}}
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'December 15, 2017'

#	The MIT License (MIT)

#	Copyright (c) <2014-2018> <Zhiyang Ong>

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






###############################################################
"""
	Module with methods that perform basic statistical analysis
		during software test automation.
"""
class data_analysis:
	#	Static variable declaration.
	#
	"""
		Dictionary of reference values.
		
		References:
			https://en.wikipedia.org/wiki/List_of_physical_constants
			https://en.wikipedia.org/wiki/Physical_constant
			https://en.wikipedia.org/wiki/List_of_common_physics_notations
	"""
	dict_of_reference_values = {"c":299792458, "standard acceleration due to gravity":9.80665, "standard atmosphere":101325}
	# =========================================================
	#	Method to access the reference value for a particular
	#		attribute/property.
	#	\cite{WikipediaContributors2019g}
	#	@return - The reference value for a particular attribute/property.
	#	O(1) method.
	@staticmethod
	def get_reference_value(property="c"):
		return statistical_analysis.dict_of_reference_values[property]
	# =========================================================
	#	Method to determine the actual change between quantity1 and
	#		quantity2.
	#	\cite{WikipediaContributors2019g}
	#	@param quantity1 - A quantity that I want to find the actual
	#		change of.
	#	@param quantity2 - Another quantity that I want to find the
	#		actual change of.
	#	@return - The actual change.
	#	O(1) method.
	@staticmethod
	def get_actual_change(quantity1=0,quantity2=0):
		return (quantity1 - quantity2)
	# =========================================================
	#	Method to determine the absolute difference between quantity1
	#		and quantity2.
	#	\cite{WikipediaContributors2019g}
	#	@param quantity1 - A quantity that I want to find the
	#		absolute difference of.
	#	@param quantity2 - Another quantity that I want to find the
	#		absolute difference of.
	#	@return - The absolute difference.
	#	@postcondition - absolute difference |quantity1 - quantity2| >= 0.
	#	O(1) method.
	#	Reference:
	#		https://en.wikipedia.org/wiki/Absolute_difference
	@staticmethod
	def get_absolute_difference(quantity1=0,quantity2=0):
		absolute_difference = abs(quantity1 - quantity2)
		if (0 > absolute_difference):
			raise Exception("	Absolute difference must be non-negative.")
		return absolute_difference
	# =========================================================
	#	Method to determine the relative change between quantity
	#		quantity1 and ref_qty (the reference quantity).
	#	\cite{WikipediaContributors2019g}
	#	@param quantity1 - A quantity that I want to find the
	#		relative change of.
	#	@param ref_qty - A reference quantity that I want to find
	#		the relative change of.
	#	@return - The relative change.
	#	O(1) method.
	@staticmethod
	def get_relative_change(quantity1=1,ref_qty=1):
		return (get_actual_change(quantity1,ref_qty)/ref_qty)
	# =========================================================
	#	Method to determine the relative difference between
	#		quantity quantity1 and quantity quantity2.
	#	\cite{WikipediaContributors2019g}
	#	@param quantity1 - A quantity that I want to find the
	#		relative difference of.
	#	@param quantity2 - Another quantity that I want to find
	#		the relative difference of.
	#	@return - The relative difference.
	#	@postcondition - absolute difference |quantity1 - quantity2| >= 0.
	#	O(1) method.
	#	Reference:
	#		https://en.wikipedia.org/wiki/Absolute_difference
	@staticmethod
	def get_relative_difference(quantity1=1,ref_qty=1):
		sw
	
	
	
	
	
	
	
		return (get_actual_change(quantity1,ref_qty)/ref_qty)
	# =========================================================
	#	Mutator methods.
	# =========================================================
	#	Method to increment the number of test cases used.
	#	@return - Nothing.
	#	@postcondition - number_test_cases_used < number_test_cases_passed.
	#	O(1) method.
	@staticmethod
	def increment_number_test_cases_used():
		if 0 == statistical_analysis.get_number_test_cases_used():
			statistical_analysis.number_test_cases_used = 1
		else:
			statistical_analysis.number_test_cases_used = statistical_analysis.number_test_cases_used + 1
		if (statistical_analysis.get_number_test_cases_used() < statistical_analysis.number_test_cases_passed):
			print("	Problem: number_test_cases_used < number_test_cases_passed")
			raise Exception("	Error in incrementing number_test_cases_used")
	# =========================================================
	#	Method to increment the number of test cases passed.
	#	@return - Nothing.
	#	@postcondition - number_test_cases_used < number_test_cases_passed.
	#	O(1) method.
	@staticmethod
	def increment_number_test_cases_passed():
		if 0 == statistical_analysis.number_test_cases_passed:
			statistical_analysis.number_test_cases_passed = 1
		else:
			statistical_analysis.number_test_cases_passed = statistical_analysis.number_test_cases_passed + 1
		if (statistical_analysis.get_number_test_cases_used() < statistical_analysis.get_number_test_cases_passed()):
			print("Number of test cases passed:	{}" .format(statistical_analysis.get_number_test_cases_passed()))
			print("Number of test cases used:	{}" .format(statistical_analysis.get_number_test_cases_used()))
			print("	Problem: number_test_cases_used < number_test_cases_passed")
			raise Exception("	Error with number_test_cases_used.")
	# =========================================================
	#	Other methods.
	# =========================================================
	#	Method to determine percentage of test cases passed.
	#	@return - percentage of test cases passed.
	#	@precondition - number_test_cases_used < number_test_cases_passed.
	#	O(1) method.
	@staticmethod
	def get_test_cases_passed_average():
		if 0 == statistical_analysis.number_test_cases_used:
			return 0
		else:
			if (statistical_analysis.get_number_test_cases_used() < statistical_analysis.get_number_test_cases_passed()):
				print("	Problem: number_test_cases_used < number_test_cases_passed")
				raise Exception("	Precondition failed (1): see number_test_cases_used or number_test_cases_passed.")
			return (statistical_analysis.get_number_test_cases_passed()*100 / statistical_analysis.get_number_test_cases_used())
	# =========================================================
	#	Method to print statistics of software testing results.
	#	@return - Nothing
	#	@precondition - number_test_cases_used < number_test_cases_passed.
	#	O(1) method.
	@staticmethod
	def print_statistics_of_software_testing():
		if (statistical_analysis.get_number_test_cases_used() < statistical_analysis.get_number_test_cases_passed()):
			print("	Problem: number_test_cases_used < number_test_cases_passed")
			raise Exception("	Precondition failed (2): see number_test_cases_used or number_test_cases_passed.")
		print("*	Number of test cases passed:		{}" .format(statistical_analysis.get_number_test_cases_passed()))
		print("*	Number of test cases used:		{}" .format(statistical_analysis.get_number_test_cases_used()))
		print("*	Percentage of test cases passed:	{}%." .format(statistical_analysis.get_test_cases_passed_average()))
		#print "*	Percentage of test cases passed:	",statistical_analysis.get_test_cases_passed_average(),"%."
		#	Format printing of the statistics as follows.
		#print "*	Percentage of test cases passed:	",(13*100/19),"%."
		#	Most of the following cannot calculate the percentage properly.
		#print "*	Percentage of test cases passed:	",(13/19)*100,"%."
		#print "*	Percentage of test cases passed:	",(13/19)*(10000/100),"%."
		#print "*	Percentage of test cases passed:	",(10000/100)*(13/19),"%."
		#print "*	Percentage of test cases passed:	",(13*10000)/(19*100),"%."

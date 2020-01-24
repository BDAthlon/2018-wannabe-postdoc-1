#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to test
		implementations of mathematical operations with numbers.
	

	Synopsis:
	Test mathematical operations with numbers from the
		"number_operations" module.


	


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
	math	For mathematical operations with numbers.
"""

import math




###############################################################
#	Import Custom Python Modules

# Package and module to perform mathematical operations with numbers.
from utilities.number_operations import number_ops


"""
	Package and module to print statistics of software testing
		results.
"""
from statistic_pkg.test_statistics import statistical_analysis

###############################################################
##	Module that tests methods that perform mathematical operations
#		with numbers
class number_ops_tester:
	## =========================================================
	#	Method to test the methods that perform file I/O operations
	#		with an invalid file.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_get_nearest_integer():
		print("	Testing method to round off floating-point numbers.")
		prompt = "	... Test: 32.5445 -> 33?				{}"
		statistical_analysis.increment_number_test_cases_used()
		if 33 == number_ops.get_nearest_integer(32.5445):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: 8127.9145 -> 8128?				{}"
		statistical_analysis.increment_number_test_cases_used()
		if 8128 == number_ops.get_nearest_integer(8127.9145):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test: 5.19145 -> 5?					{}"
		statistical_analysis.increment_number_test_cases_used()
		if 5 == number_ops.get_nearest_integer(5.19145):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))


	## =========================================================
	#	Method to test methods that perform mathematical operations.
	#	@param - Nothing
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_mathematical_methods():
		print("")
		print("")
		print("==	Testing class: number_ops.")
		number_ops_tester.test_get_nearest_integer()

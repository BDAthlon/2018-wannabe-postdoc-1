#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to test
		the constructors and methods of the vertex class.

	Synopsis:
	Test all constructors and methods of the vertex class.

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
	calendar	For calendar-related functions.
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
import calendar


###############################################################
#	Import Custom Python Modules

"""
	Package and module to print statistics of software testing
		results.
"""
from statistic_pkg.test_statistics import statistical_analysis
# Package and module to representing the vertex class of the graph.
from data_structures.vertex import vertex

"""
	Module that tests the methods for accessing and modifying
		vertices of a generic graph.

	Support for class instantiation is not provided, to avoid
		acquiring a collection of useless "vertex_tester" and
		"vertex" objects.
"""
class vertex_tester:
	# =========================================================
	##	Method to test the methods that for accessing and
	#		modifying vertices of a generic graph.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_generic_vertex():
		print("==	Testing class: vertex.")
		vertex_tester.test_constructors_and_equality_comparison()
		vertex_tester.test_pairs_of_accessor_mutator_methods()
	# =========================================================
	##	Method to test constructors and equality comparison method
	#		for the vertex class.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_constructors_and_equality_comparison():
		prompt = "	... Test default constructor of vertex	 		{}."
		statistical_analysis.increment_number_test_cases_used()
		if vertex() is not None:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test standard constructor of vertex			{}."
		statistical_analysis.increment_number_test_cases_used()
		if vertex(45678) is not None:
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		a = vertex()
		b = vertex()
		prompt = "	... Test instances of default constructor		{}."
		statistical_analysis.increment_number_test_cases_used()
		# Compare the object identities and object values.
		if (a is not b) and (a == b):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			print("	a is not b",a is not b,"=")
			print("	a == b",a == b,"=")
		a = vertex(45678)
		b = vertex(353453423)
		prompt = "	... Test instances of standard constructor (!= values)	{}."
		statistical_analysis.increment_number_test_cases_used()
		# Compare the object identities and object values.
		if (a is not b) and (a != b):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		a = vertex(45678)
		b = vertex(45678)
		prompt = "	... Test instances of standard constructor (== values)	{}."
		statistical_analysis.increment_number_test_cases_used()
		# Compare the object identities and object values.
		if (a is not b) and (a == b):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		a = vertex(45678)
		b = vertex()
		prompt = "	... Test instances of different constructors		{}."
		statistical_analysis.increment_number_test_cases_used()
		# Compare the object identities and object values.
		if (a is not b) and (a != b):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
	# =========================================================
	##	Method to test pairs of methods that for accessing and
	#		modifying vertices of a generic graph.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_pairs_of_accessor_mutator_methods():
		a = vertex()
		#print("a.get_id():::",a.get_id(),"=")
		prompt = "	... Test: get_id(), vertex()			 	{}."
		statistical_analysis.increment_number_test_cases_used()
		#if (a.get_id()) == sys.maxsize:
		#if sys.maxsize == a.get_id():
		if sys.maxsize == a.get_id():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		b = 72342787
		a = vertex(b)
		prompt = "	... Test: get_id(), vertex(72342787) 			{}."
		statistical_analysis.increment_number_test_cases_used()
		#if (a.get_id()) == sys.maxsize:
		#if sys.maxsize == a.get_id():
		if b == a.get_id():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		b = 234
		a.set_id(b)
		prompt = "	... Test: set_id(234)		 			{}."
		statistical_analysis.increment_number_test_cases_used()
		#if (a.get_id()) == sys.maxsize:
		#if sys.maxsize == a.get_id():
		if b == a.get_id():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))

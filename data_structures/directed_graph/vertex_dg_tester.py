#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This Python script is written by Zhiyang Ong to test
		the constructors and methods of the vertex class
		of a directed graph.

	Synopsis:
	Test all constructors and methods of the vertex class
		of a directed graph.

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
from statistics.test_statistics import statistical_analysis
# Package and module to representing the vertex class of the graph.
from data_structures.vertex import vertex
from data_structures.directed_graph.vertex_dg import *

"""
	Module that tests the methods for accessing and modifying
		vertices of a directed graph.

	Support for class instantiation is not provided, to avoid
		acquiring a collection of useless "vertex_dg_tester"
		and "vertex_dg" objects.
"""
class vertex_dg_tester:
	# =========================================================
	##	Method to test the methods that for accessing and
	#		modifying vertices of a directed graph.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_vertex_dg():
		print("")
		print("==	Testing class: vertex_dg.")
		vertex_dg_tester.test_constructors_and_equality_comparison()
		vertex_dg_tester.test_pairs_of_accessor_mutator_methods()
	# =========================================================
	##	Method to test constructors and equality comparison method
	#		for the vertex_dg class.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_constructors_and_equality_comparison():
		prompt = "	... Test default constructor of vertex_dg	 	{}."
		statistical_analysis.increment_number_test_cases_used()
		a = vertex_dg()
		if (a is not None) and (sys.maxsize == a.get_id()):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test standard constructor of vertex: id		{}."
		statistical_analysis.increment_number_test_cases_used()
		a_id = 45678
		a = vertex_dg(a_id)
		if (a is not None) and (a_id == a.get_id()):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		a = vertex_dg(1)
		b = vertex_dg(2)
		f_in_edges = [a, b]
		c = vertex_dg(3)
		d = vertex_dg(4)
		e = vertex_dg(5)
		f_out_edges = [c, d, e]
		f_id = 6
		f = vertex_dg(f_id, f_in_edges, f_out_edges)
		prompt = "	... Test standard constructor of vertex: 3 parameters	{}."
		statistical_analysis.increment_number_test_cases_used()
		if (f is not None) and (f_id == f.get_id()):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		f = vertex_dg(None, f_in_edges, f_out_edges)
		prompt = "	... Test standard constructor of vertex: last 2 params	{}."
		statistical_analysis.increment_number_test_cases_used()
		if (f is not None) and (sys.maxsize == f.get_id()):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			print("f.get_id():::",f.get_id(),"=")
		prompt = "	... Test instances of default constructor		{}."
		statistical_analysis.increment_number_test_cases_used()
		a = vertex_dg()
		b = vertex_dg()
		# Compare the object identities and object values.
		if (a is not b) and (a == b):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
			print("	a is not b",a is not b,"=")
			print("	a == b",a == b,"=")
		prompt = "	... Test instances of standard constructor (!= IDs)	{}."
		statistical_analysis.increment_number_test_cases_used()
		a = vertex_dg(45678)
		b = vertex_dg(353453423)
		# Compare the object identities and object values.
		if (a is not b) and (a != b):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test instances of standard constructor (!= values)	{}."
		statistical_analysis.increment_number_test_cases_used()
		a = vertex_dg(1)
		b = vertex_dg(2)
		f_in_edges = [a, b]
		c = vertex_dg(3)
		d = vertex_dg(4)
		e = vertex_dg(5)
		f_out_edges = [c, d, e]
		f_id = 6
		f = vertex_dg(f_id, f_in_edges, f_out_edges)
		g_in_edges = [a]
		g_out_edges = [c, e]
		g_id = 7
		g = vertex_dg(g_id, g_in_edges, g_out_edges)
		# Compare the object identities and object values.
		if (a is not b) and (a != b):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test instances of standard constructor (== IDs)	{}."
		statistical_analysis.increment_number_test_cases_used()
		a = vertex_dg(45678)
		b = vertex_dg(45678)
		# Compare the object identities and object values.
		if (a is not b) and (a == b):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test instances of standard constructor (== values)	{}."
		statistical_analysis.increment_number_test_cases_used()
		a = vertex_dg(1)
		b = vertex_dg(2)
		f_in_edges = [a, b]
		c = vertex_dg(3)
		d = vertex_dg(4)
		e = vertex_dg(5)
		f_out_edges = [c, d, e]
		f_id = 6
		f = vertex_dg(f_id, f_in_edges, f_out_edges)
		g = vertex_dg(f_id, f_in_edges, f_out_edges)
		# Compare the object identities and object values.
		if (a is not b) and (a == b):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test instances of different constructors (1)	{}."
		statistical_analysis.increment_number_test_cases_used()
		a = vertex_dg(45678)
		b = vertex_dg()
		# Compare the object identities and object values.
		if (a is not b) and (a != b):
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		prompt = "	... Test instances of different constructors (2)	{}."
		statistical_analysis.increment_number_test_cases_used()
		a = vertex_dg(1)
		b = vertex_dg(2)
		f_in_edges = [a, b]
		c = vertex_dg(3)
		d = vertex_dg(4)
		e = vertex_dg(5)
		f_out_edges = [c, d, e]
		f_id = 6
		f = vertex_dg(f_id)
		g = vertex_dg(f_id, g_in_edges, g_out_edges)
		# Compare the object identities and object values.
		if (f is not g) and (f != g):
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
		a = vertex_dg()
		#print("a.get_id():::",a.get_id(),"=")
		prompt = "	... Test: get_id(), vertex_dg()			 	{}."
		statistical_analysis.increment_number_test_cases_used()
		#if (a.get_id()) == sys.maxsize:
		#if sys.maxsize == a.get_id():
		if sys.maxsize == a.get_id():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		b = 72342787
		a = vertex_dg(b)
		prompt = "	... Test: get_id(), vertex_dg(72342787) 		{}."
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

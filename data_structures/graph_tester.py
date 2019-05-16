#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to test
		the constructors and methods of the graph class,
		which models generic graphs.

	Synopsis:
	Test all constructors and methods of the graph class
		of a generic graph.

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
from data_structures.graph import graph

"""
	Module that tests the methods for accessing and modifying
		vertices of an undirected graph.

	Support for class instantiation is not provided, to avoid
		acquiring a collection of useless "vertex_ug_tester"
		and "vertex_ug" objects.
"""
class graph_tester:
	# =========================================================
	##	Method to test the methods that for accessing and
	#		modifying instance objects of a generic graph.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_graph():
		print("")
		print("==	Testing class: graph.")
		graph_tester.test_constructors_and_equality_comparison()
		graph_tester.test_pairs_of_accessor_mutator_methods()
	# =========================================================
	##	Method to test constructors and equality comparison method
	#		for the graph class.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def test_constructors_and_equality_comparison():
		a = graph()
		prompt = "	... Test default constructor of graph	 		{}."
		statistical_analysis.increment_number_test_cases_used()
		if (a is not None) and (not a.is_self_loop_pseudograph()) and (not a.is_multigraph()) and (not a.is_hypergraph()):
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
		a = graph()
		prompt = "	... Test: is_multigraph()		 		{}."
		statistical_analysis.increment_number_test_cases_used()
		if False == a.is_multigraph():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		flag = True
		a.set_multigraph(flag)
		prompt = "	... Test: set_multigraph(True)			 	{}."
		statistical_analysis.increment_number_test_cases_used()
		if flag == a.is_multigraph():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		flag = False
		a.set_multigraph(flag)
		prompt = "	... Test: set_multigraph(False)			 	{}."
		statistical_analysis.increment_number_test_cases_used()
		if flag == a.is_multigraph():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		# -------------------------------------------------------
		prompt = "	... Test: is_self_loop_pseudograph()		 	{}."
		statistical_analysis.increment_number_test_cases_used()
		if False == a.is_self_loop_pseudograph():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		flag = True
		a.set_self_loop_pseudograph(flag)
		prompt = "	... Test: set_self_loop_pseudograph(True)	 	{}."
		statistical_analysis.increment_number_test_cases_used()
		if flag == a.is_self_loop_pseudograph():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		flag = False
		a.set_self_loop_pseudograph(flag)
		prompt = "	... Test: set_self_loop_pseudograph(False)	 	{}."
		statistical_analysis.increment_number_test_cases_used()
		if flag == a.is_self_loop_pseudograph():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		# -------------------------------------------------------
		a = graph()
		prompt = "	... Test: is_hypergraph()		 		{}."
		statistical_analysis.increment_number_test_cases_used()
		if False == a.is_hypergraph():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		flag = True
		a.set_hypergraph(flag)
		prompt = "	... Test: set_hypergraph(True)			 	{}."
		statistical_analysis.increment_number_test_cases_used()
		if flag == a.is_hypergraph():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))
		flag = False
		a.set_hypergraph(flag)
		prompt = "	... Test: set_hypergraph(False)			 	{}."
		statistical_analysis.increment_number_test_cases_used()
		if flag == a.is_hypergraph():
			print(prompt .format("OK"))
			statistical_analysis.increment_number_test_cases_passed()
		else:
			print(prompt .format("FAIL!!!"))

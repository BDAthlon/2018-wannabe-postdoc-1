#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3 
###!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	#!/usr/bin/python -mtimeit
#	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 ./incremental_test.py ./benchmarks/majority_netlist.json	./output/output-results
#	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3 -mtimeit ./incremental_test.py ./benchmarks/majority_netlist.json	./output/output-results

"""
	This Python script is written by Zhiyang Ong to incrementally
		test features for my software solution for genetic technology
		mapping.


	Synopsis:
	Perform incremental software testing automatically for my
		genetic technology mapping solution.

	This script can be executed as follows:
	./incremental_test.py [input JSON netlist] [output JSON technology mapping]

	Parameters:
	[input JSON netlist]:				A JSON file that contains a structural
											netlist for genetic technology
											mapping.
	[output JSON technology mapping]:	A filename of an output JSON file that
											contains a genetic technology
											mapping for the input structural
											netlist.




	Revision History:
	July 31, 2018			Version 0.1	Script.
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

	pathlib->Path
				For mapping a string to a path.
"""

import sys
import os
import os.path
#from pathlib import Path
from subprocess import call
import time
import warnings
import re



###############################################################
#	Import Custom Python Packages and Modules

# Statistics package.
"""
	Package and module to print statistics of software testing
		results.
"""
from statistics_pkg.test_statistics import statistical_analysis
# Package and module to check the validation of statistical analysis.
from statistics_pkg.test_statistics_tester import statistical_analysis_tester

"""
	Package and module to perform miscellaneous tasks in data
		analysis.
"""
from statistics_pkg.data_analysis_tool import data_analysis
"""
	Package and module to test the miscellaneous tasks in
		analyzing data. 
"""
from statistics_pkg.data_analysis_tool_tester import data_analysis_tester



# Utilities package.
# Package and module to process input arguments to the script/program.
from utilities.queue_ip_arguments import queue_ip_args
# Package and module to validate processing of input arguments.
from utilities.queue_ip_arguments_tester import queue_ip_args_tester
# Package and module to perform file I/O (input/output) operations.
from utilities.file_io import file_io_operations
# Package and module to test file I/O (input/output) operations.
from utilities.file_io_tester import file_io_operations_tester
# Package and module to perform date and time operations.
from utilities.date_time_processing import date_time_operations
# Package and module to test date and time operations.
from utilities.date_time_processing_tester import date_time_operations_tester
"""
	Package and module to configure the software application's
		parameters.
"""
from utilities.configuration_manager import config_manager
"""
	Package and module to test the configuration of the software
		application's parameters.
"""
from utilities.configuration_manager_tester import config_manager_tester
"""
	Module to generate the filename for storing the experimental
		results and simulation output.
"""
from utilities.generate_results_filename import generate_filename
"""
	Module to test if the generated filename (based on the
		then-current time stamp) conforms to the specified
		format.
"""
from utilities.generate_results_filename_tester import generate_filename_tester
# Module to test miscellaneous methods.
from utilities.miscellaneous import misc
from utilities.miscellaneous_tester import misc_tester
# Module for user-defined error/exception.
#import utilities.custom_exceptions.graph_error
from utilities.custom_exceptions.graph_error import *
# Module to test user-defined errors/exceptions.
#import utilities.custom_exceptions.graph_error_tester as graph_err_t
from utilities.custom_exceptions.graph_error_tester import *
"""
	Module with methods to calculate the factorial of numbers,
		used to test modules for current timing measurements.
	
	This is because the methods to get current time measurements
		use these get_factorial() methods.
"""
from utilities.timing_measurements.get_factorial import calculate_factorial
# Modules to perform timing measurements.
from utilities.timing_measurements.performance_measurement import execution_time_measurement
from utilities.timing_measurements.performance_measurement_no_ns import execution_time_measurement_no_ns
"""
	Modules to test methods to:
	+ determine factorials, via iteration and recursion.
	+ perform current timing/time measurements.
"""
from utilities.timing_measurements.get_factorial_tester import calculate_factorial_tester
from utilities.timing_measurements.performance_measurement_no_ns_tester import execution_time_measurement_no_ns_tester 
from utilities.timing_measurements.performance_measurement_tester import execution_time_measurement_tester
"""
	Module to perform operations regarding basic data types and numbers.
	Test module for the aforementioned module.
"""
from utilities.data_types_and_numbers.data_type_and_number_operations import data_type_n_number_ops
from utilities.data_types_and_numbers.data_type_and_number_operations_tester import data_type_n_number_ops_tester






# Package of parsers.
# Module to transform JSON objects to Python objects.
from parsers.json_object import json_obj
from parsers.json_object_tester import json_obj_tester
# Module to parse JSON configuration files.
from parsers.config_file_parser import config_parser
from parsers.config_file_parser_tester import config_parser_tester

# Package for data structures.
# Module to model the vertex of a generic graph.
from data_structures.vertex import vertex
# Module to test the vertex of a generic graph.
from data_structures.vertex_tester import vertex_tester
# Module to model a generic graph.
from data_structures.graph import graph
# Module to test a generic graph.
from data_structures.graph_tester import graph_tester
# Module to model the vertex of a directed graph.
from data_structures.directed_graph.vertex_dg import *
# Module to test the vertex of a directed graph.
from data_structures.directed_graph.vertex_dg_tester import *
# Module to model the vertex of an undirected graph.
from data_structures.undirected_graph.vertex_ug import *
# Module to test the vertex of an undirected graph.
from data_structures.undirected_graph.vertex_ug_tester import *
# Module to model the edge of an undirected graph.
from data_structures.undirected_graph.edge_ug import *
# Module to test the edge of an undirected graph.
from data_structures.undirected_graph.edge_ug_tester import *

###############################################################

# Global variables.
#	Location to store simulation and/or experimental results.
#result_repository = "/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"


###############################################################
"""
	Module with methods that incrementally test features for my software
		solution for genetic technology mapping.
	It tests the following:
	+ Test the verification code for checking if the input arguments are valid.
	+ Check if the file I/O module functions correctly.
	+ Check if the output JSON file generator works correctly.
	+ Test the implementations for genetic technology mapping.
		- Brute force algorithm
"""
class incremental_test_automation:
	# (Static) variables.
	# List of BibTeX keys
	set_of_BibTeX_keys = []
	num_of_bibtex_entries = 0
	#	Location to store simulation and/or experimental results.
	result_repository = "~/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
	# ============================================================
	#	Other methods.
	# ============================================================
	##	Method to add BibTeX keys into a list, "set_of_BibTeX_keys".
	#	@return ???
	#	O(n) method, where n is the number of BibTeX keys.
	@staticmethod
	def add_BibTeX_key(found_BibTeX_key):
		if (found_BibTeX_key in incremental_test_automation.set_of_BibTeX_keys):
			temp_str = "Duplicate BibTeX key:"+found_BibTeX_key
			warnings.warn(temp_str)
			raise Exception("Multiple instances of a BibTeX key")
		incremental_test_automation.set_of_BibTeX_keys.append(found_BibTeX_key)
	# ============================================================
	##	Method to sort BibTeX keys into a list, "set_of_BibTeX_keys".
	#	O(n*log(n)) method, where n is the number of BibTeX keys.
	@staticmethod
	def sort_BibTeX_keys():
		incremental_test_automation.set_of_BibTeX_keys = sorted(incremental_test_automation.set_of_BibTeX_keys)
	# ============================================================
	##	Method to read each line of the input BibTeX file.
	#	O(n) method, where n is the number of lines of the BibTeX file.
	@staticmethod
	def read_input_BibTeX_file(ip_file_object,input_BibTeX_file):
		#print "--------------------------------------------------------"
		println = "=	Reading input BibTeX file: "
		println += input_BibTeX_file
		print(println)
		# Read each available line in the input BibTeX file.
		for line in ip_file_object:
			# Is this line the 1st line of a BibTeX entry?
			if "@" == line[0]:
				# Yes.
#				print "...	First line of a BibTeX entry."
				# Increment number of BibTeX entries.
				incremental_test_automation.num_of_bibtex_entries = incremental_test_automation.num_of_bibtex_entries + 1
				tokenized_BibTeX_entry = re.split('@|{|,',line)
#				for i in tokenized_BibTeX_entry:
#					print i
				# Is the type of the BibTeX entry valid?
				if (tokenized_BibTeX_entry[1] in queue_ip_args.BibTeX_entry_types):
					# Yes. Try adding the BibTeX entry to "set_of_BibTeX_keys".
					incremental_test_automation.add_BibTeX_key(tokenized_BibTeX_entry[2].lower())
				else:
					# No. Warn user that the type of BibTeX entry is invalid!
					temp_str = "Invalid type of BibTeX entry:"
					temp_str += tokenized_BibTeX_entry[1]
					print(temp_str)
					#warnings.warn("Invalid type of BibTeX entry")
					raise Exception("BibTeX entry has an invalid type!")
		if (incremental_test_automation.num_of_bibtex_entries != len(incremental_test_automation.set_of_BibTeX_keys)):
			raise Exception("Mismatch in number of BibTeX entries processed.")
		else:
			print("=	Number of BibTeX entries processed: {}" .format(str(incremental_test_automation.num_of_bibtex_entries)))











###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	"""
		Print results of automated regresstion testing to
			output file.
	
		File object for output file containing automated regression
			software testing results.
	"""
	regression_results_f_obj = file_io_operations.open_file_object_write_results(file_io_operations.regression_testing_results_location, file_io_operations.regression_testing_results_suffix)
	#regression_results_f_obj = file_io_operations.open_file_object_write_results(file_io_operations.regression_testing_results_location, file_io_operations.regression_testing_results_suffix)
	
	"""
	# Redirect standard output and standard error to an output file.
	results_file_object = file_io_operations.open_file_object_write_results()
	file_io_operations.redirect_std_op_to_file_obj(results_file_object)
	file_io_operations.redirect_std_err_to_file_obj(results_file_object)
	"""
	regression_results_f_obj.write("==================================================")
	regression_results_f_obj.write("Automating incremental regression testing of my software")
	regression_results_f_obj.write("	solution for genetic technology mapping.")
	regression_results_f_obj.write("")
	# Assign input arguments to "queue_ip_args" for processing.
	#queue_ip_args.set_input_arguments(sys.argv,queue_ip_args.INCREMENTAL_TEST)
	queue_ip_args.set_input_arguments(sys.argv)
	# Check if user wants to read the brief user manual.
	queue_ip_args.check_if_help_wanted()
	# Process the first input argument.
	regression_results_f_obj.write("=	Process the first input argument.")
	ip_filename = queue_ip_args.process_1st_ip_arg()
	regression_results_f_obj.write("=	Create a file object for reading.")
	# Create a file object for input BibTeX file, in reading mode.
	ip_file_obj = file_io_operations.open_file_object_read(ip_filename)
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	# The real stuff begins here...
	regression_results_f_obj.write("-	-	-	-	-	-	-	-	-	-	-	-	-")
	regression_results_f_obj.write("=	Testing the statistical analysis package.")
	# Insert test cases for statistical analysis package
	statistical_analysis_tester.test_statistical_analysis(regression_results_f_obj)
	# Test module performing operations on basic data types & numbers.
	data_type_n_number_ops_tester.test_data_type_n_number_ops(regression_results_f_obj)
	# Test the miscellaneous tasks in analyzing data.
	data_analysis_tester.test_data_analysis()
	regression_results_f_obj.write("")
	regression_results_f_obj.write("-	-	-	-	-	-	-	-	-	-	-	-	-")
	# Insert test cases for testing the utilities package.
	regression_results_f_obj.write("")
	regression_results_f_obj.write("=	Testing the utilities package.")
	"""
		Test the get_factorial() methods first, so that I can
			test methods to get current time measurements
			that/which use these get_factorial() methods.
	"""
	calculate_factorial_tester.test_get_factorial_methods()
	execution_time_measurement_no_ns_tester.test_current_time_measurement_methods()
	execution_time_measurement_tester.test_current_time_measurement_methods()
	file_io_operations_tester.test_file_io_operations()
	queue_ip_args_tester.test_queue_ip_args()
	config_manager_tester.test_configure_sw_application_parameters()
	date_time_operations_tester.test_date_time_operations()
	generate_filename_tester.test_filename_generation_methods()
	misc_tester.test_miscellaneous_methods()
	# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	regression_results_f_obj.write("")
	regression_results_f_obj.write("=	Testing user-defined errors.")
	regression_results_f_obj.write("")
	graph_error_tester.test_raising_graph_error()
	#utilities.custom_exceptions.graph_error_tester.test_raising_graph_error()
	#utilities.custom_exceptions.graph_error_tester.helloworld()
	#utilities.custom_exceptions.graph_error_tester.graph_error_tester.helloworld()
	#utilities.custom_exceptions.graph_error_tester.graph_error_tester.test_raising_graph_error()
	#graph_err_t.test_raising_graph_error()
#	check_bibtex_key_tester.test_check_bibtex_key()
	regression_results_f_obj.write("-	-	-	-	-	-	-	-	-	-	-	-	-")
	# Insert test cases for testing the parsers package.
	regression_results_f_obj.write("")
	regression_results_f_obj.write("=	Testing the parsers package.")
	regression_results_f_obj.write("")
	json_obj_tester.test_json_object_accessibility()
	config_parser_tester.test_json_config_file_parser()
	regression_results_f_obj.write("-	-	-	-	-	-	-	-	-	-	-	-	-")
	# Insert test cases for testing the data_structures package.
	regression_results_f_obj.write("")
	regression_results_f_obj.write("=	Testing the data_structures package.")
	regression_results_f_obj.write("")
	vertex_tester.test_generic_vertex()
	graph_tester.test_graph()
	vertex_dg_tester.test_vertex_dg()
	vertex_ug_tester.test_vertex_ug()
#	edge_ug_tester.test_edge_ug()
	regression_results_f_obj.write("-	-	-	-	-	-	-	-	-	-	-	-	-")
	#	### TO-DO
	#	Test expr_configuration
#	incremental_test_automation.read_input_BibTeX_file(ip_file_obj,ip_filename)
	msg = "=================================================="
	regression_results_f_obj.write(msg)
	print(msg)
	msg = ">>	Get statistics of the software testing process."
	regression_results_f_obj.write(msg)
	print(msg)
	statistical_analysis.print_statistics_of_software_testing(regression_results_f_obj)
	# Close the file object for reading.
	regression_results_f_obj.write("=	Close the file objects for reading (and writing).")
	file_io_operations.close_file_object(ip_file_obj)
	file_io_operations.close_file_object(regression_results_f_obj)
	"""
	file_io_operations.close_file_object(results_file_object)
	# Stop redirecting standard output and standard to an output file.
	file_io_operations.stop_redirecting_std_op()
	file_io_operations.stop_redirecting_std_err()
	"""
#	regression_results_f_obj.write("<<	I can see this in standard output, printed in the Terminal.")
	if misc.add_commit_push_updates_to_git_repository("Update build: Added access to Git repository"):
		regression_results_f_obj.write("Update repository of simulation/experimental results.")
	else:
		regression_results_f_obj.write("DID NOT update repository of simulation/experimental results.")

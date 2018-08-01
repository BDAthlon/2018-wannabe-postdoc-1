#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	#!/usr/bin/python -mtimeit


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

"""
	Package and module to print statistics of software testing
		results.
"""
from statistics.test_statistics import statistical_analysis
# Package and module to check the validation of statistical analysis.
from statistics.test_statistics_tester import statistical_analysis_tester
# Package and module to process input arguments to the script/program.
from utilities.queue_ip_arguments import queue_ip_args
# Package and module to validate processing of input arguments.
from utilities.queue_ip_arguments_tester import queue_ip_args_tester
# Package and module to perform file I/O (input/output) operations.
from utilities.file_io import file_io_operations


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
class Incremental_Test_Automation:
	# List of BibTeX keys
	set_of_BibTeX_keys = []
	num_of_bibtex_entries = 0
	# ============================================================
	#	Other methods.
	# ============================================================
	##	Method to add BibTeX keys into a list, "set_of_BibTeX_keys".
	#	O(n) method, where n is the number of BibTeX keys.
	@staticmethod
	def add_BibTeX_key(found_BibTeX_key):
		if (found_BibTeX_key in Incremental_Test_Automation.set_of_BibTeX_keys):
			temp_str = "Duplicate BibTeX key:"+found_BibTeX_key
			warnings.warn(temp_str)
			raise Exception("Multiple instances of a BibTeX key")
		Incremental_Test_Automation.set_of_BibTeX_keys.append(found_BibTeX_key)
	# ============================================================
	##	Method to sort BibTeX keys into a list, "set_of_BibTeX_keys".
	#	O(n*log(n)) method, where n is the number of BibTeX keys.
	@staticmethod
	def sort_BibTeX_keys():
		Incremental_Test_Automation.set_of_BibTeX_keys = sorted(Incremental_Test_Automation.set_of_BibTeX_keys)
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
				Incremental_Test_Automation.num_of_bibtex_entries = Incremental_Test_Automation.num_of_bibtex_entries + 1
				tokenized_BibTeX_entry = re.split('@|{|,',line)
#				for i in tokenized_BibTeX_entry:
#					print i
				# Is the type of the BibTeX entry valid?
				if (tokenized_BibTeX_entry[1] in queue_ip_args.BibTeX_entry_types):
					# Yes. Try adding the BibTeX entry to "set_of_BibTeX_keys".
					Incremental_Test_Automation.add_BibTeX_key(tokenized_BibTeX_entry[2].lower())
				else:
					# No. Warn user that the type of BibTeX entry is invalid!
					temp_str = "Invalid type of BibTeX entry:"
					temp_str += tokenized_BibTeX_entry[1]
					print(temp_str)
					#warnings.warn("Invalid type of BibTeX entry")
					raise Exception("BibTeX entry has an invalid type!")
		if (Incremental_Test_Automation.num_of_bibtex_entries != len(Incremental_Test_Automation.set_of_BibTeX_keys)):
			raise Exception("Mismatch in number of BibTeX entries processed.")
		else:
			print("=	Number of BibTeX entries processed: {}" .format(str(Incremental_Test_Automation.num_of_bibtex_entries)))











###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	print("==================================================")
	print("Automating incremental regression testing of my software")
	print("	solution for genetic technology mapping.")
	print("")
	# Assign input arguments to "queue_ip_args" for processing.
	queue_ip_args.set_input_arguments(sys.argv,queue_ip_args.INCREMENTAL_TEST)
	# Check if user wants to read the brief user manual.
	queue_ip_args.check_if_help_wanted()
	# Process the first input argument.
	print("=	Process the first input argument.")
	ip_filename = queue_ip_args.process_1st_ip_arg()
	# Create a file object for reading.
	print("=	Create a file object for reading.")
	# Create a file object for input BibTeX file, in reading mode.
	ip_file_obj = file_io_operations.open_file_object_read(ip_filename)
	# The real stuff begins here...
	statistical_analysis_tester.test_statistical_analysis()
	#	### TO-DO
	# Insert test cases for testing the utilities package.
	print("-	-	-	-	-	-	-	-	-	-	-	-	-")
#	check_bibtex_key_tester.test_check_bibtex_key()
	queue_ip_args_tester.test_queue_ip_args()
	print("-	-	-	-	-	-	-	-	-	-	-	-	-")
#	Incremental_Test_Automation.read_input_BibTeX_file(ip_file_obj,ip_filename)
	print("!	!	!	!	!	!	!	!	!	!	!")
	print(">>	Get statistics of the software testing process.")
	statistical_analysis.print_statistics_of_software_testing()
	# Close the file object for reading.
	print("=	Close the file object for reading.")
	file_io_operations.close_file_object(ip_file_obj)
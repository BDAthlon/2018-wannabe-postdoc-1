#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to parse a
		JSON-based "parameters.config" (or "configuration.json") file.

	Notes/Assumptions:
	The "configuration.json" is parsed by the "config_file_parser.py",
		and its fields are mapped from a JSON object into a Python object
		represented by "json_object.py".
	In this parsing process, it sets the field(s) in the Python module/class
		in "configuration_manager.py".

		JSON (JavaScript Object Notation) is a subset of YAML
			(YAML Ain't Markup Language) \cite{WikipediaContributors2018o}.
		Hence, JSON is simpler to parse than YAML.
		Also, since XML (Extensible Markup Language)
			\cite{WikipediaContributors2018n} is more complex
			to parse than JSON \cite{Desai2015}, I am going to
			use the JSON format to represent data that is used
			to configure the parameters of the software application.
		However, JSON cannot contain comments \cite{WikipediaContributors2018p},
			while YAML \cite{WikipediaContributors2018o} and
			XML \cite{WikipediaContributors2018n} can.
		Hence, I am trading off annotations in the configuration
			file(s) for simplicity to parse such files when I
			choose JSON as my data exchange format.
		That said, if I select appropriate names for different
			nested dictionaries in the JSON file, I do not need
			to use comments.

	References:
	Citations/References that use the LaTeX/BibTeX notation are taken
		from my BibTeX database (set of BibTeX entries).

	[DrakeJr2016b]
		Section 11 File and Directory Access, Subsection 11.2 os.path - Common pathname manipulations


"""

#	The MIT License (MIT)

#	Copyright (c) <2014> <Zhiyang Ong>

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
	Package and module to configure the software application's
		parameters.
"""
from utilities.configuration_manager import config_manager
# Package and module to perform file I/O operations.
from utilities.file_io import file_io_operations
# Package and module to transform JSON objects to Python objects.
from parsers.json_object import json_obj


###############################################################
"""
	Module to parse a JSON-based "parameters.config" (or
		"configuration.json") file.
"""
class config_parser:
	"""
		Name of configuration file that would be parsed.
		It configures the parameters of this Python program.
	"""
	name_of_configuration_file = "configuration.json"
	"""
		A dictionary a set of name–value pairs, which are also
			known as key–value pairs, field–value pairs, or
			attribute–value pairs \cite{WikipediaContributors2018q}.
		Use a dictionary, which is a mapping built-in type in Python
			to store data fields and their values, to store
			a set of dictionaries, a list of dictionaries, and
			dictionaries of dictionaries, and other nested
			dictionaries.
		This is because JSON files contain dictionaries and
			nested dictionaries.
		For a default value, set this to an empty dictionary.
	"""
	temp_dictionary = dict()
	#
	# ============================================================
	##	Method to parse the "configuration.json" file.
	#	@param - None.
	#	@return boolean TRUE, if the location of the directory to
	#		store simulation/experimental results has been
	#		set/configured by the "configuration.json" file.
	#		Else, return boolean FALSE.
	#	O(n) method, where n is the number of fields in the
	#		"configuration.json" file.
	@staticmethod
	def parse_configuration_file():
		"""
			File object associated with reading the configuration
				file that parameterizes this software.
		"""
		config_file_obj = file_io_operations.open_file_object_read(config_parser.name_of_configuration_file)
		#print("	... Created file object: config_file_obj.")
		temp_dictionary = json_obj(config_file_obj)
		#print("temp_dictionary:=",temp_dictionary,"=")
		#print("temp_dictionary.__list__=",temp_dictionary.__list__,"=")
		"""
			A 'json_obj' object with the ".__list__" suffix is
				subscriptable.
			Hence, I can use the name of a field in the JSON object
				to access the value of that field.
		"""
		#print("temp_dictionary.__list__['result_repository']=",temp_dictionary.__list__["result_repository"],"=")
		"""
			The temp_dictionary is not subscriptable, since 'json_obj'
				objects are not subscriptable.
			Hence, the following sentence is not valid.
		"""
		#print("temp_dictionary['result_repository']=",temp_dictionary["result_repository"],"=")
		#if config_manager.set_result_repository(temp_dictionary.__list__["output"]):
		if config_manager.set_result_repository(temp_dictionary.__list__["result_repository"]):
			return True
		else:
			return False

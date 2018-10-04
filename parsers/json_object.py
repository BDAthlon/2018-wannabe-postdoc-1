#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to contain (nested)
		dictionaries of a JSON-based "parameters.config" (or
		"configuration.json") file.

	Notes/Assumptions:
	The "configuration.json" is parsed by the "config_file_parser.py",
		and its fields are mapped from a JSON object into a Python object
		represented by "json_object.py".
	In this parsing process, it sets the field(s) in this Python module/class.

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
	json		For parsing JSON files and processing JSON-based data.
"""

import sys
import os
import os.path
from subprocess import call
import time
import warnings
import re
import filecmp
import json


###############################################################
#	Import Custom Python Modules


###############################################################
"""
	Module to contain (nested) dictionaries of a JSON object in
		JavaScript into a Python object.
"""
class json_obj:
	"""
		Standard constructor that requires a file object associated
			with opening a JSON file for read operations.
	"""
	def __init__(self, file_object):
		#self.__dict__ = json.load(file_object)
		self.__list__ = json.load(file_object)

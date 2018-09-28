#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python

"""
	This Python script is written by Zhiyang Ong to parse a
		JSON-based "parameters.config" (or "configuration.json") file.

	Notes/Assumptions:
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

###############################################################
"""
	Module to parse a JSON-based "parameters.config" (or
		"configuration.json") file.
"""
class config_manager:
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
	"""
	temp_dictionary = dict()

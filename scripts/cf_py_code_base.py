#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to compare my
		Python boilerplate codebase with it copies in other
		Python repositories.


	Synopsis:
	For each copy of my Python boilerplate codebase,
		compare their subdirectories and files.

	This script can be executed as follows:
	./cf_py_code_base.py

	Parameters:
	[None.]




	Revision History:
	January 15, 2019			Version 0.1	Script.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'January 15, 2019'

#	The MIT License (MIT)

#	Copyright (c) <2019> <Zhiyang Ong>

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




###############################################################
# Main method for the program.

#	If this is executed as a Python script,
if __name__ == "__main__":
	# This is the relative path to my Python boilerplate codebase.
	dir_py_boilerplate_code_base = "~/Documents/progetti/bda/2018-wannabe-postdoc-1"
	"""
		This is a list of Python repositories that include copies
			of my Python boilerplate codebase.
		Each copy is a subset of my Python boilerplate codebase.
		For each repository, its relative path to the its
			corresponding directory is indicated.
		Separate each copy (of the type "string") by a comma.
	"""
	list_copies_of_py_repositories = ["~/Documents/ricerca/gulyas-scripts/std_cell_library/std_cells"]
	#	--------------------------------------------------------
	"""
	test_list_copies_of_py_repositories = ["~/Documents/ricerca/gulyas-scripts/std_cell_library/std_cells", "~/Documents/ricerca/gulyas-scripts/gelato", "~/Documents/ricerca/gulyas-scripts/barfi"]
	for index, path_of_directory in enumerate(test_list_copies_of_py_repositories):
		print(index+1, path_of_directory)

	If I used the following, the word "Output" would appear before
		printing each element in the list with the corresponding index.
	for index, path_of_directory in enumerate(test_list_copies_of_py_repositories,1):
	"""
	#	--------------------------------------------------------
	# For each copy of my Python boilerplate codebase,
	for index, path_of_directory in enumerate(list_copies_of_py_repositories):

		"""
			Print the number of enumerated repositories/directories,
				and the path of currently enumerated repository/directory.

			Note that the following:
				number of enumerated repositories/directories = index + 1.
		"""
		print(index+1, path_of_directory)
		# For each subdirectory of currently enumerated repository/directory,
		"""
			Compare it with the corresponding subdirectory
				in my Python boilerplate codebase.
		"""
"""
	Python boilerplate codebase with it copies in other
	Python repositories.
"""

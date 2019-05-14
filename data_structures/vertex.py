#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This Python script is written by Zhiyang Ong to model a vertex/node
		of a generic (mathematical) graph/network.

	References:
	Citations/References that use the LaTeX/BibTeX notation are taken
		from my BibTeX database (set of BibTeX entries).

	\cite[\S14.2,\S14.2.3]{Goodrich2013} is the primary source of reference
		about adjacency map.

	From \cite[\S14.2,pp.627]{Goodrich2013}:
		"In an adjacency list, we maintain, for each vertex, a separate list containing those edges that are incident to the vertex. The complete set of edges can be determined by taking the union of the smaller sets, while the organization allows us to more efficiently find all edges incident to a given vertex."
		"An adjacency map is very similar to an adjacency list, but the secondary container of all edges incident to a vertex is organized as a map, rather than as a list, with the adjacent vertex serving as a key. This allows for access to a specific edge (u,v) in O(1) expected time."

	The attributes/properties/fields and methods of the vertex class are primarily described in my LaTeX report about data structures and algorithms (see https://github.com/eda-ricercatore/boilerplate-code/tree/master/notes/report), including a typeset PDF copy of the report (https://github.com/eda-ricercatore/boilerplate-code/blob/master/notes/report/data-structures_n_algor.pdf).

	\cite{keyser2015} for the value of the largest integer (sys.maxsize)
		and the largest floats, float("inf") and float("-inf"), in Python.

	Revision History:
	August 1, 2018			Version 0.1, initial build.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'August 1, 2018'

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


###############################################################
#	Module with accessor and mutator method(s) for its attributes.
class vertex:
	# Properties of the vertex_dg objects.
	# Unique ID of the instance object.
	#	No other instance object of vertex shares this ID.
	id = "Unknown ID of this vertex."
	# ============================================================

	# Default constructor of a vertex.
	def __init__(self):
		self.id = sys.maxsize
		#self.id = float("inf")
		#self.id  = -9999999999999999

	"""
		Standard constructor of a vertex.

		The following line requires an ID ("initialized_id") to
			be passed in to the standard constructor.
		def __init__(self, initialized_id):

		Assigning "initialized_id" to sys.maxsize in the standard
			constructor makes the input argument "initialized_id"
			optional.
	"""
	def __init__(self, initialized_id = sys.maxsize):
		self.id = initialized_id

	# ============================================================

	# Overriding methods... Override the default implementation.

	# Comparison of two vertex objects.
	def __eq__(self, other):
		if isinstance(other, vertex):
			return self.id == other.id
		return False

	# ============================================================

	#	Accessor methods of the vertex class.

	##	Method to access the ID of a vertex instance object.
	#	@param - None.
	#	@return the ID belonging to the vertex instance object.
	#	O(1) .
	def get_id(self):
		return self.id

	# ------------------------------------------------------------

	#	Mutator methods of the vertex class.

	##	Method to set the ID of a vertex instance object as
	#		"identity".
	#	@param identity - The new/replacement ID of the vertex
	#		instance object.
	#	@return the ID belonging to the vertex instance object.
	#	O(1) .
	def set_id(self, identity):
		self.id = identity

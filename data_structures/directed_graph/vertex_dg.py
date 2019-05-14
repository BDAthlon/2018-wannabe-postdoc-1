#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This Python script is written by Zhiyang Ong to model a vertex/node
		of a directed graph.



	Notes/Assumptions:
	A vertex_dg object can share the same list of outgoing edges and
		incoming edges as another vertex_dg object, and be different/unique
		vertex_dg objects as long as their IDs are different/unique.



	References:
	Citations/References that use the LaTeX/BibTeX notation are taken
		from my BibTeX database (set of BibTeX entries).

	\cite[\S14.2,\S14.2.3]{Goodrich2013} is the primary source of reference
		about adjacency map.

	From \cite[\S14.2,pp.627]{Goodrich2013}:
		"In an adjacency list, we maintain, for each vertex, a separate list containing those edges that are incident to the vertex. The complete set of edges can be determined by taking the union of the smaller sets, while the organization allows us to more efficiently find all edges incident to a given vertex."
		"An adjacency map is very similar to an adjacency list, but the secondary container of all edges incident to a vertex is organized as a map, rather than as a list, with the adjacent vertex serving as a key. This allows for access to a specific edge (u,v) in O(1) expected time."

	[DrakeJr2016b]
		Section 11 File and Directory Access, Subsection 11.2 os.path - Common pathname manipulations

	\cite[\S2.3.3]{Ong2017} provides a list of methods that shall be
		implemented.

#### TO BE COMPLETED

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
# Package and module to representing the vertex class of the graph.
from data_structures.vertex import vertex


###############################################################
#	Module with attributes and methods to model a vertex in a
#		directed graph.
class vertex_dg(vertex):
	# Properties of the vertex_dg objects.
	# Unique ID of the instance object.
	#	No other instance object of vertex shares this ID.
	id = "Unknown ID of this vertex."
	# List of outgoing edges.
	list_outgoing_edges = []
	# List of incoming edges.
	list_incoming_edges = []
	"""
		Override the constructor of the parent/super class.
		Accepts a list of outgoing edges and a list of incoming
			edges as input parameters of the standard constructor.
		Assign the input parameters to values/"None" by default,
			so that these input parameters would be optional.
	"""
	def __init__(self, initialized_id = sys.maxsize, outgoing_edges = None, incoming_edges = None):
		if initialized_id is None:
			initialized_id = sys.maxsize
		self.id = initialized_id
		self.list_outgoing_edges = outgoing_edges
		self.list_incoming_edges = incoming_edges

	# ============================================================

	# Overriding methods... Override the default implementation.

	# Comparison of two vertex objects.
	def __eq__(self, other):
		if isinstance(other, vertex_dg):
			return (self.id == other.id) and (self.list_outgoing_edges == other.list_outgoing_edges) and (self.list_incoming_edges == other.list_incoming_edges)
		return False

	# ============================================================

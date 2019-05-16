#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to model a vertex/node
		of an undirected graph.



	#### IMPORTANT NOTES:
	A vertex_ug object can share the same dictionaries of outgoing edges and
		incoming edges as another vertex_ug object, and be different/unique
		vertex_ug objects as long as their IDs are different/unique.

	Only hashable/"mutable" objects can have a hash key, and be used with
		sets and dictionaries.
	Hence, objects of the vertex_ug class and its child/derivative classes
		cannot be hased, since Python does not provide a default hash
		function for these classes.
	However, by overriding the __hash__() function, I can make the
		objects of the vertex_ug class and its child/derivative classes
		hashable.


	References:
	Citations/References that use the LaTeX/BibTeX notation are taken
		from my BibTeX database (set of BibTeX entries).

	\cite[\S14.2,\S14.2.3]{Goodrich2013} is the primary source of reference
		about adjacency map.
		Note that in \cite[\S14.2,\S14.2.3]{Goodrich2013}, map is used
			synonymously/interchangeably with dictionary and asssociative
			arrays \cite[\S10.1]{Goodrich2013}.
		Specifically, in \cite[\S10.1]{Goodrich2013}, dictionary refers
			to Python's "dict" class, and map refers to the abstract
			data type of dictionaries.
		Note that the map(function f, list of inputs) function applies
			the function f to the list of inputs;
			f and the list of inputs are passed as input parameters to
				the map() function.
		Hence, do not confuse dictionaries/maps with the map() function.


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
#	Module with attributes and methods to model a vertex in an
#		undirected graph.
class vertex_ug(vertex):
	# Properties of the vertex_ug objects.
	# Unique ID of the instance object.
	#	No other instance object of vertex shares this ID.
	id = "Unknown ID of this vertex."
	# A dictionary of adjacent edges.
	dict_adjacent_edges = {}
	"""
		Override the constructor of the parent/super class.
		Accepts a dictionary of outgoing edges and a dictionary of
			incoming edges as input parameters of the standard
			constructor.
		Assign the input parameters to values/"None" by default,
			so that these input parameters would be optional.
	"""
	def __init__(self, initialized_id = sys.maxsize, adjacent_edges = {}):
		if initialized_id is None:
			initialized_id = sys.maxsize
		self.id = initialized_id
		self.dict_adjacent_edges = adjacent_edges

	# ============================================================

	# Overriding methods... Override the default implementation.

	# Comparison of two vertex objects.
	def __eq__(self, other):
		if isinstance(other, vertex_ug):
			"""
			print("self.id:::",self.id,"=")
			print("other.id:::",other.id,"=")
			print("self.dict_outgoing_edges:::",self.dict_outgoing_edges,"=")
			print("other.dict_outgoing_edges:::",other.dict_outgoing_edges,"=")
			print("self.dict_incoming_edges:::",self.dict_incoming_edges,"=")
			print("other.dict_incoming_edges:::",other.dict_incoming_edges,"=")
			"""
			return (self.id == other.id) and (self.dict_adjacent_edges == other.dict_adjacent_edges)
		return False

	# Hashing the unhashable/immutable vertex_ug
	def __hash__(self):
		#return hash(tuple(self))
		return hash(self.id)

	# ============================================================

	#	Accessor methods of the vertex class.

	##	Method to access the ID of a vertex instance object.
	#	@param - None.
	#	@return the ID belonging to the vertex instance object.
	#	O(1).
	def get_id(self):
		return self.id

	# ------------------------------------------------------------

	#	Mutator methods of the vertex class.

	##	Method to set the ID of a vertex instance object as
	#		"identity".
	#	@param identity - The new/replacement ID of the vertex
	#		instance object.
	#	@return the ID belonging to the vertex instance object.
	#	O(1).
	

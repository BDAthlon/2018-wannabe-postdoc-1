#!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to model a generic
		graph.



	#### IMPORTANT NOTES:
	Properties of graphs and their suggested references:
	+ multigraphs \cite{Wallis2012}
	+ hypergraphs \cite{Bretto2013,Cong2003a,Alpert1996,Berge1989,Johnson2013b}


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



###############################################################
#	Module with attributes and methods to model a generic graph.
class graph:
	# Properties of graph objects.
	# Flag to indicate if the graph is a multigraph
	multigraph = False
	# Flag to indicate if the graph can contain self-loops.
	self_loop_pseudograph = False
	# Flag to indicate if the graph is a hypergraph
	hypergraph = False

	# ============================================================

	# Default constructor: Overridden???

	# ============================================================

	# Overriding methods... Override the default implementation.

	# Comparison of two graph objects.
	def __eq__(self, other):
		"""
			Compare each attribute/property of the graph objects:
				self (current graph object) and the other graph
				object of interest.
		"""
		if isinstance(other, graph):
			return (self.multigraph == other.multigraph) and (self.self_loop_pseudograph == other.self_loop_pseudograph) and (self.hypergraph == other.hypergraph)
		else:
			return False

	# ============================================================

	#	Accessor methods of the graph class.

	##	Method to determine if this graph object is a multigraph.
	#	@param - None.
	#	@return the boolean value of the multigraph attribute.
	#	O(1).
	def is_multigraph(self):
		return self.multigraph
	# ============================================================
	##	Method to determine if this graph object can have self-loops.
	#	@param - None.
	#	@return the boolean value of the self_loop_pseudograph
	#		attribute.
	#	O(1).
	def is_self_loop_pseudograph(self):
		return self.self_loop_pseudograph
	# ============================================================
	##	Method to determine if this graph object is a hypergraph.
	#	@param - None.
	#	@return the boolean value of the hypergraph attribute.
	#	O(1).
	def is_hypergraph(self):
		return self.hypergraph

	# ============================================================

	#	Mutator methods of the graph class.

	##	Method to set the multigraph attribute of a graph instance
	#		object to a particular boolean value.
	#	@param flag - The new boolean value of the multigraph
	#		attribute.
	#	@return Nothing.
	#	O(1).
	def set_multigraph(self, flag):
		self.multigraph = flag
	# =========================================================
	##	Method to set the self_loop_pseudograph attribute of a
	#		graph instance object to a particular boolean value.
	#	@param flag - The new boolean value of the self_loop_pseudograph
	#		attribute.
	#	@return Nothing.
	#	O(1).
	def set_self_loop_pseudograph(self, flag):
		self.self_loop_pseudograph = flag
	# =========================================================
	##	Method to set the hypergraph attribute of a graph instance
	#		object to a particular boolean value.
	#	@param flag - The new boolean value of the hypergraph
	#		attribute.
	#	@return Nothing.
	#	O(1).
	def set_hypergraph(self, flag):
		self.hypergraph = flag

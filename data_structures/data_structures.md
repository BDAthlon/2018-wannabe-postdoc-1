#	Notes About Data Structures and Algorithms

See my *LaTeX* report about [data structures and algorithms](https://github.com/eda-ricercatore/boilerplate-code/tree/master/notes/report), including a typeset [PDF copy of the report](https://github.com/eda-ricercatore/boilerplate-code/blob/master/notes/report/data-structures_n_algor.pdf).

##	To-Do List

+ [ ] Implement a generic graph.
	- [ ] Implement *vertex class.
	- [ ] Test *vertex class.
	- [x] Implement *edge* class.
		* Ignored, because it is hard to find similarities between edges of directed and undirected graphs.
	- [x] Test *edge* class.
	- [ ] Implement *graph* class.
	- [ ] Test *graph* class.
+ [ ] Implement an undirected graph, which extends a generic graph.
	- [ ] Implement vertex_ug class.
	- [ ] Test vertex_ug class.
	- [ ] Implement edge_ug class.
	- [ ] Test edge_ug class.
	- [ ] Implement graph_ug class.
	- [ ] Test graph_ug class.
+ [ ] Implement a directed graph, which extends a generic graph.
	- [ ] Implement vertex_dg class.
	- [ ] Test vertex_dg class.
	- [ ] Implement edge_dg class.
	- [ ] Test edge_dg class.
	- [ ] Implement graph_dg class.
	- [ ] Test graph_dg class.

For each class, implement the following:
	- Constructor:
		* Default constructor.
		* Standard constructor(s) (if any).
	- Attributes/Properties/Fields.
	- Accessor methods for its attributes.
	- Mutator methods for its attributes.
	- Other methods.
	- Test each constructor.
	- Test each method.

##	Notes (and Assumptions)

###	Graph Implementations With Other Data Structures

As noted in \cite[\S2.3.3, pp. 13, points 1(a) and 1(e) about required data structures supporting the implementation of graphs]{Ong2017}, faster implementations of graph common algorithms (e.g., Dijkstra's single-source shortest path algorithm and Prim’s/Prim-Jarnik algorithm to find the minimum spanning tree) use a priority queue (specifically a Fibonacci heap implementation) to perform certain steps faster.

In *Python*, I can use the *heapq* module to use a heap without implementing my own Fibonacci heap.

Also, I can use sets to store collections of vertices and edges of a graph, rather than a list, so that I do not have to implement a set-like data structure myself. The default set data structure in *Python* is a fast implementation \cite{PythonWikiContributors2017}.

***Determine if there exists default implementations of circular arrays and queues (FIFOs).***

*Python*'s default implementations of:
+ queues (FIFOs):
	- [Use a deque](https://en.wikipedia.org/wiki/Double-ended_queue), since "a double-ended queue (abbreviated to deque) is an abstract data type that generalizes a queue".
		* Wikipedia contributors, ``Double-ended queue,'' in *Wikipedia, The Free Encyclopedia: Abstract data types*, Wikimedia Foundation, San Francisco, CA, May 15, 2019. Available online at: \url{https://en.wikipedia.org/wiki/Double-ended_queue}; last accessed on May 16, 2019.
	- Use [synchronized queues](https://docs.python.org/3/library/queue.html).
+ circular arrays
	- [use collections.deque with a maxlen arg](https://stackoverflow.com/questions/4151320/efficient-circular-buffer)
	- [NumPy's ringbuffer](https://pypi.org/project/numpy_ringbuffer/)


Similarly, determine how to implement open addressing in *Python* \cite[\S2.3.3, pp. 14, points 2 and 3 about required data structures supporting the implementation of graphs]{Ong2017}.


###	Miscellaneous Comments

####	*generic graph* class

For the *generic graph* class, use sets instead of lists to store its vertices and edges, so that I don't have to implement the set-like features to manipulate these vertices and edges.
+ *set_of_vertices*
+ *set_of_edges*

####	*undirected graph* classes

+ **graph_ug** class:
	- When implementing the **graph_ug** class, ignore the following for now.
		* *set_of_connected_components*
		* *set_of_cycles*
+ **vertex_ug** class:
	- variables:
		* dict *adjacent_vertices*
			+ Use a dictionary to implement the adjacency map representation of graphs.
+ **edge_ug** class:
	- variables:
		* *set_of_endpoints*



####	*directed graph* class

+ **graph_dg** class:
	- When implementing the **graph_dg** class, ignore the following for now.
		* *set_of_strongly_connected_components*
		* *set_of_directed_cycles*
+ **vertex_dg** class:
	- variables:
		* dict *source_vertices*
			+ Use a dictionary to implement the adjacency map representation of graphs.
		* dict *dstn_vertices*
			+ Use a dictionary to implement the adjacency map representation of graphs.
+ **edge_dg** class:
	- variables:
		* *set_of_source_vertices*
		* *set_of_dstn_vertices*





#	References

Citations/References that use the *LaTeX/BibTeX* notation are taken
	from my *BibTeX* database (set of *BibTeX* entries).







#	Author Information

The MIT License (MIT)

Copyright (c) <2018> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.

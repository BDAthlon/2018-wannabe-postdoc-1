# 2018-wannabe-postdoc-1

This is the repository for problem 1 of the 2018 BDAthlon programming contest.

It my solution for the problem on genetic technology mapping.


## Organization of the Repository

+ docs
	- Documentation generated by documentation generators
		* Doxygen
		* pydoc (for Python scripts): /usr/bin/pydoc
+ notes
	- Software licenses
		* *MIT License*.
	- Guidelines for collaborating on open source software and/or hardware
      projects.
    * Documentation about guidelines that I am following for my research,
  		  and for my research collaborators to know about.
  - Externalities list.
    * *Publicly available library, API, or framework* that I have used as
        external components for my software.
		* Some *Python* modules from the repository [bibtex-analytics](https://github.com/eda-ricercatore/bibtex-analytics),
			which I developed.


##  Description of the Software Solution for Genetic Technology Mapping

My solution for genetic technology mapping, **problem1_solution.py**, takes in
	two input parameters, **[input JSON netlist]** and
	**[output JSON technology mapping]**.

The first input parameter **[input JSON netlist]** is a JSON file that contains
	a structural netlist for genetic technology mapping.

The other input parameter **[output JSON technology mapping]** is the filename
	of an output JSON file that contains a genetic technology mapping for the
	input structural netlist (**[input JSON netlist]**).

The front-end of **problem1_solution.py** parses the input arguments, checks
	their validity, and parses the input structural netlist for genetic
	technology mapping.
	It also parses the genetic technology library **genetic_gate_library.json**,
		maps each genetic NOT gate into a *genetic_not_gate* object, and stores
		each object in a map of *(id,objects)*;
		the *id* of the object is the *id* field of the genetic NOT gate, which is
			specified in the genetic technology library.

The genetic technology mapping engine of **problem1_solution.py** consists of a
	(set of) solution(s) to perform genetic technology mapping.
	A solution is an implementation of a known/new algorithm/heuristic for
		genetic technology mapping.

**Dr. Nicholas Roehner and Dr. Curtis Madsen, I am running out of time, so I
	will sketch the outline of my solutions, and update them as I solve the problem.**

Solution *1a* performs *brute force search* to explore different options for
	genetic technology mapping.
+	Explore each permutation of NOT gates.
+	For each selection, store its alpha value and the permutation in a table
+ Enumerate a table to find the largest alpha value, and select the
		corresponding permutation of NOT gates.


Solution *1b* uses simulated annealing for discrete optimization.
+ Pseudo-randomly select a permutation of NOT gates.
+ Initialize temperature to be very hot
+ While temperature is not 0, cool the temperature of the annealing process.
	- As the temperature cools, slowly decrease the

Solution *1b* uses a genetic algorithm for discrete optimization.


Other solutions considered:
+ 0-1 integer linear programming (ILP)
	* Can't formulate the objective function of the 0-1 ILP problem.
+ pseudo-boolan optimization (PBO)
	* Can't formulate the conjunctive normal form (CNF) boolean satisfiability
		formula for PBO.

The back-end of **problem1_solution.py** generates an output file containing
	the genetic technology mapping of the input genetic circuit, in JSON format.








##  Instructions on How to Build and Run the Software Solution

###	Building and Executing the Software Solution

To execute the software solution, try:

	./problem1_solution.py [input JSON netlist] [output JSON technology mapping]

Input Parameters:
[input JSON netlist]:							A JSON file that contains a structural
																		netlist for genetic technology mapping.

[output JSON technology mapping]:	A filename of an output JSON file that
																		contains a genetic technology mapping for
																		the input structural netlist.


###	Documentation Generation

To use *Doxygen* to generate documentation for the Python software, try:

	make doxygen

To view the *Doxygen*-generated documention, open the file [**docs/html/index.html**](https://github.com/BDAthlon/2018-wannabe-postdoc-1/blob/master/docs/html/index.html) in a Web browser.

The command **make doxygeninit** has already been used to generate a *Doxygen*
	configuration file named **doxygen.config**.
	**DO NOT RUN THE COMMAND *doxygen.config* AGAIN!!!**

To use *pydoc* to view or generate documentation for my software solution
	(Python code), try:

	pydoc [*Python* package/module/class]

A *Python* package corresponds to a subdirectory of this repository, while a
	*Python* module/class corresponds to a *Python* source file in a subdirectory.




##	Miscellaneous

###	Refactoring attempt: **Utilities** package

Refactor the class **queue_ip_args** in the *Python* module
	*queue_ip_arguments.py*, so that does not need the argument **which_script**
	for the static method **set_input_arguments(list_of_ip_arguments,which_script)**.
	That is, refactor the code to





#	References

Citations/References that use the LaTeX/BibTeX notation are taken from my
	BibTeX database (set of BibTeX entries).

Additional references not found in the reference list shall be indicated below
	(TO BE UPDATED).


	@misc{Roehner2018,
		Address = {Boston, {MA}},
		Author = {Nicholas Roehner and Curtis Madsen},
		Howpublished = {Self-published},
		Month = {July 31},
		Publisher = {Boston University},
		School = {Boston University},
		Title = {BDAthlon 2018},
		Year = {2018}}



#	Author Information

The MIT License (MIT)

Copyright (c) <2018> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.

#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to implement
		mathematical operations with numbers.
	

	Synopsis:
	Perform mathematical operations with numbers.


	


	Revision History:
	July 31, 2018			Version 0.1, initial build.
"""

__author__ = 'Zhiyang Ong'
__version__ = '1.0'
__date__ = 'July 31, 2018'

#	The MIT License (MIT)

#	Copyright (c) <2018> <Zhiyang Ong>

#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#	Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"	Che cosa significa?



###############################################################
"""
	Import modules from The Python Standard Library.
	math	For mathematical operations with numbers.
"""

import math




###############################################################
#	Import Custom Python Modules





###############################################################
##	Module with methods that perform mathematical operations
#		with numbers.
class number_ops:
	# ============================================================
	##	Method to get the nearest integer for a floating-point
	#		number.
	#	@param floating_pt_num - A floating-point number.
	#	@return the nearest integer for this floating-point number.
	#	O(?) method.
	#		Computational time complexity depends on these methods:
	#		+ math.ceil()
	#		+ math.floor()
	#
	#	References (last accessed on January 24, 2020):
	#	+ https://www.e-education.psu.edu/egee102/node/1899
	#	+ http://academic.brooklyn.cuny.edu/geology/leveson/core/linksa/roundoff.html
	#	+ https://en.wikipedia.org/wiki/Rounding
	#	+ https://www.chemteam.info/SigFigs/Rounding.html
	#	+ http://www.webmath.com/k8round.html
	#	+ https://www.purplemath.com/modules/rounding.htm
	#	+ https://www.basic-math-explained.com/rounding-off-numbers.html
	@staticmethod
	def get_nearest_integer(floating_pt_num):
		if 0.5 <= floating_pt_num:
			return math.ceil(floating_pt_num)
		else:
			return math.floor(floating_pt_num)


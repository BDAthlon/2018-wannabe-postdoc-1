#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
###	/usr/bin/python
###	/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
	This Python script is written by Zhiyang Ong to perform
		input/output (I/O) operations on files, such as BibTeX
		databases/files and LaTeX documents.

	References:
	\cite[\S11 File and Directory Access, \S11.2 os.path - Common pathname manipulations]{DrakeJr2016b}


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
#	Module with methods that perform file I/O operations.
class file_io_operations:
	#
	# ============================================================
	##	Method to check if a path to file is valid.
	#	@param filename - Path to a file.
	#	@return a boolean TRUE, if the path to the file is valid.
	#		Else, return FALSE.
	#	O(1) method.
	@staticmethod
	def is_path_valid(filename):
		if (os.path.exists(filename) and os.path.isfile(filename)):
			return True
		else:
			return False
	# ============================================================
	##	Method to open a file object for read/input operations.
	#	@param filename - Path to a file.
	#	@return file object ip_file_obj
	#	@throws Exception for invalid path to the file.
	#	O(1) method.
	@staticmethod
	def open_file_object_read(filename):
		if file_io_operations.is_path_valid(filename):
			ip_file_obj = open(filename, 'r')
			return ip_file_obj
		else:
			raise Exception("File Read Operation: Path to file is invalid.")
	# ============================================================
	##	Method to open a file object for write/output operations.
	#	@param filename - Path to a file.
	#	@return file object op_file_obj
	#	@throws Exception for invalid path to the file.
	#	O(1) method.
	@staticmethod
	def open_file_object_write(filename):
		if not file_io_operations.is_path_valid(filename):
			op_file_obj = open(filename, 'w')
			return op_file_obj
		else:
			raise Exception("File Write Operation: Path to file is valid.")
	# ============================================================
	##	Method to close a file object.
	#	@param file_obj - A file object.
	#	@return - Nothing.
	#	O(1) method.
	@staticmethod
	def close_file_object(file_obj):
		file_obj.close()
	# ============================================================
	##	Method to determine if two files are equivalent.
	#	@param file1 - Path to a file.
	#	@param file2 - Path to another file.
	#	@return a boolean TRUE, if the files are equivalent. Else,
	#		return FALSE.
	#	O(n) method, with respect to the number of lines in the
	#		larger (if the files are different), or either, of the
	#		files.
	@staticmethod
	def file_comparison(file1, file2):
		return filecmp.cmp(file1,file2,shallow=False)
	# ============================================================
	##	Method to determine the file extension of a file.
	#	@param filename - Name of a file.
	#	@return the file extension of a file.
	#	O(n) method, with respect to the number of characters in the
	#		path_to_file argument;
	#		traverse the string from the right end till the first
	#			period is found (this indicates the file extension).
	#	References:
	#	1) \cite{Dharmkar2017}\cite{nosklo2017}
	#	2) \cite[\S11 File and Directory Access, \S11.2 os.path - Common pathname manipulations]{DrakeJr2016b}
	@staticmethod
	def get_file_extension(filename):
		temp_filename_extension = ""
		while True:
			filename_prefix, filename_extension = os.path.splitext(filename)
			if not filename_extension:
				break
			else:
				filename  = filename_prefix
				temp_filename_extension = filename_extension + temp_filename_extension
		return temp_filename_extension
	# ============================================================
	##	Method to determine if the file extension of a file matches with
	#		a given file extension.
	#	@param filename - Name of a file.
	#	@param file_extension - Extension
	#	@return boolean True if the file extension of the given filename
	#		matches file_extension; else, return False.
	#	O(n) method, with respect to the number of characters in the
	#		path_to_file argument;
	#		traverse the string from the right end till the first
	#			period is found (this indicates the file extension).
	@staticmethod
	def check_file_extension(filename, file_extension):
		if file_extension == file_io_operations.get_file_extension(filename):
			return True
		else:
			return False
	# ============================================================
	##	Method to determine if the time is valid.
	#	@param hh - Hour of a time in numbers.
	#	@param mm - Minutes of a time in numbers.
	#	@param ss - Seconds of a time in numbers.
	#	@param us - Microseconds of a time in numbers.
	#	@return boolean True if the date is valid;
	#		else, return False.
	#	O(1) method.
	@staticmethod
	def is_valid_time(hh,mm,ss,us):
		# Check if the hour is valid: 0 <= tokens[3] <= 23.
		if (0>hh) or (23<hh):
			return False
		# Check if the minute is valid: 0 <= tokens[4] <= 59.
		if (0>mm) or (59<mm):
			return False
		# Check if the second is valid: 0 <= tokens[5] <= 59.
		if (0>ss) or (59<ss):
			return False
		# Check if the microsecond is valid: 0 <= tokens[6] <= 1000000.
		if (0>us) or (1000000<us):
			return False
		return True
	# ============================================================
	##	Method to determine if the date is valid.
	#	@param dd - Date/Day of a date in numbers.
	#	@param mm - Month of a date in numbers.
	#	@param yy - Year of a date in numbers.
	#	@return boolean True if the date is valid;
	#		else, return False.
	#	O(1) method.
	@staticmethod
	def is_valid_date(dd,mm,yy):
		# Check if the month is valid: 1 <= tokens[1] <= 12.
		if (1>mm) or (12<mm):
			#print("Month is:%d",mm)
			return False
		# Check if the year is valid: 2014 <= tokens[2] <= 2100.
		if (2014>yy) or (2100<yy):
			#print("Year is:%d",yy)
			return False
		# Check if month has 31 days, 1 <= tokens[0] <= 31.
		if ((1 == mm) or (3 == mm) or (5 == mm) or (7 == mm) or (8 == mm) or (10 == mm) or (12 == mm)) and ((1>dd) or (31<dd)):
			"""
			print("Month is:%d",mm)
			print("Date/Day is:%d",dd)
			"""
			return False
		if (calendar.isleap(yy)) and (2 == mm) and ((1 > dd) or (29 < dd)):
			"""
			print("Month is:%d",mm)
			print("Date/Day is:%d",dd)
			print("Leap year is:%d",calendar.isleap(yy))
			print("Year is:%d",yy)
			print("February has 29 days.")
			"""
			return False
		if (not calendar.isleap(yy)) and (2 == mm) and ((1 > dd) or (28 < dd)):
			"""
			print("Month is:%d",mm)
			print("Date/Day is:%d",dd)
			print("Leap year is:%d",calendar.isleap(yy))
			print("Year is:%d",yy)
			print("February has 28 days.")
			"""
			return False
		# Check if the month is valid: 1 <= tokens[0] <= 31.
		if (1>dd) or (30<dd):
			#print("Date/Day is:%d",dd)
			return False
		else:
			"""
			print("Month is:%d",mm)
			print("Date/Day is:%d",dd)
			print("Year is:%d",yy)
			"""
			return True
	# ============================================================
	##	Method to determine if the filename contains information
	#		about the date and time in which the output files are
	#		generated.
	#	@param filename - Name of a file.
	#	@return boolean True if the filename contains the date and
	#		time placed in the DD-MM-YY-HR-SS-US format is valid;
	#		else, return False.
	#	O(n) method, with respect to the number of characters in the
	#		filename argument;
	#		traverse the string from the right end till the first
	#			period is found (this indicates the file extension).
	@staticmethod
	def check_filename_date_time_format(filename):
		# Remove the file extension from the filename.
		filename, filename_extension = os.path.splitext(filename)
		tokens = filename.split("-")
		return (file_io_operations.is_valid_date(int(tokens[0]),int(tokens[1]),int(tokens[2])) and file_io_operations.is_valid_time(int(tokens[3]),int(tokens[4]),int(tokens[5]),int(tokens[6])))

#!/usr/local/bin/python3
###!/Users/zhiyang/anaconda3/bin/python3

"""
	This Python script is written by Zhiyang Ong to implement
		miscellaneous tasks.
	1) Add, commit, and push additions and updates to a Git repository.
	2) ???

	Synopsis:
	Perform miscellaneous tasks.


	#### IMPORTANT NOTES:
	#### IMPORTANT ASSUMPTIONS:
	A complete test suite for this Python module is not provided.
	This is because it would require a Python interface to Git in order
		to test if differences between the last build (or build *n*) and
		the previous last build (or build *n*-1) have been committed and
		pushed to the cloud-based Git repository.
		It involves checking for file additions and deletions, and file
			updates.
	I cannot simply and quickly write a test suite for this, so I have
		only tested this manually.


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
	sys			Get access to any command-line arguments.
	os			Use any operating system dependent functionality.
	os.path		For pathname manipulations.

	subprocess -> call
				To make system calls.

	time		To measure elapsed time.
	warnings	Raise warnings.
	re			Use regular expressions.
	calendar	For checking if given year is a leap year.
"""

import sys
import os
import os.path
#from subprocess import call
import subprocess
#import time
import warnings
#import re
import calendar
from calendar import month_name

###############################################################
#	Import Custom Python Modules

"""
	Package and module to configure the software application's
		parameters.
"""
from utilities.configuration_manager import config_manager
# Package and module to generate filename with time stamp.
#from utilities.generate_results_filename import generate_filename
"""
	Module to test if the generated filename (based on the
		then-current time stamp) conforms to the specified
		format.
"""
from utilities.generate_results_filename_tester import generate_filename_tester

###############################################################
##	Module with methods that perform miscellaneous tasks.
class misc:
	absolute_path_to_store_results = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
	months_of_the_year = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
	# ============================================================
	##	Method to get the absolute path to store results.
	#	It is an accessor method.
	#	@param - Nothing.
	#	@return the absolute path to store results.
	#	O(1) method.
	@staticmethod
	def get_absolute_path_to_store_results():
		if os.path.exists(misc.absolute_path_to_store_results) and os.path.isdir(misc.absolute_path_to_store_results):
			return misc.absolute_path_to_store_results
		else:
			return None
	# ============================================================
	##	Method to validate the absolute path to store results.
	#	It is an query method
	#	@param path_to_file - A path to store the results file.
	#		Assumes that the path ends with the character '/'
	#			for UNIX-like operating systems.
	#		Else, when it is concatenated with the filename, it
	#			can result in an invalid path.
	#	@param filename - A filename.
	#	@return boolean True, if the path to the desired location can
	#		contain the value in "misc.absolute_path_to_store_results"
	#		and the filename of the results file.
	#		Else, return boolean False.
	#	@precondition - If path_to_file is equivalent to the None
	#		object, return False to indicate this method cannot
	#		be carried out to successful completion.
	#	@precondition - If filename is equivalent to the None
	#		object, return False to indicate this method cannot
	#		be carried out to successful completion.
	#	O(1) method.
	@staticmethod
	def check_absolute_path_to_store_results(path_to_file,filename):
		if (path_to_file is None) or (filename is None):
			return False
		# Complete path to the file named 'filename'.
		complete_path = path_to_file + filename
		if os.path.exists(complete_path) and os.path.isdir(path_to_file) and os.path.isfile(complete_path):
			return True
		else:
			return False
	# ============================================================
	##	Method to determine if a filename has the DD-MM-YY-HH-MM-SS-uS.txt
	#		format.
	#	@param filename - A filename.
	#	@return boolean True if the path to the desired location can
	#		be found;
	#		Else, return boolean False.
	#	O(1) method.
	@staticmethod
	def check_filename_format(filename):
		if filename is None:
			print("'filename is None' is:",(filename is None),"=")
			return False
		if not isinstance(filename, str):
			return False
		filename_wo_extn, file_extn = os.path.splitext(filename)
		if ".txt" != file_extn:
			print(".txt != file_extn is:",(".txt" != file_extn),"=")
			return False
		tokens = filename_wo_extn.split("-")
		"""
			Check against the format: DD-MM-YY-HH-MM-SS-uS[.txt].
			tokens[0] = DD/Day
			tokens[1] = MM/Month
			tokens[2] = YY/Year
			tokens[3] = HH/Hour
			tokens[4] = MM/Minute
			tokens[5] = [SS/Second]
			tokens[6] = [uS/Microsecond]

			Are there 7 tokens?
		"""
		if (7 != len(tokens)):
			print("7 != len(tokens)",(7 != len(tokens)),"=")
			return False
		# Is the DD token
		if (not isinstance(tokens[0], int)) or (1 > int(tokens[0])):
			print("isinstance(tokens[0], int) is:",isinstance(tokens[0], int),"=")
			print("isinstance(tokens[1], int) is:",isinstance(tokens[1], int),"=")
			print("2 == int(tokens[1]) is:",(2 == int(tokens[1])),"=")
			print("28 < int(tokens[0]) is:",(28 < int(tokens[0])),"=")
			print("calendar.isleap(int(tokens[2])) is:",calendar.isleap(int(tokens[2])),"=")
			return False
		if (not isinstance(tokens[0], int)) or (not isinstance(tokens[1], int)) and 2 == int(tokens[1]) and (29 < int(tokens[0])) and calendar.isleap(int(tokens[2])):
			print("isinstance(tokens[0], int) is:",isinstance(tokens[0], int),"=")
			print("isinstance(tokens[1], int) is:",isinstance(tokens[1], int),"=")
			print("2 == int(tokens[1]) is:",(2 == int(tokens[1])),"=")
			print("28 < int(tokens[0]) is:",(28 < int(tokens[0])),"=")
			print("calendar.isleap(int(tokens[2])) is:",calendar.isleap(int(tokens[2])),"=")
			return False
		if (not isinstance(tokens[0], int)) or (not isinstance(tokens[1], int)) and (2 == int(tokens[1])) and (28 < int(tokens[0])) and (not calendar.isleap(int(tokens[2]))):
			return False
		if (not isinstance(tokens[0], int)) or (not isinstance(tokens[1], int)) and generate_filename_tester.is_30_day_month(tokens[1]) and 30 < int(tokens[0]):
			return False
		if (not isinstance(tokens[0], int)) or (not isinstance(tokens[1], int)) and generate_filename_tester.is_31_day_month(tokens[1]) and 31 < int(tokens[0]):
			return False
		if (not isinstance(tokens[1], int)) or (1 > int(tokens[1])):
			return False
		if (not isinstance(tokens[1], int)) or (12 < int(tokens[1])):
			return False
		if (not isinstance(tokens[2], int)) or (2000 > int(tokens[2])):
			return False
		if (not isinstance(tokens[3], int)) or (0 > int(tokens[3])):
			return False
		if (not isinstance(tokens[3], int)) or (23 < int(tokens[3])):
			return False
		if (not isinstance(tokens[4], int)) or (0 > int(tokens[4])):
			return False
		if (not isinstance(tokens[4], int)) or (59 < int(tokens[4])):
			return False
		if (not isinstance(tokens[5], int)) or (0 > int(tokens[5])):
			return False
		if (not isinstance(tokens[5], int)) or (59 < int(tokens[5])):
			return False
		if (not isinstance(tokens[6], int)) or (0 > int(tokens[6])):
			return False
		if (not isinstance(tokens[6], int)) or (999999 < int(tokens[6])):
			return False
		return True
	# ============================================================
	##	Method to determine where to store the results of the
	#		experimental, simulation, verification, or testing runs
	#	@param filename - A filename that has the DD-MM-YY-HH-MM-SS-uS.txt.
	#	@return a string representing the absolute path of the location.
	#	@precondition - If the filename does not follow the format
	#		specified in "DD-MM-YY-HH-MM-SS-uS.txt", return a None
	#		object to indicate that no valid location exists for
	#		this filename.
	#	O(1) method.
	@staticmethod
	def find_desired_location_for_results(filename):
		# Does filename have the DD-MM-YY-HH-MM-SS-uS.txt format?
		if not misc.check_filename_format(filename):
			#stderr.write("=	'filename' needs to have the format: DD-MM-YY-HH-MM-SS-uS.txt.")
			return None
		# Remove file extension, and tokenize the filename.
		filename_wo_extn, file_extn = os.path.splitext(filename)
		tokens = filename_wo_extn.split("-")
		"""
			In the repository to store results from experiments,
				simulations, and verification runs, and testing runs,
				classify the files by subdirectories according to year
				first before the month.
		"""
		# Does a directory for the specified year exists?
		path_to_results_file = misc.get_absolute_path_to_store_results() +  "/" + tokens[2]
		if not os.path.isdir(path_to_results_file):
			# Creat the directory for the specified year.
			os.mkdir(path_to_results_file)
		# Does a directory for the specified month exists?
		path_to_results_file = path_to_results_file + "/" + month_name[int(tokens[1])].lower()
		if not os.path.isdir(path_to_results_file):
			# Creat the directory for the specified month.
			os.mkdir(path_to_results_file)
		path_to_results_file = path_to_results_file + "/" + filename
		#print("path_to_results_file:",path_to_results_file,"=")
		return path_to_results_file
	# ============================================================
	##	Method to store the results file in the specified absolute path.
	#	@param path_to_file - A path to store the results file.
	#	@return a file object for the results file.
	#	O(1) method.
	#	Not tested.
	@staticmethod
	def store_results(path_to_file):
		if path_to_file is not None:
			print("= path_to_file is not None")
		if os.path.exists(path_to_file):
			print("= os.path.exists(path_to_file)")
		if os.path.isfile(path_to_file):
			print("= os.path.isfile(path_to_file)")
		if path_to_file.startswith(misc.absolute_path_to_store_results):
			print("= path_to_file.startswith(misc.absolute_path_to_store_results)")
		if (path_to_file is not None) and (not os.path.exists(path_to_file)) and (not os.path.isfile(path_to_file)) and path_to_file.startswith(misc.absolute_path_to_store_results):
			return open(path_to_file, 'w+')
		else:
			return None
	# ============================================================
	##	Method to add, commit, and push additions and updates
	#		to a Git repository.
	#	@param comment - A comment for this commit/build [to the
	#						repository].
	#	@return boolean True if updates can be added, committed,
	#		and push additions to a Git repository;
	#		Else, return boolean False.
	#	O(1) method.
	#	Not tested, since this method can fail when it shouldn't.
	#	It may complain that another Git process is running
	#		in this directory, and report the following error
	#		message.
	#	fatal: Unable to create '/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization/.git/index.lock': File exists.
	#	"Another git process seems to be running in this repository,
	#	e.g., an editor opened by 'git commit'. Please make sure
	#	all processes are terminated then try again. If it still
	#	fails, a git process may have crashed in this repository
	#	earlier:
	#	remove the file manually to continue."
	#
	#	Refactored method to implement Git operations (add,
	#		commit, and push) via the os.system() method, so
	#		that these Git operations can be performed
	#		successfully.
	#	To port the code from using the os.system() method
	#		to the safer and faster methods from the "subprocess"
	#		module, see https://docs.python.org/3/library/subprocess.html#subprocess-replacements.
	#	Or, see \cite[From section "Concurrent Execution", subsection "subprocess — Subprocess management"]{DrakeJr2016b}
	#
	# Use \cite{Barbu2015,Brandon2017} to squelch the output from
	#	running the Git operations to make the output of the automated
	#	regression testing easier to read, skim, and comprehend.
	#
	#
	#	References:
	#	+ [Barbu2015]
	#		- Paul-Gheorghe Barbu, Answer to "Silence git (no errors,
	#			no output, don't say a word)," Stack Exchange Inc.,
	#			New York, NY, May 21, 2015.
	#			Available online from Stack Exchange Inc.: Stack Overflow:
	#				Questions at: https://stackoverflow.com/a/30379171/1531728;
	#				February 14, 2020 was the last accessed date.
	#	+ [Brandon2017]
	#		- Brandon, Comment to Thomas Edwards's answer for
	#			"Can git operate in 'silent mode'?", Stack Exchange Inc.,
	#			New York, NY, November 9, 2017.
	#			Available online from Stack Exchange Inc.: Stack Overflow:
	#				Questions at: https://stackoverflow.com/questions/8943693/can-git-operate-in-silent-mode#comment81367451_8943761; 
	#				February 14, 2020 was the last accessed date.
	@staticmethod
	def add_commit_push_updates_to_git_repository(comment):
		try:
			"""
			print("-------------------------------------------------")
			cmd = ['git', 'add', '-A']
			p = subprocess.Popen(cmd, cwd=config_manager.result_repository)
			#p = subprocess.call(cmd, cwd=config_manager.result_repository)
			print("-	Added. Commit now.")
			print("Precautionary removal of Git's '.git/index.lock'.")
			cmd = ["rm", "-rf", "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization/.git/index.lock"]
			p = subprocess.Popen(cmd, cwd=config_manager.result_repository)
			print("Git's '.git/index.lock' should no longer be there.")
			comment = "Update build via Python script."
			cmd = ["git", "commit", "-m", comment]
			p = subprocess.Popen(cmd, cwd=config_manager.result_repository)
			p.wait()
			print("-	Committed. Push now.")
			cmd = ["git", "push"]
			p = subprocess.Popen(cmd, cwd=config_manager.result_repository)
			p.wait()
			"""
			#print("-------------------------------------------------")
			# Squelch standard output and standard error output.
			current_wking_dir = os.getcwd()
			#new_working_dir = config_manager.result_repository
			new_working_dir = "/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization"
			go_to_new_working_dir = "cd " + new_working_dir
			#print(">>>	pwd is:",go_to_new_working_dir,"=")
			#os.system(go_to_new_working_dir)
			os.chdir("/Users/zhiyang/Documents/ricerca/risultati_sperimentali/std-cell-library-characterization")
			#os.system("pwd")
			#os.system("ls -al")
			#os.system("git add -A -f >/dev/null 2>&1")
			os.system("git add -A -f &> /dev/null")
			#print("-	Added. Commit now.")
			#git_commit_cmd = "git commit -m \"" + comment + "\" >/dev/null 2>&1"
			git_commit_cmd = "git commit -m \"" + comment + "\" &> /dev/null"
			#os.system("git commit -m \"Update build via Python script.\"")
			os.system(git_commit_cmd)
			#os.system("git push >/dev/null 2>&1")
			os.system("git push &> /dev/null")
			go_to_original_working_dir = "cd " + current_wking_dir
			os.system(go_to_original_working_dir)
			os.chdir(current_wking_dir)
			#os.system("pwd")
			#print("-------------------------------------------------")
			return True
		except:
			return False

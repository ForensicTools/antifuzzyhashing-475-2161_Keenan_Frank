'''
File: antifuzz.py

Authors: Kaitlin Keenan and Ryan Frank
'''


# Import needed modules
import sys
import re
import random
import argparse
import subprocess
from shutil import copy2
import ssdeep #http://python-ssdeep.readthedocs.io/en/latest/installation.html


'''
Name: main

Purpose: The main method performs the antifuzzing operations to show the percentage of similarity between two mp3 files.

Parameters: None

Return: 1 if incorrect arguments are passed
	0 if operation has been succesfully run
'''

def main():

	parser = argparse.ArgumentParser()
	
	parser.add_argument("originalFile", help="File to antifuzz")
	
	parser.add_argument("--newFile", help="Name of the antifuzzed file")
	
	parser.add_argument("-m", action='store_true', default=False, help="Change the metadata of the file instead, will still change the ssdeep hash")
	
	args = parser.parse_args()
	
	pattern = re.compile('mp3$')

	if args.newFile is None:
		
		args.newFile = args.originalFile
	
	if not args.originalFile.endswith('.mp3'):
		
		print "Please use a file with the .mp3 extension for your original file"
		
		return 1
	
	if not args.newFile.endswith('.mp3'):
		
		print "Please use a file with the .mp3 extension for your newfile"
		
		return 1
	
	# Take in file
	ogFile = args.originalFile

	# Make copy of file
	nFile = args.newFile

	# Hash original file
	ogHash = ssdeep.hash_from_file(ogFile)
	
	# Make changes to given file
	mp3(ogFile, nFile, args)

	# Hash new file
	newHash = ssdeep.hash_from_file(nFile)

	# Compare the hashes
	diff = str(ssdeep.compare(ogHash, newHash))
	
	print("The files are " + diff + "% similar")

	return 0


'''
Name: mp3

Purpose: Changes mp3 file by using lame to change volume by a scale of 1

Parameters: ogFile - Original mp3 file to be antifuzzed
	    newFile - Antifuzzed mp3 file
	    args - Contains all arguments passed into antifuzz.py

Return: None
'''

def mp3(ogFile, newFile, args):

	if args.m is None:
		cmd(['lame','--quiet', '--scale', '1', ogFile])
	
	else:
		cmd(['lame','--quiet','--tc', str(random.randrange(0, 27)), ogFile])
	
	cmd(['mv', ogFile + ".mp3", newFile])


'''
Name: cmd

Purpose: Runs a shell command

Parameters: command - String array where each argument is a command line argument

Return: out - Standard ouput of shell command
'''

def cmd(command):
	
	p = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	
	out, err = p.communicate()
	
	return out


# Run main method
if __name__ == "__main__":
	main()

'''
File: antifuzz.py

Authors: Kaitlin Keenan and Ryan Frank
'''


# Import needed modules
import sys
import argparse
import subprocess
from shutil import copy2
import ssdeep #http://python-ssdeep.readthedocs.io/en/latest/installation.html


'''
Name: main

Purpose: x

Parameters: None

Return: x
'''

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("originalFile", help="File to antifuzz")
	parser.add_argument("--newFile", help="Name of the antifuzzed file")
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

	ogHash = ssdeep.hash_from_file(ogFile)
	
	# Mess with the given file
	mp3(ogFile, nFile)

	# Hash files
	newHash = ssdeep.hash_from_file(nFile)

	# Compare the hashes
	diff = str(ssdeep.compare(ogHash, newHash))
	print("The files are " + diff + "% similar")

	return 0


'''
Name: mp3

Purpose: changes mp3 file by using lame to change vol by scale of 1

Parameters: ogFile - the original mp3 file to be antifuzzed
	    newFile - the antifuzzed mp3 file

Return: None
'''

def mp3(ogFile, newFile):
	
	cmd(['lame','--quiet', '--scale', '1', ogFile])
	cmd(['mv', ogFile + ".mp3", newFile])


'''
Name: cmd

Purpose: Runs a shell command

Parameters: command - String array - each arg = cmd line

Return: out - std out of shell command
'''

def cmd(command):
	
	p = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	out, err = p.communicate()
	
	return out


# Run main method
if __name__ == "__main__":
	main()

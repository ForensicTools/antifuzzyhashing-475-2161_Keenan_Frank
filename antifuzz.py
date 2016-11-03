'''
File:  antifuzz.py

Authors: Kaitlin Keenan and Ryan Frank

'''

import sys
from shutil import copy2
import subprocess
import ssdeep #http://python-ssdeep.readthedocs.io/en/latest/installation.html
import argparse

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("originalFile", help="File to antifuzz")
	parser.add_argument("newFile", help="Name of the antifuzzed file")
	args = parser.parse_args()

	# Take in file
	ogFile = args.originalFile

	# Make copy of file
	nFile = args.newFile

	# Mess with the given file
	mp3(ogFile, nFile)

	# Hash files
	ogHash = ssdeep.hash_from_file(ogFile)
	newHash = ssdeep.hash_from_file(nFile)

	# Compare the hashes
	#print ogHash
	diff=str(ssdeep.compare(ogHash, newHash))
	print("The files are " + diff + "% different")

def mp3(ogFile, newFile):
	cmd(['lame','--quiet', '--scale', '1', ogFile])
	cmd(['mv', ogFile + ".mp3", newFile])

def cmd(command):
	#if (arg2 && arg1):
	p = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	out, err = p.communicate()
	return out

if __name__ == "__main__":
	main()

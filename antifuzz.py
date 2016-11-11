'''
File: antifuzz.py

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


def mp3(ogFile, newFile):
	
	cmd(['lame','--quiet', '--scale', '1', ogFile])
	cmd(['mv', ogFile + ".mp3", newFile])


def cmd(command):
	
	p = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	out, err = p.communicate()
	
	return out


if __name__ == "__main__":
	main()

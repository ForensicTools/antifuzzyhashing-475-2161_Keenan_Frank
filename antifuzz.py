'''
File:  antifuzz.py

Authors: Kaitlin Keenan and Ryan Frank

'''

import sys
from shutil import copy2
import subprocess
import ssdeep #http://python-ssdeep.readthedocs.io/en/latest/installation.html

def main():

	# Take in file
	ogFile = sys.argv[1]

	# Make copy of file
	newFile = sys.argv[2]

	# Mess with the given file
	cmd(['lame','--quiet', '--scale', '1', ogFile])
	print cmd(['mv', ogFile + ".mp3", newFile])

	# Hash files
	ogHash = ssdeep.hash_from_file(ogFile)
	newHash = ssdeep.hash_from_file(newFile)

	# Compare the hashes
	#print ogHash
	print ssdeep.compare(ogHash, newHash)

def cmd(command):
	#if (arg2 && arg1):
	p = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	out, err = p.communicate()
	return out

if __name__ == "__main__":
	main()

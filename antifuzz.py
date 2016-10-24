'''
File:  antifuzz.py

Authors: Kaitlin Keenan and   Ryan Frank

'''

import sys
from shutil import copy2
import subprocess


def main():


	# Take in file
	ogFile = sys.argv[1]


	# Make copy of file
	newFile = sys.argv[2]

	copy2(ogFile, newFile)


	print "\n"


	# Run ssdeep on files
	hashesFile = open('hashes.txt', 'w+')

	p = subprocess.Popen(['ssdeep', '-b', ogFile, hashesFile], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	
	out, err = p.communicate()

	hashesFile.write(out.decode('utf-8'))

	p2 = subprocess.Popen(['ssdeep', '-bm', hashesFile, newFile], stdout = subprocess.PIPE, stderr = subprocess.PIPE)

	out2, err2 = p2.communicate()

	hashesFile.close()

	print out2 #+ "\n"

	#print err2




if __name__ == "__main__":
	main()

#Authors: Kaitlin Keenan and   Ryan Frank

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



=======
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

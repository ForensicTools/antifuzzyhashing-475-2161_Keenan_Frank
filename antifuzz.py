
#Authors: Kaitlin Keenan and   Ryan Frank

import sys
from shutil import copy2
import subprocess
<<<<<<< HEAD
import ssdeep #http://python-ssdeep.readthedocs.io/en/latest/installation.html
import argparse
=======
>>>>>>> kkeenan-master

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
	#print ogHash
	diff=str(ssdeep.compare(ogHash, newHash))
	print("The files are " + diff + "% similar")

	return 0

def mp3(ogFile, newFile):
	cmd(['lame','--quiet', '--scale', '1', ogFile])
	cmd(['mv', ogFile + ".mp3", newFile])

def cmd(command):
	#if (arg2 && arg1):
	p = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	out, err = p.communicate()
<<<<<<< HEAD
=======

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
>>>>>>> kkeenan-master
	return out

if __name__ == "__main__":
	main()

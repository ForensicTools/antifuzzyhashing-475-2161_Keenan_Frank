# Purpose:

Fuzzy hashing provides a comparison of two files whose content may only vary slightly.  Tools that provide such a service, like ssdeep or VirusTotal, are helpful to forensic investigators, as they can aid in finding potentially incriminating files.  However, an individual may wish to protect their files from being discovered through such a technique.



# Solution:

Our solution is a Python command line utility that serves as an anti-fuzzy hashing tool.  This tool takes in a given mp3 file and makes small changes to it (See Usage for more information).  These changes ensure that, when the antifuzzed file is compared to the original mp3 file via ssdeep, the files will appear to be completely different.



# Usage:

To alter original file by changing file volume by scale of 1:

```python antifuzz.py [filename.mp3]``` 



To keep original file and save volume alterations to new file:

```python antifuzz.py [originalFileName.mp3] --newFile [newFileName.mp3]```



To alter original file by changing file metadata (Program automatically and randomly makes these changes):

```python antifuzz.py -m [filename.mp3]```



To keep original file and save metadata alterations to new file (Program automatically and randomly makes these changes):

```python antifuzz.py -m [originalFileName.mp3] --newFile [newFileName.mp3]```

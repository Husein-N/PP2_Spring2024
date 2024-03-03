import os

path = r'~/PP2/lab6/dir-and-files'

with open(path, 'r') as f:
	lines = len(f.readlines())
	print(lines)
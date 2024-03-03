import os

path = r"husein@DESKTOP-N6HKMU1:~/PP2/lab6/dir-and-files"

for i in range(65,91):
    name = os.path.join(path, chr(i) + ".txt")
    f = open(name, "a")
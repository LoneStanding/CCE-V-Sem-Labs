import sys
import os

filename = sys.argv[-1]
print(filename)

directory = os.path.dirname(os.path.abspath(__file__))

f = open(directory + '\\' + filename, 'r')

revstring = "".join(f.readlines()[-1::-1])
print(revstring)
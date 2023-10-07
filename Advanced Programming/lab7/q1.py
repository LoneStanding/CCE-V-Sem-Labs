import os

path = os.path.dirname(os.path.abspath(__file__))

f = open(path +'\\text.txt', 'rb')

print(len(f.read()))
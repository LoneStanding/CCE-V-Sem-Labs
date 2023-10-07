import os 
import re

regx = "@gmail.com|@yahoo.com|@rediffmail.com{1}$"

directory = os.path.dirname(os.path.abspath(__file__))

f = open(directory + '\\input.txt', 'r')
text = f.read().split('\n')

# print(re.findall(regx, text[2]))

for i in text:
    if re.findall(regx, i) != []:
        print(i)
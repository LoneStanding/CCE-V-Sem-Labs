import re

string = input("Enter a string: ")

nstring = re.sub("([a-zA-Z]+)", lambda x:x.group()[0].upper()+x.group()[1:], string)
print(nstring)
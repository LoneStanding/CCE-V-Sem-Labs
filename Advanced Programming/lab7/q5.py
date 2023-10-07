import re

regex = r'^[a-zA-Z]$|^([a-zA-Z]).*\1$'

string = input("Enter a string: ")

match = re.search(regex, string)
if match:
    print("Valid")
else:
    print("Invalid")
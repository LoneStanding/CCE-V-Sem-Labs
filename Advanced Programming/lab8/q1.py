import re

all_attributes = dir(re)

find_functions = [attr for attr in all_attributes if "find" in attr]

find_functions.sort()

for func in find_functions:
    print(func)

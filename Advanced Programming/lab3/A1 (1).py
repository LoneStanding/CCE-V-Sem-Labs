def count(string):
    upper = 0
    lower = 0

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower


string = input("Enter the string: ")
upper, lower = count(string)
print(f"There are {upper} uppercase and {lower} lowercase letters in above string")

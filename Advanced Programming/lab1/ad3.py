input_string = input("Enter a string: ")

input_string = input_string.lstrip('0x').lstrip('0X')

if len(input_string) > 0 and all(char.isdigit() or char.lower() in 'abcdef' for char in input_string):
    print(input_string, "is a valid hexadecimal number.")
else:
    print(input_string, "is not a valid hexadecimal number.")

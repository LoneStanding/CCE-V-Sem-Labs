class ALessThanB(Exception):
    pass

try:
    n = int(input("Enter the number: "))
    m = int(input("Enter the number: "))
except ValueError:
        print("ERROR: Not a integer")
        exit(0)

op = input("Select operation: ")
if (op == '+'):
    print(f'{n} + {m} = {n+m}')
elif (op == '-'):
    try:
        if n<m: raise ALessThanB
    except ALessThanB:
        print("ERROR: A is less than B")
        exit(0)
    print(f'{n} - {m} = {n-m}')
elif (op == '*'):
    print(f'{n} * {m} = {n*m}')    
elif (op == '/'):
    try:
        print(f'{n} / {m} ={n/m}')
    except ZeroDivisionError: print("ERROR: Division by zero")
elif (op == '%'):
    try:
        print(f'{n} % {m} ={n%m}')
    except ZeroDivisionError: print("ERROR: Division by zero")
else:
    print("Invalid operation")
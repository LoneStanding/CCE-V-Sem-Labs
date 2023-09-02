import math

n = int(input('enter number to be checked'))
num = str(n)
length = len(num)

digit_sum = sum(int(digit)**length for digit in num)

if digit_sum == n :
    print('given number is an armstrong number')
else :
    print('not')
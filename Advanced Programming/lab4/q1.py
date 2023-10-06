import cmath

n = int(input("Enter a number: "))
print("It's sin value is ", "{:.2f}".format(cmath.sin(n).real))
print("It's sqrt value is ","{:.2f}".format(cmath.sqrt(n).real))
print("It's log value is ","{:.2f}".format(cmath.log(n).real))
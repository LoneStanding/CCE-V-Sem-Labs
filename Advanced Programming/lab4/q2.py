import cmath

r,i = int(input("Enter a complex number: ").split(" "))
n = complex(r,i)
print("It's sin value is ", "{:.2f}".format(cmath.sin(n).real), "{:.2f}".format(cmath.sin(n).imag))
print("It's sqrt value is ","{:.2f}".format(cmath.sqrt(n).real), "{:.2f}".format(cmath.sqrt(n).imag))
print("It's log value is ","{:.2f}".format(cmath.log(n).real), "{:.2f}".format(cmath.log(n).imag))

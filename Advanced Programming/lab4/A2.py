from CustomReverse import reverse

n = input("Enter a number: ")
revn = reverse(n)

if revn==n:
    print(f"Pallindrome hai {n}")
else:
    print(f"Pallindrome nhi hai {n}")
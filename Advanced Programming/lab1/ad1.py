m = int(input("Enter the lower limit (m): "))
n = int(input("Enter the upper limit (n): "))

print(f"Prime numbers between {m} and {n} are:")
for number in range(m, n + 1):
    if number <= 1:
        continue
    elif number <= 3:
        print(number)
    elif number % 2 != 0 and number % 3 != 0:
        i = 5
        is_prime = True
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                is_prime = False
                break
            i += 6
        if is_prime:
            print(number)


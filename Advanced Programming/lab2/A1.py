cache = {}
def cash_karo(n):
    if n in cache:
        print("Using cached result for ", n)
        return cache[n]

    print("Performing computation for", n)
    result = n * n
    cache[n] = result
    return result

print(cash_karo(5))
print(cash_karo(5))
print(cash_karo(8))
print(cash_karo(8))
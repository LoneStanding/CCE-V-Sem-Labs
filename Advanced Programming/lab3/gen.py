def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

 

n = 10  
fibonacci = fibonacci_generator()
result = [next(fibonacci) for _ in range(n)]
print(result)
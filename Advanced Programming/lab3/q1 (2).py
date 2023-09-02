
def multiply_nums(numbers) :
    res = 1
    for i in numbers:
        if isinstance(i, (int, float)) :
            res *= i
            
    return res

numbers = [2, 2, -5, 8]
print(f"the product of elements in list {numbers} is", multiply_nums(numbers))

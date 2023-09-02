def count():
    a = 10
    b = "hello"
    c = [1, 2, 3]
    d = {"key": "value"}
    e = None
    name = "sanjana"
    cnt = locals()
    return len(cnt)


cnt = count()
print("Number of local variables:", cnt)
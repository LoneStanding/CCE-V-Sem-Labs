def unique(list) :
    new = []
    for i in list :
        if i not in new :
            new.append(i)
    return new

list = [1, 1, 2, 3, 3, 4, 5]
print(f"{list} after having only one occurence of each value is ", unique(list))
    
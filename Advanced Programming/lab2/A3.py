with open("textfile", "w") as file:
    file.write("hello\n")
    file.write("this\n")
    file.write("is\n")
    file.write("one of\n")
    file.write("the\n")
    file.write("most\n")
    file.write("irritating\n")
    file.write("question\n")
d = {}
with open("textfile", "r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        d[i] = [lines[i], len(lines[i])]
print(d)
d1 = {}
with open("textfile", "r") as file:
    lines = file.read()
    for i in range(len(lines)):
        if lines[i] in d1:
            d1[lines[i]] += 1
        else:
            d1[lines[i]] = 1
print(d1)





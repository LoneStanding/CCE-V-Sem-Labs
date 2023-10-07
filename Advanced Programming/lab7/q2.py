import os 

direc = os.path.dirname(os.path.abspath(__file__))

f = open(direc + '\\text.txt', 'r')

txt = f.read()

delimiters = [' ', '\n']
for delimiter in delimiters:
    txt = " ".join(txt.split(delimiter))

txtlist = txt.split()

count = {}

for i in range(len(txtlist)):
    if txtlist[i] not in count.keys():
        count[txtlist[i]] = 1
    else:
        count[txtlist[i]] += 1

print(count)

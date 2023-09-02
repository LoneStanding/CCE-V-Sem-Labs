n = int(input('enter number of strings'))
str_list = []
for i in range(n) :
    stri = input('enter string')
    str_list.append(stri)

for i in enumerate(str_list):
    print(i)

count = 0

for stri in str_list :
    if len(stri)>=2 and stri[0]==stri[-1] :
        count+=1

print("the number of strings of length greater than or equal to 2 and having same first and last characters is:")
print(count)         

for stri in str_list :
    if len(stri)%2!=0:
        print(stri)

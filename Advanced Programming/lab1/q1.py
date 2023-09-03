m = int(input("enter size of list 1:"))
n = int(input("enter size of list 2:"))

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []


print('enter first list')
for x in range(m) :
    i = int(input())
    list1.append(i)

print('enter second list')
for x in range(n) :
    j = int(input())
    list2.append(j)

for i in list1 :
    if i%2!=0 :
        list3.append(i)

for i in list2 :
    if i%2==0 :
        list4.append(i)

list5 = list3 + list4

print(list5)
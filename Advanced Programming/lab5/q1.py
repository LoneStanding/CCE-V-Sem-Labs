n = int(input("Enter number of employees: "))

emplist = []

for i in range(n):
    _id_ = input("Enter ID: ")
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    department = input("Enter department: ")
    t = (_id_, name, salary, department)
    emplist.append(t)

search = input("Enter ID to search: ")
for i in range(n):
    if search == emplist[i][0]:
        print(emplist[i])
        exit(0)

print("Employee not found")    
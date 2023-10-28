import random


class Bank:
    def __init__(self, name, age, account_number, account_type, balance=0):
        self.name = name
        self.age = age
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
def deposit(banks, account_number, n):
    for i in banks: 
        if (i.account_number == account_number):
            print(f"Name: {i.name}")
            print(f"Age: {i.age}")
            print(f"Acccount Type: {i.account_type}")
            print(f"Account Number: {i.account_number}")
            print(f"Previous Balance: {i.balance}")
            i.balance += n
            print(f"Current Balance: {i.balance}")
            return
        print("Account not FOUND")
def withdraw(banks, account_number, n):
    for i in banks: 
        if (i.account_number == account_number):
            print(f"Name: {i.name}")
            print(f"Age: {i.age}")
            print(f"Acccount Type: {i.account_type}")
            print(f"Account Number: {i.account_number}")
            print(f"Prevoius Balance: {i.balance}")
            if(i.balance - n < 0):
                print("Not enough balance to withdraw")
            else: i.balance -= n
            print(f"Current Balance: {i.balance}")
            return
        print("Account not FOUND")


banks = []
print("----------------WELCOME TO BANKS----------------")
print("1.) New Account")
print("2.) Deposit")
print("3.) Withdraw")
print("4.) EXIT")

ch = int(input())
while(ch != 4):
    if(ch == 1):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        account_number = random.randint(4000, 10000)
        account_type = input("Enter account type: ")
        b = Bank(name, age, account_number, account_type)
        banks.append(b)
        print(f"Your account number is: {account_number}")
    if(ch == 2):
        acc_n = int(input("Enter account_number: "))
        n = int(input("Enter the amount to deposit: "))
        deposit(banks, acc_n, n)
    if(ch == 3):
        acc_n = int(input("Enter account_number: "))
        n = int(input("Enter the amount to withdraw: "))
        withdraw(banks, acc_n, n)
    ch = int(input("Enter choice again: "))

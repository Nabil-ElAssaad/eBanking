import sys


class Bank:
    bankName = "Nabil Bank"

    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, dAmount):
        self.balance = self.balance + dAmount
        print("The balance after deposit : ", self.balance)

    def withdraw(self, wAmount):
        if wAmount > self.balance:
            print("Insufficient Funds ... Cannot perform this operation")
            sys.exit()
        self.balance = self.balance - wAmount
        print("Balance after withdraw : ", self.balance)


print("Welcome to ", Bank.bankName)
name = input("Enter Your name : ")

bank = Bank(name)
while True:
    print("d for Deposit \nw for withdraw \nc for Check Balance \ne for Exit")
    option = input("Enter Your Option : ")
    if option.lower() == "d":
        amount = eval(input("Enter Amount tp deposit : "))
        bank.deposit(amount)
    elif option.lower() == "w":
        amount = eval(input("Enter Amount tp withdraw : "))
        bank.withdraw(amount)
    elif option.lower() == "c":
        print("Your Balance is ", bank.balance)
    elif option.lower() == "e":
        print("Thanks for banking with" , bank.bankName)
        sys.exit()
    else:
        print("invalid Option please choose correct option")

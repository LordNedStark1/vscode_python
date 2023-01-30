


class Account:
   
    def __init__(self,account_name, account_type):
        self.account_name = account_name
        self.account_type = account_type

def deposit(amount):
   
    balance = balance + amount

def withdraw(amount):
    if balance >amount and balance> 0:
        balance = balance - amount
    else: 
        return "Insufficient funds"
def getBalance():
    return balance

def main():
    deposit(eval(input("Enter deposit amount")))
    print (" the balance is ", getBalance)
    withdraw(eval(input("Enter the withdrawal amount")))
    print (" the balance is ", getBalance)
main()






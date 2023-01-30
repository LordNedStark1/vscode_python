class Account:
    balance = 0

    def __init__(self,account_name, account_type):
        self.account_name = account_name
        self.account_type = account_type

    def deposit(self, amount):
    
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if balance > amount and balance> 0:
            balance = balance - amount
        else: 
            return "Insufficient funds"
    def getBalance(self):
        return self.balance


class MainClass:
    if __name__=='main':
        account = Account("Elite", "Savings")
        account.deposit(eval(input("Enter deposit amount")))
        print (" the balance is ", account.getBalance)
        account.withdraw(eval(input("Enter the withdrawal amount")))
        print (" the balance is ", account.getBalance)
    






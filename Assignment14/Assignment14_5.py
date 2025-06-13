# Create a class BankAccount with account_number, name and balance. Create method for deposit, withdraw and displaying balance

class BankAccount:

    def __init__(self,account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Deposited amount", amount)
        else:
            print("Deposit amount should be positive")
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn amount", amount)
        else:
            print("Insufficient balance or invalid withdraw amount")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}")

def main():
    aobj = BankAccount("123456789", "John Doe", 1000)
    aobj.display_balance()
    aobj.deposit(500)
    aobj.display_balance()
    aobj.withdraw(200)
    aobj.display_balance()

if __name__ == "__main__":
    main()
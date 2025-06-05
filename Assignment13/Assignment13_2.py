class BankAccount():
    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return
        self.Amount = self.Amount + amount

    def Withdraw(self, amount):
        if amount <= 0 or amount > self.Amount:
            print("Invalid withdraw amount")
            return
        self.Amount = self.Amount - amount
    
    def CalculateInterest(self, years):
        pass

    def Display(self):
        print(self.Name, "having balance is ", self.Amount)

def main():
    obj1 = BankAccount("Radha Kavade", 1000)
    obj1.Deposit(500)
    obj1.Withdraw(200)
    obj1.Display()

    obj2 = BankAccount("Shivani Patil", 2000)
    obj2.Deposit(1000)
    obj2.Withdraw(500)
    obj2.Display()
    
if __name__ == "__main__":
    main()
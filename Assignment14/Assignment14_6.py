# Create a class Calculator with method for Add, Subsctract, Multiply, Divide. Ask user input for values and call methods accordingly

class Calculator:
    def __init__(self, no1, no2):
        self.value1 = no1
        self.value2 = no2

    def Addition(self):
        return self.value1 + self.value2

    def Subtraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        if self.value2 != 0:
            return self.value1 / self.value2
        else:
            return "Division by zero is not allowed"

def main():
    print("Enter 1st number:")
    no1 = int(input())

    print("Enter 2nd number:")
    no2 = int(input())

    cobj = Calculator(no1, no2)
    print("Addition:", cobj.Addition())
    print("Subtraction:", cobj.Subtraction())
    print("Multiplication:", cobj.Multiplication())
    print("Division:", cobj.Division())

if __name__ == "__main__":
    main()
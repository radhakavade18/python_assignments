class Arithmatic():

    def __init__(self):
        self.No1 = 0
        self.No2 = 0

    def Accept(self, A, B):
        self.No1 = A
        self.No2 = B

    def Addition(self):
        return self.No1 + self.No2

    def Substraction(self):
        return self.No1 - self.No2

    def Multiplication(self):
        return self.No1 * self.No2

    def Division(self):
        return self.No1 / self.No2

def main():
    obj = Arithmatic()
    obj.Accept(10, 11)
    ret = obj.Addition()
    print(ret)

    ret = obj.Substraction()
    print(ret)

    ret = obj.Multiplication()
    print(ret)

    ret = obj.Division()
    print(ret)

if __name__ == "__main__":
    main()

class Demo():
    Value = 10

    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B

    def Fun(self):
        print(self.No1)

    def Gun(self):
        print(self.No2)

def main():
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)
    obj1.Fun()
    obj1.Gun()
    obj2.Fun()
    obj2.Gun()

if __name__ == "__main__":
    main()
    
    
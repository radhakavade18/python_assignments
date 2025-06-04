class Circle():
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Circumference = 0.0
        self.Area = 0.0

    def CalculateArea(self):
        self.Area =  self.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference =  2 * self.PI * self.Radius
    
    def Accept(self, A):
        self.Radius = A

    def Display(self):
        self.CalculateArea()
        self.CalculateCircumference()
        print(self.Radius)
        print(self.Area)
        print(self.Circumference)

def main():
    obj = Circle()
    obj.Accept(10)
    obj.Display()

if __name__ == "__main__":
    main()

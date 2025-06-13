# Create a class Rectangle with length and width. Add member to compute area and perimeter.
# Area = 50, Perimeter = 30

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def CalculateArea(self):
        area = self.width * self.length
        print("Area of Rectangle:", area)

    def CalculatePerimeter(self):
        perimeter = 2 * (self.width + self.length)
        print("Perimeter of Rectangle:", perimeter)

def main():
    robj = Rectangle(5, 10)
    robj.CalculateArea()
    robj.CalculatePerimeter()

if __name__ == "__main__":
    main()
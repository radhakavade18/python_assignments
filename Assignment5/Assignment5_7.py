# Area and perimeter of Rectangle
# Accept length and width of rectangle. Calculate and display the area and perimeter
# Input - length -5, width-3
# Output - Area - 15, Perimeter - 16

CalculateArea = lambda length, width: length * width

CalculatePerimeter = lambda length, width: 2 * length + 2 * width 

def main():
    print("Enter length")
    length = int(input())

    print("Enter width")
    width = int(input())

    ret = CalculateArea(length, width)
    print("Area of reactangle", ret)

    ret = CalculatePerimeter(length, width)
    print("Perimeter of rectangle", ret)

if __name__ == "__main__":
    main()
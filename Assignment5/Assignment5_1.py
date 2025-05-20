# Arithmatic operations on 2 numbers
# Write a program to accept 2 integer from user and display their
# Sum
# Difference
# Product
# Division
# Input - 10    2
# Sum - 12, Difference - 8, Product - 20, Division - 5.0

Sum = lambda a, b : a + b
Difference = lambda a, b: a - b
Product = lambda a, b: a * b
Division = lambda a, b: a / b

def main():
    print("Enter 1st number")
    no1 = int(input())

    print("Enter 2nd number")
    no2 = int(input())

    ret = Sum(no1, no2)
    print("Sum is ", ret)

    ret = Difference(no1, no2)
    print("Difference is", ret)

    ret = Product(no1, no2)
    print("Product is", ret)

    ret = Division(no1, no2)
    print("Division is", ret)

if __name__ == "__main__":
    main()
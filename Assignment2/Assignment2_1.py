# Create a module name Arithmatic, which contain 4 functions Add() for Addition, Sub() for Subsctraction, Multi() for multiplication,
# Division() for Division. All function accepts 2 parameters as number and perform the operation.
# write a python program which calls the all functions from arithmatic module by accepting parameters from user.

import Arithmatic

def main():
    print("Enter 1st number")
    value1 = int(input())

    print("Enter 2nd number")
    value2 = int(input())

    res = Arithmatic.Addition(value1, value2)
    print("Addition is ", res)

    res = Arithmatic.Substraction(value1, value2)
    print("Substraction is ", res)

    res = Arithmatic.Multiplication(value1, value2)
    print("Multiplication is ", res)

    res = Arithmatic.Division(value1, value2)
    print("Division is ", res)

if __name__ == "__main__":
    main()
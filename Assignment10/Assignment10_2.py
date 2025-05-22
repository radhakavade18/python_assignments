# Write a program which contain 1 lambda function which accepts 2 parameter and return its multiplication

Multiplication = lambda value1, value2: value1 * value2

def main():
    print("Enter 1st number")
    no1 = int(input())

    print("Enter 2nd number")
    no2 = int(input())

    result = Multiplication(no1, no2)

    print("Result:", result)

if __name__ == "__main__":
    main()
# Write a program which contain 1 lambda function which accepts 1 parameter and return power of 2

Power = lambda value: value ** 2

def main():
    print("Enter number")
    no = int(input())

    result = Power(no)

    print("Result:", result)

if __name__ == "__main__":
    main()
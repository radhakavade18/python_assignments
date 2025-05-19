# write a program which contains one lambda function which accepts two parameters and return its multiplication
# Input - 4     Output - 16

Power = lambda value : value ** 2

def main():
    print("Enter number")
    no = int(input())

    ret = Power(no)
    print("Power is ", ret)

if __name__ == "__main__":
    main()
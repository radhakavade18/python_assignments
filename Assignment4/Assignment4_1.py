# write a program which contains one lambda function which accepts one parameter and return power of two
# Input - 4     Output - 16

Power = lambda value : value ** 2

def main():
    print("Enter number")
    no = int(input())

    ret = Power(no)
    print("Power is ", ret)

if __name__ == "__main__":
    main()
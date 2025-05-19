# write a program which accepts number from user and return its factorial
# Input- 12, O/p - 120

def Factorial(no):
    value = 1
    while(no > 0):
        value = no * value
        no -= 1
    return value

def main():
    print("Enter number")
    value = int(input())

    res= Factorial(value)
    print("Factorials is :", res)

if __name__ == "__main__":
    main()
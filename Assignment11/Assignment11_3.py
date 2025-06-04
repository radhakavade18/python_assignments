# Write a recursive function to calculate the sum of digits of a number

sum = 0
def Factorial(no):
    sum = 0
    while(no >= 1):
        value = no % 10
        print(value)
        Factorial(value)

    return sum

def main():
    print("Enter number")
    no = int(input())
    
    Factorial(no)

if __name__ == "__main__":
    main()
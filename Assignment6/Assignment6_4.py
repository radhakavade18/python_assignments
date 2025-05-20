# Accept number from user and print its factorials using for loop
# Input - 5
# Output - 120 (1*2*3*4*5)

def CalculateFactorial(value):
    fact = 1
    for i in range(1, value+1):
        fact = fact * i

    return fact 

def main():
    print("Enter number")
    no = int(input())

    ret = CalculateFactorial(no)
    print("Factorial of", no,"is",ret)
    
if __name__ == "__main__":
    main()
# write a program which accepts number from user and check whether number is prime or not
# Input - 5 , O/P- its a prime number

def CheckPrime(no):
    isPrime = True

    for i in range(2, int(no/2)+1):
        if(no % i == 0):
            isPrime = False

    if isPrime:
        print("Prime number")
    else:
        print("Not a prime number")
        
def main():
    print("Enter number")
    value = int(input())

    CheckPrime(value)

if __name__ == "__main__":
    main()
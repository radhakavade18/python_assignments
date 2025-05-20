# Accept number from user and check whether it is prime number of not
# Input - 11
# Output - Its a prime number

def CheckPrime(value):
    isPrime = True
    for i in range(2, int(value/2)):
        if value % i == 0:
            isPrime = False
    
    return isPrime

def main():
    print("Enter number")
    no = int(input())

    ret = CheckPrime(no)

    if ret == True:
        print("Its a prime number")
    else:
        print("Is not a prime number")
    
if __name__ == "__main__":
    main()
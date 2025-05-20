# Accept list of integer from the user and use filter() function to return list of prime numbers only.

# Input - 10 11 12 13 14 15 16 17
# Output - 11 13 17

def CheckPrime(value):
    isPrime = True
    for i in range(2, int(value/2)):
        if value % i == 0:
            isPrime = False
            
    if isPrime == True:
        return value

def main():
    Data = []
    print("Enter numbers")
    for i in range(8):
        Data.append(int(input()))

    fData = list(filter(CheckPrime, Data))
    print("List of prime numbers", fData)

if __name__ == "__main__":
    main()
# Write a program which accepts N numbers from user and store it into list. Returns addition of all prime numbers from that list.
# main python file accepts N number from user and pass each number to chekPrime() function which is part of our user defined module
# named as MarvellousNum. Name of the function from main python file should be ListPrime()

# Input- Number of element: 11
# Input - Elements : 13  5  45  7  4  56  10   34  2   5  8
# Output - 54(13+5+7+2+5)

import MarvellousNum

def main():
    print("Enter number of elements")
    size = int(input())

    print("Enter elements")
    Data = []
    for i in range(size):
        Data.append(int(input()))

    PrimeData = []

    for i in Data:
        ret = MarvellousNum.ChkPrime(i)
        if(ret == True):
            PrimeData.append(i)

    sum = 0
    for i in PrimeData:
        sum = sum + i
    print("Addition of prime numbers is", sum)

if __name__ == "__main__":
    main()
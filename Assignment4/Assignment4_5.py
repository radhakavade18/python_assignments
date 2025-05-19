# write a program which contains filter(), map() and reduce() in it. Pyhton application which contain one list of numbers.
# list contain numbers which are accepted from user. Filter function should filter out all prime numbers.
# Map function will multiply each number by 2. Reduce will return maximum number from that numbers.

# Input - [4, 34, 36, 76, 68, 24, 89, 90]
# List after filter - [76, 89, 90, 70]
# List after map - [86, 99, 100, 80]
# Output of reduce - 6538752000

from functools import reduce

def CheckPrime(Value):
    for i in range(2,int(Value/2)+1):
        if Value % i != 0:
            return Value

MultiplyByTwo = lambda value:value * 2

def MaxNumber(no1, no2):
    max = 0
    if no1 > no2:
        max = no1
    return max

def main():
    print("Enter number of elements")
    size = int(input())

    print("Enter element")
    Data = list()

    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(CheckPrime, Data))

    print("Filterd data",FData)

    MData = list(map(MultiplyByTwo, FData))

    print("Map data", MData)

    RData = reduce(MaxNumber, MData)

    print("Maximum number is", RData)

if __name__ == "__main__":
    main()
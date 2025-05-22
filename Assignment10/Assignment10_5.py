# Write a program which contain filter(), map() and reduce() in it. Write python application which contain 1 list of numbers. List contain numbers which are accepted from user. Filter should filter out such a numbers which are prime number. Map function will multiply by 2. Reduce will return addition of all that numbers

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
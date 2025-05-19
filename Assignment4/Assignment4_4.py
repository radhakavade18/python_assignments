# write a program which contains filter(), map() and reduce() in it. Pyhton application which contain one list of numbers.
# list contain numbers which are accepted from user. Filter function should filter out such numbers which are even.
# Map function will calculate its square. Reduce will return addition of all that numbers

# Input - [4, 3, 6, 7, 8, 4, 9, 6, 5, 7, 9, 3]
# List after filter - [4, 6, 8, 4, 6]
# List after map - [16, 36, 64, 16, 36]
# Output of reduce - 168

from functools import reduce

def CheckEven(Value):
    if (Value % 2 == 0):
        return Value

CalculateSqr = lambda value: value * value

Addition = lambda no1, no2: no1 + no2

def main():
    print("Enter number of elements")
    size = int(input())

    print("Enter element")
    Data = list()

    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(CheckEven, Data))

    print("Filterd data",FData)

    MData = list(map(CalculateSqr, FData))

    print("Map data", MData)

    RData = reduce(Addition, MData)

    print("Addition of all numbers", RData)

if __name__ == "__main__":
    main()
# write a program which contains filter(), map() and reduce() in it. Pyhton application which contain one list of numbers.
# list contain numbers which are accepted from user. Filter function should filter out such numbers which are grater than 70
# and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers

# Input - [4, 34, 36, 76, 68, 24, 89, 90, 45, 70]
# List after filter - [76, 89, 90, 70]
# List after map - [86, 99, 100, 80]
# Output of reduce - 6538752000

from functools import reduce

def FilterNumber(Value):
    if (Value > 70 and Value <= 90):
        return Value

IncreaseNumber = lambda(value):value + 10

CalculateProduct = lambda (no1, no2): no1 * no2

def main():
    print("Enter number of elements")
    size = int(input())

    print("Enter element")
    Data = list()

    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(FilterNumber, Data))

    print("Filterd data",FData)

    MData = list(map(IncreaseNumber, FData))

    print("Map data", MData)

    RData = reduce(CalculateProduct, MData)

    print("Product of all numbers", RData)

if __name__ == "__main__":
    main()
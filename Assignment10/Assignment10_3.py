# Write a program which contain filter(), map() and reduce() in it. Write python application which contain 1 list of numbers. List contain numbers which are accepted from user. Filter should filter out such a numbers which are grater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers
from functools import reduce

NumberInRange = lambda no: no >= 70 and no <= 90

IncreaseBy10 = lambda no: no + 10

Product = lambda no1, no2: no1 * no2

def main():
    print("Enter number of elements")
    size = int(input())

    Data = []
    print("Enter elements")
    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(NumberInRange, Data))
    print("Filtered Data", FData)

    MData = list(map(IncreaseBy10, FData))
    print("Mapped Data", MData)

    RData = reduce(Product, MData)
    print("Final Result", RData)

if __name__ == "__main__":
    main()
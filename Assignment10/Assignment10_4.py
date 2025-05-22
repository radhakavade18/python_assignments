# Write a program which contain filter(), map() and reduce() in it. Write python application which contain 1 list of numbers. List contain numbers which are accepted from user. Filter should filter out such a numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers

from functools import reduce

EvenNumber = lambda no: no % 2 == 0

CalculateSquare = lambda no: no * no

Addition = lambda no1, no2: no1 + no2

def main():
    print("Enter number of elements")
    size = int(input())

    Data = []
    print("Enter elements")
    for i in range(size):
        Data.append(int(input()))

    FData = list(filter(EvenNumber, Data))
    print("Filtered Data", FData)

    MData = list(map(CalculateSquare, FData))
    print("Mapped Data", MData)

    RData = reduce(Addition, MData)
    print("Final Result", RData)

if __name__ == "__main__":
    main()
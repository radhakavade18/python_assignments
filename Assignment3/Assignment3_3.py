# Write a program which accepts N numbers from user and store it in a list, accept one another number from user, Return frequency of that
# number from that list.
# Input: 5
# Eleemnt to search: 4
# Input element: 13   4   45  4   4   56
# Output: 3

def CountFrequency(Value, no):
    count = 0
    for i in Value:
        if i == no:
            count += 1

    return count

def main():
    print("Enter number of elements")
    size = int(input())

    Data = list()

    print("Enter the values")
    for i in range(size):
        Data.append(int(input()))

    print("Enter element to search")
    ele = int(input())
    
    ret = CountFrequency(Data, ele)
    print("Count is:", ret)

if __name__ == "__main__":
    main()
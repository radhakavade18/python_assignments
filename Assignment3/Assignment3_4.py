# Write a program which accepts N numbers from user and store it in a list, Return minimum number from that list.
# Input: 5
# Input element: 13   5   45  7   4   56
# Output: 56

def MinimumNum(Value):
    min = Value[0]
    for no in Value:
        if(min > no):
            min = no

    return min

def main():
    print("Enter number of elements")
    size = int(input())

    Data = list()

    print("Enter the values")
    for i in range(size):
        Data.append(int(input()))
    
    ret = MinimumNum(Data)
    print("Minimum Number is:", ret)

if __name__ == "__main__":
    main()
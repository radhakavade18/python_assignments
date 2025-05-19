# Write a program which accepts N numbers from user and store it in a list, Return maximum number from that list.
# Input: 5
# Input element: 13   5   45  7   4   56
# Output: 56

def MaximumNum(Value):
    max = Value[0]
    for no in Value:
        if(max < no):
            max = no

    return max

def main():
    print("Enter number of elements")
    size = int(input())

    Data = list()

    print("Enter the values")
    for i in range(size):
        Data.append(int(input()))
    
    ret = MaximumNum(Data)
    print("Maximum Number is:", ret)

if __name__ == "__main__":
    main()
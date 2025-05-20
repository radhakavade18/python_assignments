# Accept 5 inputs from user. Find and print largest number
# Output - 23 89 12 56 45

def FindLargest(Data):
    Max = Data[0]
    for i in Data:
        if i > Max:
            Max = i
    
    return Max

def main():
    print("Enter 5 numbers")
    Data = list()

    for i in range(5):
        Data.append(int(input()))

    ret = FindLargest(Data)
    print("maximum number is", ret)
    
if __name__ == "__main__":
    main()
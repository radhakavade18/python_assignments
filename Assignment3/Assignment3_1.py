# Write a program which accepts N numbers from user and store it in a list, Return addition of all elements from that list.
# Input: 6
# Input element: 13   5   45  7   4   56
# Output: 130

def Addition(Value):
    sum = 0
    for no in Value:
        sum += no
    return sum

def main():
    print("Enter number of elements")
    size = int(input())

    Data = list()

    print("Enter the values")
    for i in range(size):
        Data.append(int(input()))
    
    ret = Addition(Data)
    print("Addition of all elements is:", ret)

if __name__ == "__main__":
    main()
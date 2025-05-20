# Find the largest among three numbers
# Accept 3 number from user, and print the largest using nested if-else statement
# Input - 5   9   3
# Output - 9

def CheckLargestNum(value1, value2, value3):
    max = 0
    if value1 > value2 and value1 > value3:
        max = value1
    elif value2 > value1 and value2 > value3:
        max = value2
    else:
        max = value3
    
    return max

def main():
    print("Enter 1st number")
    no1 = int(input())

    print("Enter 2nd number")
    no2 = int(input())

    print("Enter 3rd number")
    no3 = int(input())

    ret = CheckLargestNum(no1, no2, no3)
    print("Maximum number is ", ret)

if __name__ == "__main__":
    main()
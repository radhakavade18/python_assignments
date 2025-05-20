# Even and Odd number check
# Write a program to check whether the entered number is even or odd
# Input - 5 
# Output - Odd

def CheckEvenOdd(value):
    if (value % 2 == 0):
        return "Even number"
    else:
        return "Odd number"

def main():
    print("Enter number")
    no = int(input())

    ret = CheckEvenOdd(no)
    print(no, "is an", ret)

if __name__ == "__main__":
    main()
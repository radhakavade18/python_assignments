# write a program which accepts number from user and return number of digits in that number
# input - 2345, O/P - 4

CountLength = lambda no: len(str(no))
        
def main():
    print("Enter number")
    value = int(input())

    print("length is ", CountLength(value))

if __name__ == "__main__":
    main()
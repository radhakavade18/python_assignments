def CheckDivisibleBy5(no):
    if no % 5 == 0:
        return True
    else:
        return False

def main():
    print("Enter a number: ")
    no = int(input())
    ret = CheckDivisibleBy5(no)
    if ret: 
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
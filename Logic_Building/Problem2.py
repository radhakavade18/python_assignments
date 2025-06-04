# Accept one number from user and check whether it is divisible by 5 or not

def CheckDivisible(no):
    if no % 5 == 0:
        return True
    else:
        return False

def main():
    print("Enter number")
    no = int(input())

    ret = CheckDivisible(no)

    if ret == True:
        print("Divisible by 5")
    else: 
        print("Not divisible by 5")

if __name__ == "__main__":
    main()
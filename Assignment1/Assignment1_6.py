def CheckNumber(no):
    if no > 0:
        print("Positive")
    elif no < 0:
        print("Negative")
    else:
        print("Zero")

def main():
    print("Enter a number: ")
    no = int(input())
    CheckNumber(no)

if __name__ == "__main__":
    main()
# Accept one number from user and print that number of * on screen

def Display(no):
    for i in range(no):
        print("*")

def main():
    print("Enter number")
    no = int(input())

    Display(no)

if __name__ == "__main__":
    main()
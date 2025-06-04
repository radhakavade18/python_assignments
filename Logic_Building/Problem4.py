# Accept 2 numbers from user and display 1st number 2nd number of times

def Display(no1, no2):
    for i in range(no2):
        print(no1)

def main():
    print("Enter 1st number")
    no1 = int(input())

    print("Enter 2nd number")
    no2 = int(input())

    Display(no1, no2)

if __name__ == "__main__":
    main()
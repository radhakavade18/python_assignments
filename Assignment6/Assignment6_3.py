# Accept number from user and print its multiplication table up to 10
# Input - 7
# Output - 7 14 21 28.....

def DisplayTable(value):
    i = 1
    while(i <= 10):
        print(value * i)
        i = i + 1

def main():
    print("Enter number to display its table")
    no = int(input())
    DisplayTable(no)
    
if __name__ == "__main__":
    main()
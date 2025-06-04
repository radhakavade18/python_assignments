# Print Numbers using recursion, write a recursive function to print numbers from 1 to N

count = 1
def PrintNum(value):
    global count
    if value >= 1:
        print(count)
        count = count + 1
        value = value - 1
        PrintNum(value)

def main():
    print("Enter number")
    no = int(input())
    
    PrintNum(no)

if __name__ == "__main__":
    main()
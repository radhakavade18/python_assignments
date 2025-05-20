# Print sum of even numbers between 1 to 100. use a loop to find and print the sum of all even numbers from 1 to 100
# Output - Sum of even numbers from 1 to 100 - 2550

def CheckEven():
    i = 1
    sum = 0
    while(i <= 100):
        if i % 2 == 0:
            sum = sum + i
        i = i + 1
    
    return sum

def main():
    ret = CheckEven()

    print("Sum of Even numbers from 1 to 100:", ret)
    
if __name__ == "__main__":
    main()
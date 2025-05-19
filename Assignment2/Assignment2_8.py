# write a program which accepts number from user and display below pattern
# Input : 5
# O/P - 
# 1
# 1   2
# 1   2   3
# 1   2   3   4
# 1   2   3   4   5

def DisplayPattern(no):
    temp = 1
    while (temp <= no):
        for i in range(1, temp+1):
            print(i, end=" ")
        print()
        temp = temp + 1
        

def main():
    print("Enter number")
    value = int(input())

    DisplayPattern(value)

if __name__ == "__main__":
    main()
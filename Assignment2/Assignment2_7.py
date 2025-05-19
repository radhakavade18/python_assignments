# write a program which accepts number from user and display below pattern
# Input : 5
# O/P - 
# 1   2   3   4   5
# 1   2   3   4   5
# 1   2   3   4   5
# 1   2   3   4   5
# 1   2   3   4   5

def DisplayPattern(no):
    for i in range(1,no+1):
        print(i, end=" ")
    print()
        

def main():
    print("Enter number")
    value = int(input())

    for no in range(value):
        DisplayPattern(value)

if __name__ == "__main__":
    main()
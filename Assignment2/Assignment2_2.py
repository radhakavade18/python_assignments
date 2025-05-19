# write a program which accepts number from user and display below pattern
# Input : 5
# O/P -
# *   *   *   *   *
# *   *   *   *   *
# *   *   *   *   *
# *   *   *   *   *
# *   *   *   *   *

def DisplayPattern(no):
    temp = no
    while (temp > 0):
        for i in range(no):
            print("*", end=" ")
        print()
        temp = temp - 1
        

def main():
    print("Enter number")
    value = int(input())

    DisplayPattern(value)

if __name__ == "__main__":
    main()
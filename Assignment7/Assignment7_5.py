# Write a function that accepts a string and checks whether it is palindrome.

# Input - radar
# Output - it is palindrom

def CheckPalindrom(value):
    if value == (''.join(reversed(value))):
        print("Its a palindrom string")
    else:
        print("Its not a palindrom strign")

def main():
    print("Enter string")
    value = input()

    CheckPalindrom(value)

if __name__ == "__main__":
    main()
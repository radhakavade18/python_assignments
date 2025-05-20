# Accept single character from user and check if it is a vowel(a, e, i, o, u). If not print its a consonant
# Input - e
# Output - Its a vowel

def CheckVowel(char):
    if (char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u') or (char == 'A') or (char == 'E') or (char == 'I') or (char == 'O') or (char == 'U'):
        print("Its a vowel")
    else:
        print("Its a consonant")

def main():
    print("Enter a character")
    char = input()

    CheckVowel(char)

if __name__ == "__main__":
    main()
# Accept 10 mubers from user and write then into file named Numbers.txt, each on new line

import os

def main():
    fileName = "Numbers.txt"

    fobj = open(fileName, "w")
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    for number in numbers:
        fobj.write(str(number) + "\n")
    fobj.close()

if __name__ == "__main__":
    main()
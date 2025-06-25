# Write a program to read a file line by line and display only those lines which contain more than 5 words

import os

def main():
    fileName = input("Enter file name: ")
    ret = os.path.exists(fileName)

    if ret:
        fobj = open(fileName, "r")
        lines = fobj.readlines()

        for line in lines:
            word = line.split()
            if len(word) > 5:
                print(line.strip())

        fobj.close()

if __name__ == "__main__":
    main()
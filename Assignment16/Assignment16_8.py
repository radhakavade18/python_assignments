# Write a script to remove all blank lines from a file. Save the cleaned output to new file

import os

def main():
    fileName = input("Enter file name: ")

    fobj = open(fileName, 'r')
    lines = fobj.readlines()
    fobj.seek(0)

    fobj2 = open("Clean.txt", "w")
    for line in lines:
        if line.strip():
            fobj2.writelines(line)


if __name__ == "__main__":
    main()
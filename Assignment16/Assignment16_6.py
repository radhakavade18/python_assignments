# Write a program to copy content from one file to another file

import os

def main():
    sourceFile = input("Enter file name: ")
    destFile = input("Enter destination file name: ")

    ret = os.path.exists(sourceFile)
    if ret:
        sObj = open(sourceFile, "r")
        dObj = open(destFile, "w")

        data = sObj.read()
        dObj.write(data)

        sObj.close()
        dObj.close()
    else:
        print("Source file does not exist.")


if __name__ == "__main__":
    main()
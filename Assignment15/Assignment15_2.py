# Write a program which accepts file name from user and open that file and display its content on screen
# Demo.txt
# Hello my name is Radha
import os

def main():
    fileName = input("Enter the file name: ")

    fobj = open(fileName, "r")

    ret = os.path.exists(fileName)

    if ret:
        data = fobj.read()

        print("Data in the file")
        print(data)

    else :
        print("File does not exist")


if __name__ == "__main__":
    main()
# Write a program which accepts file name from user and a string and return the frequency of that string in the file.
# Hello.txt Radha
# Hello my name is Radha = 1
import os

def main():
    fileName = input("Enter the file name: ")
    searchString = input("Enter the string to search: ")

    ret = os.path.exists(fileName)
    if not ret:
        print("File does not exist.")
        return
    else:
        fobj = open(fileName, "r")
        data = fobj.read()

        frequesncy = data.count(searchString)
        print("Frequsncy is:", frequesncy)

        fobj.close()

if __name__ == "__main__":
    main()
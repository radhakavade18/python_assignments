# Write a program which accepts file name from user and check whether that file is exists in current directory or not
# Demo.txt
# Demo.txt exists or not
import os

def main():
    fileName = input("Enter the file name: ")

    ret = os.path.exists(fileName)

    if ret:
        print("File exists")
    else:
        print("File does not exist")
    

if __name__ == "__main__":
    main()
# Write a program which accepts 2 file names from user and compare contents of both files. if its true return succcess else failure
# Hello.txt Demo.txt
# Content is same
import os
import sys

def CheckContent(fileOne, fileTwo):
    ret = os.path.exists(fileOne)
    if not ret:
        print("File does not exist.")
        exit()

    ret = os.path.exists(fileTwo)
    if not ret:
        print("File does not exist.")
        exit()

    fobj1 = open(fileOne, "r")
    fobj2 = open(fileTwo, "r")

    data1 = fobj1.read()
    data2 = fobj2.read()

    if len(data1) == len(data2):
        if data1 == data2:
            print("Content is same")
        else:
            print("Content is different")
    else:
        print("Content is different")

def main():
    Border = '-'*72
    print(Border)
    print("---------------------------- File Copying ---------------------------")
    print(Border)

    if(len(sys.argv) == 3):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to compare contents of two files.")
            print("This is the automation directory script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ....")
            print("ScriptName.py NameOfFirstFile NameOfSecondFile")
            print("Please provide valid absolute path of directory")

        else:
            CheckContent(sys.argv[1], sys.argv[2])
    
    else:
        print("Invalid number of arguments")
        print("Use the given flags as:")
        print("--h or --H : used to display help")
        print("--u or --U : used to display usage")

    print(Border)
    print("----------------------- Thank you for using our script ------------------------")
    print(Border)


if __name__ == "__main__":
    main()
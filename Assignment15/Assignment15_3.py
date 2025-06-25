# Write a program which accepts file name from user and create new file named as Demo.txt and copy all the contents from input file to newly created file
# ABC.txt
# Copy of ABC.txt to Demo.txt
import os
import sys

def CopyFile(FileName):
    fobj = open(FileName, "r")
    ret = os.path.exists(FileName)
    if not ret:
        print("File does not exist.")
        exit()
    else:
        data = fobj.read()
        print("Data in the file:")
        print(data)

        newFobj = open("Demo.txt", "w")
        newFobj.write(data)
        newFobj.close()

def main():
    Border = '-'*72
    print(Border)
    print("---------------------------- File Copying ---------------------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to copy contents from one file to another.")
            print("This is the automation directory script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ....")
            print("ScriptName.py NameOFile")
            print("Please provide valid absolute path of directory")

        else:
            CopyFile(sys.argv[1])
    
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
# Write a python script to count number of lines, words, and characters in a given file

import os
import sys

def Count(fileName):
    ret = os.path.exists(fileName)

    if ret:
        fobj = open(fileName, "r")
        lines = fobj.readlines()
        lineCount = len(lines)
        fobj.close()

        fobj = open(fileName, "r")
        data = fobj.read()
        words = data.split()
        wordCount = len(words)

        characters = len(data)
        print(f"File Name: {fileName}")
        print(f"Number of Lines: {lineCount}")
        print(f"Number of Words: {wordCount}")
        print(f"Number of Characters: {characters}")

        fobj.close()

    else:
        print("File does not exist.")

def main():
    Border = '-'*72
    print(Border)
    print("---------------------------- File Copying ---------------------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to count lines, words and characters from the given file.")
            print("This is the automation directory script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ....")
            print("ScriptName.py NameOfFile")
            print("Please provide valid absolute path of directory")

        else:
            Count(sys.argv[1])
    
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
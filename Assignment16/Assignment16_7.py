# Create Marks.txt with students name and marks. then read the file and display students who scored more than 75 marks

import os

def main():
    fileName = input("Enter file name: ")
    ret = os.path.exists(fileName)
    if ret:
        fobj = open(fileName, "r")
        lines = fobj.readlines()

        for line in lines:
            words = line.split()
            for word in words:
                if word.isnumeric():
                    if int(word) > 75:
                        print(words[0])

        fobj.close()

if __name__ == "__main__":
    main()
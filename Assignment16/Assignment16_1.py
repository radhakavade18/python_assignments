# Write a python program to create a text file named Student.txt and write the name of 5 students into it

def main():
    fileName = input("Enter file name:")
    fobj = open(fileName, "x")
    students = ["Alice", "Bob", "Charlie", "David", "Eve"]

    for student in students:
        fobj.write(student + "\n")

    fobj.close()

if __name__ == "__main__":
    main()
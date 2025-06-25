# Write a python program to read and display the content of a file data.txt

def main():
    fobj = open("data.txt", "r")
    data = fobj.read()
    print("File content:")
    print(data)

    fobj.close()

if __name__ == "__main__":
    main()
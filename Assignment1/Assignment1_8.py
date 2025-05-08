def Display(value):
    for i in range(value):
        print("*")

def main():
    print("Enter a number: ")
    no = int(input())
    Display(no)

if __name__ == "__main__":
    main()
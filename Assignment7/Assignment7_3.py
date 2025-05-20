# Accept list of integer from the user and use filter() function to keep only even.

# Input - 1 2 3 4 5
# Output - 2 4

EvenNumber = lambda no : no % 2 == 0

def main():

    Data = []
    print("Enter numbers")
    for i in range(5):
        Data.append(int(input()))

    fData = list(filter(EvenNumber, Data))
    print("List of even", fData)

if __name__ == "__main__":
    main()
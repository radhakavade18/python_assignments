# Accept list of integer from the user and use map() function to double each value.

# Input - 1 2 3 4 5
# Output - 2 4 6 8 10

DoubleNumber = lambda no : no * 2

def main():

    Data = []
    print("Enter numbers")
    for i in range(5):
        Data.append(int(input()))

    MData = list(map(DoubleNumber, Data))
    print("Doubled list", MData)

if __name__ == "__main__":
    main()
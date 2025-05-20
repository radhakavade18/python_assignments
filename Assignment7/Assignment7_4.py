# Accept list of integer from the user and use reduce() (from functools) function to find the product of all numbers.

# Input - 1 2 3 4 5
# Output - 2 4
from functools import reduce 

FindProduct = lambda no1, no2 : no1 * no2

def main():

    Data = []
    print("Enter numbers")
    for i in range(3):
        Data.append(int(input()))

    fData = reduce(FindProduct, Data)
    print("List of even", fData)

if __name__ == "__main__":
    main()
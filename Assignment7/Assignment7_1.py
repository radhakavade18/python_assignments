# Write two lambda functions
# One to calculate square of number
# Another to calculate qube of number

# Input - 3
# Output - Square - 9, Qube - 27

Square = lambda value: value * value

Qube = lambda value: value ** value

def main():
    print("Enter number")
    no = int(input())

    ret = Square(no)
    print("Square is:", ret)

    ret = Qube(no)
    print("Qube is:", ret)

if __name__ == "__main__":
    main()
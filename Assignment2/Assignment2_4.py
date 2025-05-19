# write a program which accepts number from user and return addition of its factors
#Input- 12, O/p - 16 (1+2+3+4+6)

def Factor(no):
    sum = 0
    for i in range(1, no):
        if (no % i == 0):
            sum += i
    return sum

def main():
    print("Enter number")
    value = int(input())

    res= Factor(value)
    print("Additon of factors is :", res)

if __name__ == "__main__":
    main()
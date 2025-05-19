# write a program which accepts number from user and return addition of its digits 
# Ex: 23535 o/p - 18

def CalculateSum(no):
    sum = 0
    while (no != 0):
        sum = sum + (no % 10)
        no //=10
    return sum
        
def main():
    print("Enter number")
    value = int(input())

    ret = CalculateSum(value)
    print("Sum of digits is ", ret)

if __name__ == "__main__":
    main()
# Factorial using recursion

fact = 1
def Factorial(no):
    global fact
    if(no >= 1):
        fact = fact * no
        no = no - 1
        Factorial(no)

    return fact

def main():
    print("Enter number")
    no = int(input())
    
    ret = Factorial(no)
    print("Factorials are:", ret)

if __name__ == "__main__":
    main()
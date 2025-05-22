# Write a python program uses multiprocessing.Pool to compute factorial of numbers in a list

import multiprocessing

def Factorial(value):
    fact = 1
    while(value > 0):
        fact = value * fact
        value -= 1
    return fact

def main():
    Data = [2, 4, 5, 10, 6, 8]

    p = multiprocessing.Pool()

    result = p.map(Factorial, Data)
    p.close()
    p.join()

    print("result",result)

    print("Exit main")

if __name__ == "__main__":
    main()
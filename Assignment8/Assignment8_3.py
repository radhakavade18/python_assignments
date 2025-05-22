# Design python application which creates 2 threads as evenlist and oddlist. Both the threads accepts 1 parameters as interger. evenlist thread will add all even elements from input list and oddlist will add all odd elements from input list and display the additon

import threading

def EvenList(value):
    sum = 0
    for i in value:
        if i % 2 == 0:
            sum = sum + i

    print(sum)

def OddList(value):
    sum = 0
    for i in value:
        if i % 2 != 0:
            sum = sum + i

    print(sum)

def main():
    print("Enter size")
    size = int(input())

    Data = []
    print("enter elements")
    for i in range(size):
        Data.append(int(input()))

    T1 = threading.Thread(target = EvenList, args=(Data,))
    T2 = threading.Thread(target = OddList, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()
    print("Exit from main")

if __name__ == "__main__":
    main()
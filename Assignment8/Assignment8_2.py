# Design python application which creates 2 threads as evenfactor and odd factor. Both the threads accepts 1 parameters as interger. Evenfactor thread will display addition of even factors of given number and oddfactor will display addition of odd factors of given numbers. After execution of both the threads gets completed main thread should display msg as "exit from main"
import threading

def EvenFactor(value):
    sum = 0
    for i in range(2, int(value/2)+1):
        if value % i == 0:
            sum = sum + i

    print(sum)

def OddFactor(value):
    sum = 0
    for i in range(2, int(value/2)+1):
        if value % i != 0:
            sum = sum + i

    print(sum)

def main():
    print("Enter number")
    no = int(input())

    T1 = threading.Thread(target = EvenFactor, args=(no,))
    T2 = threading.Thread(target = OddFactor, args=(no,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()
    print("Exit from main")

if __name__ == "__main__":
    main()
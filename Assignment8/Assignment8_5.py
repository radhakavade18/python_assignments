# Design python application which creates 2 threads as evenlist and oddlist. Both the threads accepts 1 parameters as interger. evenlist thread will add all even elements from input list and oddlist will add all odd elements from input list and display the additon

import threading

def DisplayNumber1(event):
    for i in range(1, 50):
        print(i)
    event.set()

def DisplayNumber2(event):
    event.wait()
    for i in range(50, 0, -1):
        print(i)

def main():
    event = threading.Event()

    T1 = threading.Thread(target = DisplayNumber1,args=(event,))
    T2 = threading.Thread(target = DisplayNumber2,args=(event,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
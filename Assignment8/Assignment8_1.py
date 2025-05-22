# Design python application which creates 2 threads named as even and odd. Even thread will display first 10 even numbers and odd thread will display 1st 10 odd numbers
import threading

def DisplayEven():
    i = 0
    count = 0

    while i < 10:
        if count % 2 == 0:
            i = i + 1
            print(count)
        count += 1

def DisplayOdd():
    i = 0
    count = 0

    while i < 10:
        if count % 2 != 0:
            i = i + 1
            print(count)
        count += 1

def main():
    T1 = threading.Thread(target = DisplayEven)
    T2 = threading.Thread(target = DisplayOdd)

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
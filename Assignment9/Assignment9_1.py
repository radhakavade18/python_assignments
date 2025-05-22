# Create a python program that starts 3 threads, each printing numbers from 1 to 5 with delay of 1 sec. Use threading.Thread
import threading
import time

def DisplayNum(delay):
    time.sleep(delay)
    for i in range(1, 6):
        print(i)

def main():
    thread1 = threading.Thread(target=DisplayNum, args=(0,))
    thread2 = threading.Thread(target=DisplayNum, args=(1,))
    thread3 = threading.Thread(target=DisplayNum, args=(2,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("Exit main")

if __name__ == "__main__":
    main()
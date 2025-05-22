# Write a python program that compares execution time of summing numbers from 1 to 10 million using normal function, threading and multiprocessing

import multiprocessing
import time

def Addition(value):
    sum = 0
    for i in range(1, value+1):
        sum = sum + i

    print("Addition is:", sum)

def main():
    no = 1000000
    start_time = time.time()

    P = multiprocessing.Process(target=Addition, args=(no,))
    P.start()
    P.join()

    end_time = time.time()
    print("Time required to complete the process is:", end_time - start_time)
    print("Exit main")

if __name__ == "__main__":
    main()
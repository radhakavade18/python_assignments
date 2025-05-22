# Write a python program using multiprocessing.Process to square a list of numbers using multiple processes

import multiprocessing

def SquareNumber(no):
    print(no * no)

def main():
    Data = [2, 4, 5,10, 46, 8]

    for i in Data:
        ProcessX = multiprocessing.Process(target = SquareNumber, args=(i,))
        ProcessX.start()
        ProcessX.join()

    print("Exit main")

if __name__ == "__main__":
    main()
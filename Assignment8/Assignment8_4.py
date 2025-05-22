# Design python application which creates 3 threads as small, capital, digits. All the threads accept string as parameter. small thread will display number of small characters, capital thread display number of capital characters and digit thread will display number of digits. Display id and name of each thread

import threading

def SmallChar(value):
    print("Thread ID: ", threading.get_ident())
    print("Theread name:", threading.current_thread().name)
    count = 0
    for i in value:
        if (i >= 'a' and i <= 'z'):
            count += 1
    
    print("Small character count is:",count)

def CapitalChar(value):
    print("Thread ID: ", threading.get_ident())
    print("Theread name:", threading.current_thread().name)
    count = 0
    for i in value:
        if i >= 'A' and i <= 'Z':
            count += 1
    
    print("Capital character count is:",count)

def Digits(value):
    print("Thread ID: ", threading.get_ident())
    print("Theread name:", threading.current_thread().name)
    count = 0
    for i in value:
        if i >= '0' and i <= '9':
            count += 1
    
    print("Digits character count is:",count)

def main():
    print("Enter string which contains small, capital and digits in it")
    value = input()

    T1 = threading.Thread(target = SmallChar, args=(value,))
    T2 = threading.Thread(target = CapitalChar, args=(value,))
    T3 = threading.Thread(target = Digits, args=(value,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()
    print("Exit from main")

if __name__ == "__main__":
    main()
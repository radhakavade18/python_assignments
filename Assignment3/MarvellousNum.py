def ChkPrime(value):
    isPrime = True

    for i in range(2, int(value/2)+1):
        if (value % i == 0):
            isPrime = False
    return isPrime
class Numbers():

    def __init__(self, A):
        self.Value = A
    
    def CheckPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def CheckFactor(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        return factors

    def SumFactors(self):
        factors = self.CheckFactor()
        return sum(factors)
    

    def CheckPerfect(self):
        return self.SumFactors() == self.Value


def main():
    print("Enter a number:")
    no = int(input())
    
    obj = Numbers(no)
    
    if obj.CheckPrime():
        print(f"{no} is a prime number.")
    else:
        print(f"{no} is not a prime number.")
    
    factors = obj.CheckFactor()
    print(f"Factors of {no}: {factors}")
    
    sum_factors = obj.SumFactors()
    print(f"Sum of factors of {no}: {sum_factors}")
    
    if obj.CheckPerfect():
        print(f"{no} is a perfect number.")
    else:
        print(f"{no} is not a perfect number.")

if __name__ == "__main__":
    main()

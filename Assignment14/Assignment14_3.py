# Create a class Book with private attribute __price. Add member to get and set the price. Show Encapsulation

class Book:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price cannot be negative.")

def main():
    bobj = Book(100)
    print("Initial Price:", bobj.get_price())
    bobj.set_price(150)

if __name__ == "__main__":
    main()
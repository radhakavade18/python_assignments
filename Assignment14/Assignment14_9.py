# Create a base class Product with name and price. Implement __eq__ method to compare products based on price.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if (self.price == other.price):
            print("Products price is similar")

        else:
            print("Products price is different")

def main():
    obj1 = Product("Laptop", 1000)
    obj2 = Product("Smartphone", 800)
    obj3 = Product("Laptop", 1000)

    obj1.__eq__(obj2)
    obj1.__eq__(obj3)

if __name__ == "__main__":
    main()
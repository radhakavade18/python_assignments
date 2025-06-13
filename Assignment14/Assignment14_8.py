# Create a base class Person with name and age. Derive a class teacher with subject and salary. use Super() to call base class constructor and print both

class Vehicle:
    def __init__(self):
        print("Vehicle class initialized")

    def Start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def Start(self):
        super().Start()
        print("Car is starting")

def main():
    cobj = Car()
    cobj.Start()

if __name__ == "__main__":
    main()
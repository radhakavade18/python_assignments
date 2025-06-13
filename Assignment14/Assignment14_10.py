# Demonstrate private, protected and public access modifiers using a class Employee with attributes: __salary, _department, and name.

class Employee:
    def __init__(self, salary, department, name):
        self.__salary = salary
        self._department = department
        self.name = name

class Demo(Employee):
    def __init__(self, salary, department, name):
        super().__init__(salary, department, name)

    def display(self):
        print("Name:",self.name "Department:", self._department "Salary:", self.__salary)

def main():
    obj = Demo(50000, "IT", "John Doe")
    obj.display()

if __name__ == "__main__":
    main()
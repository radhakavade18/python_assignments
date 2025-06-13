# Create a base class Person with name and age. Derive a class teacher with subject and salary. use Super() to call base class constructor and print both

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}, Salary: {self.salary}")

def main():
    t1 = Teacher("John Doe", 30, "Mathematics", 50000)
    t1.display_details()

    t2 = Teacher("Radha", 35, "Science", 60000)
    t2.display_details()

if __name__ == "__main__":
    main()
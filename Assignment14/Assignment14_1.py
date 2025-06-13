# Create a class Employee with attribute name, emp_id, and salary. Create Objects of this class and print their details

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Employee ID: {self.emp_id}, Salary: {self.salary}")

def main():
    eobj = Employee("John Doe", 123, 50000)
    eobj.display_details()

    eobj = Employee("Radha", 456, 200000)
    eobj.display_details()

if __name__ == "__main__":
    main()
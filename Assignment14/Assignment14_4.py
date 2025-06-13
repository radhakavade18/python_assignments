# Create a class Student with name and roll number. change school name using class name

class Student:
    school_name = "ABC High School"

    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def StudentDetails(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, School: {Student.school_name}"

def main():
    sobj = Student("John Doe", 101)
    print(sobj.StudentDetails())
    sobj = Student("Radha", 102)
    print(sobj.StudentDetails())

    Student.school_name = "XYZ High School"
    sobj = Student("John Doe", 101)
    print(sobj.StudentDetails())

if __name__ == "__main__":
    main()
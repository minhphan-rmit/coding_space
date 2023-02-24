class Student:

    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def get_info(self):
        print(f"Name: {self.name}, Age: {self.age}, GPA: {self.gpa}")

    def get_name(self):
        print(f"Name: {self.name}")

    def get_age(self):
        print(f"Age: {self.age}")

    def get_gpa(self):
        print(f"GPA: {self.gpa}")

    def set_age(self, n_age):
        self.age = n_age

    def set_name(self, n_name):
        self.name = n_name

    def set_gpa(self, n_gpa):
        self.gpa = n_gpa


# test cases
s_name = input('Student name: ')
s_age = int(input('Student age: '))
s_gpa = float(input('Student GPA: '))
stud = Student(s_name, s_age, s_gpa)
stud.get_info()
stud.get_name()
s_gpa_new = float(input('New GPA'))
stud.set_gpa(s_gpa_new)
stud.get_info()
s_name_new = input('New student name: ')
stud.set_name(s_name_new)
stud.get_info()


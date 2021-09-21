class Student:
    def __init__(self, name):
        self.name = name
        self.grades = (90, 90, 93, 78, 90)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob")

# Two ways of calling the same function
print(Student.average_grade(student))
print(student.average_grade())
print(student.name)
print(student.grades)

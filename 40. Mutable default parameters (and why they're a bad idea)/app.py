from typing import List, Optional


class Student:
    # Never make a parameter equal to a mutable field like LIST
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("bob")
rolf = Student("rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)

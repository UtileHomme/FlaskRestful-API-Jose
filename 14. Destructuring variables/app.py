# Another way to define a tuple
t = 5, 11

# Assigning values from tuple to different variables
x, y = t

# Dictionary
student_attendance = {"Rolf": 96, "Jatin": 23}

print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print({student : attendance})

# List of tuples
student_attendance = [("Rolf", 96), ("Jatin", 23)]

for student in student_attendance:
    print(f" Name: {student[0]}, Attendance: {student[1]}")

person = ("Jatin", 42, "Mechanic")

# Underscore variable will take a value but might not be used. Good for skipping values during assignment
name, _, profession = person

# for printing the first value, and printing the list of rest of the values
head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)

*head, tail = [1, 2, 3, 4, 5]

print(head)
print(tail)\

# for printing the starting values without list, and the last value separately
*head, tail = [1, 2, 3, 4, 5]

print(*head)
print(tail)














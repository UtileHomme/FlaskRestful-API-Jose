friend_ages = {"Rolf": 24, "Adam": 27, "Anne": 30}

friend_ages["Bob"] = 20

print(friend_ages)

# List of Dictionaries
friends = [
    {"name": "Rolf", "age": 20},
    {"name": "Adam", "age": 20},
    {"name": "Anne", "age": 20},
]

print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Jatin": 23}

# First way of accessing the data
for student in student_attendance:
    print(f"{student} : {student_attendance[student]}")

# Better way of accessing the data
for student, attendance in student_attendance.items():
    print(f"{student} : {student_attendance[student]}")

if "Jatin" in student_attendance:
    print(f"Jatin: {student_attendance['Jatin']}")
else:
    print("Jatin is not a student in this class")

attendance_values = student_attendance.values();

print(sum(attendance_values) / len(attendance_values))

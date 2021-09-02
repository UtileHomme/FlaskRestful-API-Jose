numbers = [1, 3, 5]

# new way to double the numbers
doubled = [x * 2 for x in numbers]
print(doubled)

friends = ["Rolf", "Jatin", "Sam", "Sarah"]

# To include names of friends whose name starts with S
start_s = [friend for friend in friends if friend.startswith("S")]
print(start_s)









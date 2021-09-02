name = input("Enter your name : ")
print(name)

size_input = input("how big is your house (in square feet:)")

square_feet = int(size_input)

square_metres = square_feet/ 10.8

# .2f for floating point result upto 2 digits
print(f"{square_feet} square feet is {square_metres:.2f} square metres.")

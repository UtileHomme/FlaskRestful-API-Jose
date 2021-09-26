a = []
b = a

a.append(35)

print(a)
print(b)

# id gives location of the variable in memory
print(id(a))
print(id(b))

# Lists are mutable

# Tupes are immutable

a = ()
# a = a + 15

# integers are also immutable

a = 8597
b = 8597

# a and b above point to the same location

a = "hello"
b = a

a += "world"
print(a + "    " + b)
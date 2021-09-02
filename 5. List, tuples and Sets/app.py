# lists can be modified
l = ["Bob", "Rolf", "Anne"]

# tuple can't be modified
t = ("Bob", "Rolf", "Anne")

# Sets don't have duplicate elements, Order of elements could change any moment
s = {"Bob", "Rolf", "Anne"}

# can be used on lists or tuples
print(l[0])

# use append to add elements to a list
l.append("Smith")
print(l)

# removing elements from list
l.remove("Bob")

# adding elements to a set
s.add("Anna")

print(s)

print(5==5)

friends = ["Rolf" , "Bob"]
abroad = ["Rolf" , "Bob"]

print(friends == abroad)

# this will give false. Both lists were created in different memory locations despite having the same value, hence false
print(friends is abroad)

local = friends;
# this will give true because we didn't explicitly create a list in the memory
print(local is friends)
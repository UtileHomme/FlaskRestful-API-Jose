friends = {"Bob" , "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

total_friends = friends.union(abroad)
print(total_friends)

both = friends.intersection(abroad)
print(both)
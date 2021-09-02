# Basic definition of a function
def hello():
    print("Hello")


hello()


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_in_seconds = user_age * 24 * 60 * 60
    print(f"Your age in seconds is {age_in_seconds}")


user_age_in_seconds()

# friends = ["rolf", "jatin"]

# def add_friend():
#     friend_name = input("Enter your friend name:")
#     # won't work
#     f = friends + [friend_name]
#
#
# add_friend()


def add_friends():
    friends.append("Jatin")

friends = []
add_friends()


print(friends)
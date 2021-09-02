movies_Watched = {"The Matrix", "Green book", "Her"}
user_movie = input("Enter what you have watched : ")

if user_movie in movies_Watched:
    print(f"I have watched {user_movie} too.")
else:
    print(f"I haven't watched it yet.")

number = 7
user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guesses correctly")
    elif abs(number - user_number) == 1:
        print("You wer off by one")
    else:
        print("Sorry, it's wrong")

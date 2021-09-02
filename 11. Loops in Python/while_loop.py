number = 7
user_input = input("Would you would like to play? (Y/n) ")

while user_input != "n":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guesses correctly")
    elif abs(number - user_number) == 1:
        print("You wer off by one")
    else:
        print("Sorry, it's wrong")

    user_input = input("Would you would like to play? (Y/n) ")

#     Second way of ending the loop is described below:

while True:

    user_input = input("Would you would like to play? (Y/n) ")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guesses correctly")
    elif abs(number - user_number) == 1:
        print("You wer off by one")
    else:
        print("Sorry, it's wrong")

    user_input = input("Would you would like to play? (Y/n) ")

import random

print("************************************")
print("Welcome to the Number Guessing Game!")
print("************************************")

random_number = None
guess = None
number_of_guess = 5


def create_random_number():
    return random.randint(1, 100)


def set_random_number():
    global random_number
    random_number = create_random_number()


def take_guess():

    global guess, number_of_guess

    if number_of_guess < 1:
        print("Oops! out of moves")
        try:
            if input("do you want to play again? Y or N : ").upper() == "Y":
                start_game()
            else:
                print("Thank You for playing!")
                return
        except KeyboardInterrupt:
            print("\nSee you again!")
            return

    try:
        guess = int(input(f"What is your guess? you have {number_of_guess} left : "))

        if 1 < guess > 100:
            print("Input a number between 1 and 100")
            take_guess()

    except ValueError:
        print("Oops invalid type of input! number was expected...")
        take_guess()
    except KeyboardInterrupt:
        print("\nSee you again!")
        return

    number_of_guess -= 1
    validate_guess()


def validate_guess():
    global random_number, guess

    if guess == random_number:
        print("You got it right! The number was {}".format(random_number))

        try:
            if input("do you want to play more? Y or N : ").upper() == "Y":
                start_game()
            else:
                print("Thank You for playing!")
                return
        except KeyboardInterrupt:
            print("\nSee you again!")
            return

    elif guess > random_number:
        print("Your guess is greater then the number! try again")
        take_guess()
    else:
        print("Your guess is lower then the number! try again")
        take_guess()


def start_game():
    global random_number, guess

    set_random_number()
    print("Take a guess between 1 and 100")
    take_guess()


start_game()

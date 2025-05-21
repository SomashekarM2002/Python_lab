import random
def number_guessing_game():
    number_guess=random.randint(1,100)
    attempts=0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess=int(input("Guess a number between 1 and 100: "))
            attempts +=1

            if guess < number_guess:
                print("Your guess is too low.")
            elif guess > number_guess:
                print("Your guess is too high.")
            else:
                print("correct!you guessed it right{attempts}.")
                break
        except ValueError:
            print("please enter a valid number.")

if __name__ == '__main__':
    number_guessing_game()
import random
import sys

guesses_left = 10
random_number = random.randint(1, 100)

def main():
    global guesses_left
    while True:
        try:
            guessed_number = int(input("What do you think the secret number is? "))

            if bigger_or_smaller(guessed_number, random_number) != None:
                print(bigger_or_smaller(guessed_number, random_number))
            if win_check(guessed_number, random_number) != False:
                play_again()
            print(guesses_reduce(guesses_left))

        except ValueError:
            print("Please enter an integer for your guess as to what the winning number might be.")

def guesses_reduce(guesses_remaining):
    global guesses_left
    guesses_remaining -= 1
    guesses_left = guesses_remaining

    return(f"You have {guesses_left} chances to guess the correct number or you lose.")


def bigger_or_smaller(n: int, random_num):
    if n > random_num:
        return(f"The secret number is smaller than {n}.")
    elif n < random_num:
        return(f"The secret number is bigger than {n}.")
    else:
        return None # code will not allow it to be printed and will skip to win check



def win_check(n, random_num):
    global guesses_left

    if n == random_num:
        print(f"You have guessed the secret, hidden number: {random_num}! You win!")
    elif guesses_left == 1:
        print(f"You ran out of guesses and lost the game. You did not guess the correct number: {random_num}.")
    else:
        return False

def play_again():
    global guesses_left
    global random_number

    while True:
        again = input("Would you like to play again? Yes - y, No - n. ").lower().strip()

        if again == "y":
            guesses_left = 11
            random_number = random.randint(1, 100)
            return True
        elif again == "n":
            sys.exit("Thank you for playing Dhanika Botejue's Number Guessing 100! Play again soon!")


if __name__ == "__main__":
    main()

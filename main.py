import random

from past.builtins import raw_input


def guessNumber(number, user_guess):
    headtail = [0,0] #first heads, then tails
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            headtail[1] += 1
        else:
            headtail[0] += 1
    return headtail

if __name__ == "__main__":
    playing = True
    number = str(random.randint(0,99999))

    guesses = 0

    print("Let's play a game of Heads n Tail!")
    print("I will generate a number, and you have to guess the numbers one number at a time!")
    print("Rules: Your number must be a 5-digit number!")
    print("The game ends when you get 5 Heads!")
    print("\n")

    while playing:
        user_guess = raw_input("Give me your best guess!")
        if user_guess == "exit":
            break
        headstailscount = guessNumber(number, user_guess)
        guesses += 1

        print("You have" + str(headstailscount[0]) + "Tails and" + str(headstailscount[1]) + "Heads")

        if headstailscount[1] == 5:
            playing = False
            print("You win the game after" + str(guesses) + "The number was" + str(number))
            break #exit

        else:
            print("Your guess is not right, try again")

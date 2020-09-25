#####################################################
# Word Guess Chat bot
# Author: Timothy Kung
# Date: September 24, 2020
# Description: A chat bot that plays guess the word.
#####################################################
import random
import words as words

game_list = []
guessed_list = []
num_guesses = 5

# program picks random word from pre-made list // ensures no duplicates in game list
def generate_list(array, rounds):
    while len(array) < rounds:
        for x in range(0, rounds):
            new_word = random.choice(words.word_list)
            if new_word not in array:
                array.append(new_word)
            else:
                pass
    return array, rounds

# Generates blank
def gets_reveal():
    result = "_" * len(list((game_list[0])))
    return result


# program asks 1 player or 2 players
print("Hey there! I'm Hangman bot. I can set up a game for you!\n"
      "Type 'play' if you want to play!")

game_type = input()

# if 1 player: set up one player game
while True:
    if game_type == 'play':
        while True:
            # asks number of rounds player would like to play
            num_rounds = input("How many rounds would you like to play?\n")
            try:
                num_rounds = int(num_rounds)
            except ValueError or TypeError:
                print("Please type in a valid number for me.")
            else:
                # if round number < 5 and number > 0: set round
                if 0 < num_rounds < 6:
                    break
                else:
                    print("Please choose a number between 1 and 5 for me.")
        break

generate_list(game_list, num_rounds)

reveal = gets_reveal()
print(game_list)

# Game loop while blanks or until out of guesses
while True:
    # checks if user is out of guesses
    if num_guesses == 0:
        print("You're out of guesses!\n"
              "Too bad, try your luck next time.")
        break

    # checks if word is already solved or not
    if "_" not in reveal:

        # clear guessed list and goes to next round
        del guessed_list[:]
        print("Nice going! You win this round!")
        num_rounds -= 1

        # checks if there is a next round
        if num_rounds >= 0:
            game_list.pop(0)
            print("You're onto the next round!\n")
            reveal = gets_reveal()

    if num_rounds == 0:
        print("Thanks for playing a game with me!")
        break

    user_guess = input(f"Guess my secret word or a letter in my secret word: {reveal}\n")

    if user_guess not in guessed_list:
        if len(user_guess) == 1 and user_guess in game_list[0]:
            guessed_list.append(user_guess)
            print("You got it!")
            reveal = ["_" if i not in guessed_list else i for i in list(game_list[0])]

        elif user_guess == game_list[0]:
            del guessed_list[:]
            print("Nice going! You win this round!")
            num_rounds -= 1

            if num_rounds > 0:
                game_list.pop(0)
                print("You're onto the next round!\n")
                reveal = gets_reveal()

        elif user_guess in guessed_list:
            print("You've already guessed that letter/word!")
            num_guesses -= 1

        else:
            print("That's not a letter in the word. Try again!")
            guessed_list.append(user_guess)
            num_guesses -= 1

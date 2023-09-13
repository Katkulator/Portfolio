import random


def pick_word():
    words = ["majmun", "krastavac", "traktor",
             "cigara", "pas", "bunar", "plug"]
    return random.choice(words)


def update_missing(target_word, guesser, letter):
    for i in range(len(target_word)):
        if target_word[i] == letter:
            guesser[i] = letter


def play_game():
    target_word = pick_word()
    guesser = ["_"] * len(target_word)
    max_guesses = 6
    guessed_letters = []

    print("Welcome to the Guessing Game!")
    print("Pick one letter at a time")
    print(f"You have a maximum of {max_guesses} guesses\n")

    while max_guesses > 0:
        print(f"Try to guess the word: {guesser}")
        letter = input("Pick one letter:").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter just one letter\n")
        elif letter in guessed_letters:
            print("You already tryed that letter\n")
            continue
        else:
            guessed_letters.append(letter)

        if letter in target_word:
            update_missing(target_word, guesser, letter)
            if "_" not in guesser:
                print(f"Congrats, you've guessed the word: {target_word}")
                break
            else:
                print("Correct guess!")
        else:
            max_guesses -= 1
            print(f"Wrong! Guess again!\n You have {max_guesses} guesses left")

    if max_guesses == 0:
        print(f"You've run out of guesses. The word is: {target_word}")

    play_again = input("Do you want to play again? y/n:")
    if play_again == "y":
        play_game()
    else:
        print("Thank you for playing")


play_game()

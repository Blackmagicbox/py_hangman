def print_lives(strikes):
    display = ""
    print("Strikes left: ")
    for strike in range(strikes):
        display += '|'
    print(display)


def main():
    print(chr(27) + "[2J")  # clear the screen every round
    strikes = 10
    right_guesses = 0
    word = 'TERMINATOR'
    guessed_letter = input("Guess a letter: ")
    display = ['_'] * len(word)

    while guessed_letter != "quit" and strikes > 0:
        print(chr(27) + "[2J")  # clear the screen every round
        print("Guesses left: ")
        print_lives(strikes)

        if guessed_letter in word:
            print("Correct guess")
            for index, letter in enumerate(word):
                if letter == guessed_letter:
                    display[index] = letter
                    right_guesses += 1
        else:
            strikes -= 1
            print("Wrong guess")
        print(" ".join(display))  # Print current state of the word
        if right_guesses == len(word):
            break
        guessed_letter = input("Guess a letter: ")

    print(chr(27) + "[2J")  # clear the screen every round
    print("Guesses left: ")
    print_lives(strikes)
    print(" ".join(display))  # Print current state of the word

    if strikes <= 0:
        print("You loose")
    else:
        print("Congratulations you won!")

    print("Done!")


main()

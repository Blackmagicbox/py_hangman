import curses


def print_lives(stdscr, strikes):
    display = ""
    stdscr.addstr("Strikes left: \n")
    for strike in range(strikes):
        display += '|'
    stdscr.addstr(display + "\n")


def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    try:
        strikes = 10
        right_guesses = 0
        word = 'TERMINATOR'
        stdscr.addstr("Guess a letter: ")
        stdscr.refresh()
        guessed_letter = stdscr.getkey()

        display = ['_'] * len(word)

        while guessed_letter != "quit" and strikes > 0:
            stdscr.clear()
            stdscr.addstr("Guesses left: \n")
            print_lives(stdscr, strikes)

            if guessed_letter in word:
                stdscr.addstr("Correct guess\n")
                for index, letter in enumerate(word):
                    if letter == guessed_letter:
                        display[index] = letter
                        right_guesses += 1
            else:
                strikes -= 1
                stdscr.addstr("Wrong guess\n")
            stdscr.addstr(" ".join(display) + "\n")  # Print current state of the word
            if right_guesses == len(word):
                break
            stdscr.addstr("Guess a letter: ")
            stdscr.refresh()
            guessed_letter = stdscr.getkey()

        stdscr.clear()
        stdscr.addstr("Guesses left: \n")
        print_lives(stdscr, strikes)
        stdscr.addstr(" ".join(display) + "\n")  # Print current state of the word

        if strikes <= 0:
            stdscr.addstr("You loose\n")
        else:
            stdscr.addstr("Congratulations you won!\n")

        stdscr.addstr("Press any key to exit...\n")
        stdscr.refresh()
        stdscr.getkey()  # Wait for a keypress
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()


main()

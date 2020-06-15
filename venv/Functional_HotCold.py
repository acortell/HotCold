import random
import math

LETTERS = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',\
          'w', 'x', 'y', 'z', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao',\
          'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax', 'ay', 'az'


def valid_input(prompt):
    while True:
        string = input(prompt).lower()
        x = ''
        y = ''
        mode = 1
        for char in string:
            if mode == 1:
                if char.isnumeric():
                    x += char
                    mode = 2
            elif mode == 2:
                if char.isnumeric():
                    x += char
                else:
                    if char.isalpha():
                        y += char
                    mode = 3
            elif mode == 3:
                if char.isalpha():
                    y += char
        if x and y:
            return x, y
        else:
            print("Sorry, I didn't understand that.")


def pick_spot(x, y):
    a = random.randint(1, int(x))
    b = LETTERS[random.randint(0, LETTERS.index(y))]
    return a, b


def evaluate(a, b, guess_x, guess_y):
    # Find x distance
    xdist = abs(a - int(guess_x))
    # Find y distance
    ydist = abs(LETTERS.index(b) - LETTERS.index(guess_y))
    # Find total distance
    tdist = math.sqrt(xdist ** 2 + ydist ** 2)
    # assign a response
    if tdist > 10:
        print("Extremely cold!")
    elif tdist > 8:
        print("Cold.")
    elif tdist > 6:
        print("Warm.")
    elif tdist > 4:
        print("Hot.")
    elif tdist > 2:
        print("Extremely hot!")
    else:
        print("YOU'RE ON FIRE!")


def play(x, y):
    a, b = pick_spot(x, y)
    guesses = 0
    while True:
        guess_x, guess_y = valid_input("Guess a location!")
        guesses += 1
        if a == int(guess_x) and b == guess_y:
            print(f"Congratulations, you guessed the spot in {guesses} guesses.")
            break
        else:
            evaluate(a, b, guess_x, guess_y)


def main():
    print("""Welcome to hide and seek or whatever this is.
Each turn you'll guess a location on a board, designated by a number-letter pair. For example, 2h.
The computer will tell you whether you're hot or cold and let you guess again.
Find the spot in as few turns as possible for a high score!""")
    x, y = valid_input("Set the board size by giving the coordinates of the farthest point.")
    play(x, y)
    while True:
        again = input("Would you like to play again? Enter yes or no.").lower()
        if again == 'yes':
            x, y = valid_input("Set the board size by giving the coordinates of the farthest point.")
            play(x, y)
        elif again == 'no':
            break
        else:
            print("Sorry, I didn't understand that.")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()

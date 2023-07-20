import random
from random import randint  # Do not delete this line


def displayIntro():
    print("_______________________________________________")
    print(" _                                             ")
    print("| |                                            ")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                    __/ |                      ")
    print("                   |___/                       ")
    print("_______________________________________________")
    print("_____________________Rules_____________________")
    print("Try to guess the hidden word one letter at a   ")
    print("time. The number of dashes are equivalent to ")
    print("the number of letters in the word. If a player ")
    print("suggests a letter that occurs in the word,    ")
    print("blank places containing this character will be ")
    print("filled with that letter. If the word does not  ")
    print("contain the suggested letter, one new element  ")
    print("of a hangman’s gallow is painted. As the game  ")
    print("progresses, a segment of a victim is added for ")
    print("every suggested letter not in the word. Goal is")
    print("to guess the word before the man hangs!  ")
    print("_______________________________________________")


def displayEnd(result):
    if result == True:
        print("________________________________________________________________________")
        print("          _                                  _                          ")
        print("         (_)                                (_)                         ")
        print("__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    ")
        print("\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   ")
        print(" \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      ")
        print("  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      ")
        print("           | |   (_)    | |                  | (_)                      ")
        print("        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ ")
        print("       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|")
        print("      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   ")
        print("       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   ")
        print("________________________________________________________________________")
    elif result == False:
        print(" __     __           _           _   _                                    ")
        print(" \ \   / /          | |         | | | |                                   ")
        print("  \ \_/ /__  _   _  | | ___  ___| |_| |                                   ")
        print("   \   / _ \| | | | | |/ _ \/ __| __| |                                   ")
        print("    | | (_) | |_| | | | (_) \__ \ |_|_|                                   ")
        print("    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   ")
        print("        _______ _                                        _ _          _ _ ")
        print("       |__   __| |                                      | (_)        | | |")
        print("          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |")
        print("          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |")
        print("          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|")
        print("          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)")
        print("__________________________________________________________________________")


def displayHangman(state):
    if state == 5:
        print("     ._______.   ")
        print("     |/          ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print(" ____|___        ")
        print("")
        print("")


    elif state == 4:
        print("     ._______.   ")
        print("     |/      |   ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print(" ____|___        ")
        print("")
        print("")

    elif state == 3:
        print("     ._______.   ")
        print("     |/      |   ")
        print("     |      (_)  ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print("     |           ")
        print(" ____|___        ")
        print("")
        print("")

    elif state == 2:
        print("     ._______.   ")
        print("     |/      |   ")
        print("     |      (_)  ")
        print("     |       |   ")
        print("     |       |   ")
        print("     |           ")
        print("     |           ")
        print(" ____|___        ")
        print("")
        print("")

    elif state == 1:
        print("     ._______.   ")
        print("     |/      |   ")
        print("     |      (_)  ")
        print("     |      \|/  ")
        print("     |       |   ")
        print("     |           ")
        print("     |           ")
        print(" ____|___        ")
        print("")
        print("")

    else:
        print("     ._______.   ")
        print("     |/      |   ")
        print("     |      (_)  ")
        print("     |      \|/  ")
        print("     |       |   ")
        print("     |      / \  ")
        print("     |           ")
        print(" ____|___        ")


def getWord():
    lst = open("hangman-words.txt").readlines()
    word = lst[random.randint(1, len(lst) - 1)]
    print(word)
    return word.replace("\n", "")


def valid(c):
    if c.isalpha() and c.islower() and len(c) == 1:
        return True
    else:
        return False


def play():
    displayHangman(5)
    word = getWord()
    print("Guess the word: " + ('_' * len(word)))
    guesses = []
    s = ""
    for i in range(5, 0, -1):
        entered_letter = input("\nEnter the letter: \n")
        while not valid(entered_letter):
            entered_letter = input("\nEnter a valid lowercase letter: \n")
        if entered_letter in word:
            guesses.append(entered_letter)
            displayHangman(i)
            s = "Guess the word: "
            for j in word:
                if not j in guesses:
                    s += "_"
                else:
                    s += j
            print(s)
            nums = 0
            for j in word:
                if j in guesses:
                    nums += 1
            if nums == len(word):
                break

        else:
            displayHangman(i - 1)
            if s == "":
                print("Guess the word: " + ('_' * len(word)))
            else:
                print(s)

    nums = 0
    for j in word:
        if j in guesses:
                nums += 1
        if nums == len(word):
            return True
    else:
        print("Hidden word was " + word)
        return False


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        user_input = input("Do you want to play again? (yes/no)")
        if user_input == "yes":
            continue
        else:
            break


if __name__ == "__main__":
    hangman()


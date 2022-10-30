from typing import List
import string
import random


def generate_grid() -> List[str]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. ['i', 'e', 'a', 'd', 'c', 'b', 'g', 'a', 'k']
    """
    board = random.choices(string.ascii_lowercase, k=9)
    return board


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    acceptable_words = []
    with open(f, 'r') as file:
        file = file.read().lower()
        dictionary = file.split('\n')[2:]
    tuples = []
    central_letter = letters[4]
    while len(letters) != 0:
        char = letters[0]
        tuples.append((letters[0], letters.count(char)))
        for i in range(letters.count(char)):
            letters.remove(char)

    for word in dictionary:

        possible_word = word

        if len(word) > 9 or central_letter not in word:
            continue

        for k in range(len(tuples)):
            if possible_word.count(tuples[k][0]) == 0:
                continue
            elif possible_word.count(tuples[k][0]) > tuples[k][1]:
                break
            else:
                possible_word = possible_word.replace(tuples[k][0], '')

        if len(possible_word) == 0:
            try:
                if acceptable_words.index(word) > 0:
                    continue
            except:
                acceptable_words.append(word)

    return acceptable_words


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    # stop with key combination 'cmd+d' ('ctrl+d' if ran in terminal)
    word = ''
    running = True
    user_words = []
    while running:
        try:
            print('Enter the word: ')
            word = input()
        except:
            running = False

        if not word:
            break

        try:
            if user_words.index(word) >= 0:
                continue
        except:
            user_words.append(word)

    return user_words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary of the game.
    """
    correct_words, no_such_words = [], []
    for word in user_words:
        try:
            if words_from_dict.index(word) >= 0:
                correct_words.append(word)
        except:
            no_such_words.append(word)

    return no_such_words, correct_words


def results():
    board = generate_grid()
    print(board)
    user_words = get_user_words()
    possible_combinations = get_words('dictionary.txt', board)
    checked_words = get_pure_user_words(user_words, board, possible_combinations)
    with open('result.txt', 'w') as file:
        print(len(checked_words[1]))
        file.write(str(len(checked_words[1])) + '\n')
        print(possible_combinations)
        file.write(str(possible_combinations) + '\n')
        for word in checked_words[1]:
            possible_combinations.remove(word)
        print(possible_combinations)
        file.write(str(possible_combinations) + '\n')
        print(user_words)
        file.write(str(user_words) + '\n')
        print(checked_words[0])
        file.write(str(checked_words[0]))
        file.close()

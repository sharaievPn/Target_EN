from typing import List
import string
import random


def generate_grid() -> List[str]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
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
        dictionary = file.split('\n')
    tuples = []
    central_letter = letters[4]
    while len(letters) != 0:
        tuples.append((letters[0], letters.count(letters[0])))
        letters.remove(letters[0])

    for word in dictionary:
        possible_word = word
        if len(word) > 9 or central_letter not in word:
            continue
        flag = True
        while len(tuples) != 0:
            if word.count(tuples[0][0]) == -1:
                continue
            if word.count(tuples[0][0]) > tuples[0][1]:
                flag = False
                break
            word.replace(tuples[0][0], '')
            tuples.remove(tuples[0])
        if not flag:
            break

        if len(word) == 0:
            acceptable_words.append(possible_word)

    return acceptable_words




def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    pass


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass

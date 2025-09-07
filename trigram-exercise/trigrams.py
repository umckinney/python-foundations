"""
trigrams.py by Uriah McKinney

Lesson Requirements:
    * Take a string of any length and generate a trigram dict
        Key = set of two consecutive words
        Value = list of words that follow the consecutive words
    * Generate a new string
        Initial string will = a random key from the trigram dict
        The following word = the 0th position of the key's list
        Pop the 0th position from the key's list
        Find the key that matches the 2nd and 3rd words in the new string
        The following word = the 0th position of that key's list
        Pop the 0th position from that key's list
        Continue this process
        When a key has no remaining list items, remove the key
        Punctionation and new lines count as words
        If a word is lowercase and is preceded by a full stop, question mark, exclamation point, or \n, set it to title case
        When there are no remaining keys, add \nThe End
        Save new string to an output file [trigrams-udm-ISOTIMESTAMP.txt]
        Print new string
Goals:
    1. Generate a new .txt file with correct naming convention and content
    2. Pass all tests
Stretch Goals:
    A. Read initial string from a .txt file on disk
    B. Handle memory issues with large file sizes
"""

import re, string, random, copy, os
from datetime import date


def title_case_validation(key_0, key_1):
    """
    Function to manage spacing and capitalization betweens words added to new_string
    Args:
        key_0: 1st key value
        key_1: 2nd key value
    """
    if key_0 in (".", "!", "?") and key_1:
        return " " + key_1.title()
    elif key_0 in ("\n", "\r", "\r\n") and key_1:
        return key_1.title()
    elif key_0 and key_1 in (".", "!", "?"):
        return key_1
    else:
        return " " + key_1


def pick_random_pair(trigram_dict):
    """
    Function to select a random key from trigram_dict
    Used to select initial key and if we hit a deadend
    Args:
        trigram_dict: dict containing trigram key-values
    """
    selection = random.choice(list(trigram_dict.items()))
    return selection[0]


def get_random_follower(trigram_dict, key_pair):
    """
    Function to select a random word from the list associated with the key_pair
    Args:
        trigram_dict: dict containing trigram key-values
        key_pair: active key in trigram_dict
    """
    value_list = trigram_dict.get(key_pair, [])
    try:
        return random.choice(value_list)
    except IndexError as error:
        return "could not find a value. moving on"


def remove_word_from_key_pair_list(trigram_dict, key_pair, next_word):
    """
    Function to remove a word from the active key's list of words after it has been added to new_string
    Args:
        trigram_dict: dict containing trigram key-values
        key_pair: active key in trigram_dict
        next_word: word to remove
    """
    if key_pair_exists(trigram_dict, key_pair) and next_word in trigram_dict[key_pair]:
        trigram_dict[key_pair].remove(next_word)


def remove_key_pair_from_dict(trigram_dict, key_pair):
    """
    Function to remove the active key_pair from the trigrams dict when it's list is empty
    Args:
        trigram_dict: dict containing trigram key-values
        key_pair: active key in trigram_dict
    """
    if key_pair in trigram_dict and not trigram_dict[key_pair]:
        del trigram_dict[key_pair]


def make_sentence(trigram_dict, key_pair):
    """
    Function to construct the new trigram string.
    Args:
        trigram_dict: dict containing trigram key-values
        key_pair: active key in trigram_dict
    """
    new_string = key_pair[0].title() + title_case_validation(key_pair[0], key_pair[1])
    while len(trigram_dict) > 0:
        next_word = get_random_follower(trigram_dict, key_pair)
        if next_word == "could not find a value. moving on":
            break
        if next_word in string.punctuation:
            new_string += next_word
        else:
            new_string += title_case_validation(key_pair[1], next_word)
        remove_word_from_key_pair_list(trigram_dict, key_pair, next_word)
        remove_key_pair_from_dict(trigram_dict, key_pair)
        key_pair = (key_pair[1], next_word)
        if len(trigram_dict) == 0:
            break
        while key_pair not in trigram_dict:
            key_pair = pick_random_pair(trigram_dict)
    new_string += "\n\nThe End."
    return new_string


def split_with_punctuation(initial_string):
    """
    Function to split a string treating punctuation as a value in the resulting list.
    Args:
        initial_string: string from which to construct the trigram.
    """
    return re.findall(r"\w+|[^\w\s]|\n", initial_string)


def build_trigram(split_list):
    """
    Function to construct the trigram.
    Args:
        split_list: list of words and punctuation marks split from initial_string
    """
    trigram_dict = {}
    constructor_list = split_list[:]
    for i in range(len(constructor_list) - 2):
        key_pair = (constructor_list[-3], constructor_list[-2])
        next_word = constructor_list[-1]
        if key_pair_exists(trigram_dict, key_pair):
            trigram_dict[key_pair].append(next_word)
        else:
            trigram_dict[key_pair] = [next_word]
        constructor_list.pop()
    return trigram_dict


def key_pair_exists(trigram_dict, key_pair):
    """
    Function to validate a key_pair exists in the trigrams dict
    Useful for cases where the constructed key_pair is invalid
    Args:
        trigram_dict: dict containing trigram key-values
        key_pair: active key in trigram_dict
    """
    return key_pair in trigram_dict


def save_string(new_string):
    """
    Function to save new_string to disk
    Args:
        new_string: the output of the trigram construction
    """
    path = "Trigrams"
    ensure_directory_exists(path)
    filename = path + "-" + get_timestamp() + ".txt"
    with open(path + "/" + filename, "w") as outfile:
        outfile.write(new_string)


def ensure_directory_exists(directory_path):
    """
    Function ensure the Trigrams directory exists.
    Args:
        directory_path: relative path
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def get_timestamp():
    """
    Function to collect the current timestamp in isoformat
    Used for filename
    """
    return date.today().isoformat()


def get_book():
    start_flag = False
    end_flag = False
    processed_book_text = ""
    try:
        with open("sherlock.txt", "r") as file:
            for line in file:
                list_line = process_book(line, start_flag, end_flag)
                start_flag = list_line[0]
                if list_line[1]:
                    processed_book_text += list_line[1]
                end_flag = list_line[2]
                if end_flag:
                    break
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    return processed_book_text


def process_book(raw_book_line, start_flag, end_flag):
    start_string = "ADVENTURE I. A SCANDAL IN BOHEMIA"
    end_string = "ADVENTURE II. THE RED-HEADED LEAGUE"
    if not start_flag:
        if start_string in raw_book_line:
            return [True, "", False]
    if start_flag:
        if end_string in raw_book_line:
            return [True, "", True]
        else:
            return [True, raw_book_line, False]
    return [start_flag, "", end_flag]


if __name__ == "__main__":
    processed_text = get_book()
    my_string = split_with_punctuation(processed_text)
    my_trigram = build_trigram(my_string)
    starting_key = pick_random_pair(my_trigram)
    new_string = make_sentence(my_trigram, starting_key)
    print(f"New String\n\n{new_string}")
    save_string(new_string)

if __name__ == "__main__":
    main()

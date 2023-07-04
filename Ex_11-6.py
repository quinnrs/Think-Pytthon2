import time

"""  Start with a list of words as strings, find eash word that meets
        these conditions:
        - removing the first letter yields a word with the same
    pronunciation, and
        - removing the second letter yields a word
    with the same pronunciation.  """

# download a phonetic dictionary
from phonetic_dict import read_dictionary
d = read_dictionary()
phonetic = d

def homophones(a, b, phonetic):
    """ this function was copied from the author
        Checks if words two can be pronounced the same way.

        If either word is not in the pronouncing dictionary, return False

        input:  a, b: strings
                phonetic: map from words to pronunciation codes
    """
    if a not in phonetic or b not in phonetic:
        return False

    return phonetic[a] == phonetic[b]

"""
from abrv_dict import limit_dict
print(type(limit_dict))
abrv_word_dict = limit_dict
print(type(abrv_word_dict)) """

# make a word_dict with words >+4 and <= 6
fin = open("Chapter_9/words.txt")
def limit_dict():
    """ write a function that reads the words in words.txt and stores them as 
    keys in a dictionary with these conditions:
        minimum length (excluding white space) is min
        maximum length (excluding white space) is min
        input:  words.txt
        min - int
        max - int
        return: dict
    """
    limit_dict = dict()  # using dict function
    for line in fin:
        word = line.strip()
        # print(word, len(word))  # debugging
        if len(word) <= 6:
            if len(word) >= 4:
                # print(word) prints as expected
                limit_dict[word] = ''
        pass
    return limit_dict

abrv_dict = limit_dict()  # to define dict instead of functio

print(f"\nabrv_dict is  ", type(abrv_dict))  # returns dict
print(f"len(abrv_dict) is ",len(abrv_dict))   # returns 113809 without if logic, 27266 with if
print(f"limit_dict is ", type(limit_dict))  # returns function
# print(len(limit_dict())) # returns 0


def check_word(word, word_dict, phonetic):
    """Checks to see if the word has the following property:
    removing the first letter yields a word with the same
    pronunciation, and removing the second letter yields a word
    with the same pronunciation.



    word: string
    word_dict: dictionary with words as keys
    phonetic: map from words to pronunciation codes
    """
    word1 = word[1:] 
    if word1 not in word_dict:
        return False
    if not homophones(word, word1, phonetic):
        return False

    word2 = word[0] + word[2:]
    if word2 not in word_dict:
        return False
    if not homophones(word, word2, phonetic):
        return False

    return True

# call the function and print results
phonetic = read_dictionary()
# word_dict = limit_dict()
word_dict = abrv_dict   # FINALLY - yes
print(f"\nclass word_dict is ", type(word_dict))
print(f"len(word_dict = ",len(word_dict))
for word in word_dict:
    if check_word(word, word_dict, phonetic):
        print(check_word)
        print(word, word[1:], word[0] + word[2:])

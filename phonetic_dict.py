"""this is an advanced project for me so much of this code has been copied
     directly from the author - i will denote copied code in each segment """


# download the CMU Pronouncing Dictionary
def read_dictionary(filename='Chapter_11/c06d'):
    """ This function was copied from the author
    Reads from a file and builds a dictionary that maps from each word to a
      string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    # fin = open(filename)
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

""" this is how the function should be called 
    d = read_dictionary()
    for k, v in d.items():
        print(k, v)
"""

d = read_dictionary()
# for k, v in d.items():
    #print(k, v)

phonetic = d  # change function to dictionary
print(f"\nlen_phonetic = ",len(phonetic))


# check if are two words are homophones
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

# call and test the function 
a = 'whale'  # exoect False
a = 'whole'  # expect True
b = 'hole'
print(f"\n",homophones(a, b, phonetic))

#
# new file named fin to read input

fin = open("Chapter_9/words.txt")
# # print(fin.readline()) # will stop at first new line
# read the next line # returns expected value
# print(fin.readline())

print("\nEx_9-1")
"""
write a ptrogram to read  each line of a file and print only the words with
more than 20 characters (excluding white space)

input:  words.txt
return: two colunmns with counter and long words
"""
# def print_long_words(fin):
fin = open("Chapter_9/words.txt")
word_count = 0
for line in fin:
    word = line.strip()
    if len(word)  >= 20:
        word_count += 1
        print(word_count, word)
# print("total words in list = ", word_count)


print("\nEx_9-2")
"""
write a function to determine that returns True if a word does not conain "e"

input:  word (a string)
return: True or False
"""
def has_no_e(word): 
    """ 
    index = 0
        while index < len(word):
        print(index, word[index] )
        if word[index] == "e":   # logic problem here
            return False
        index += 1
        return True
    this code runs correctly but the code below is better
    """
    for letter in word:
        # print(word, letter)
        if letter == "e":   
            return False
    return True
    
print(has_no_e("one"))   # should be False- OK 
print(has_no_e("two"))   # should be True - OK

"""
write a program to read each line of a file and print only the words that
do not contain "e)

input:  words.txt
return: two colunmns with counter and words without "e"
"""
fin = open("Chapter_9/words.txt")
word_count = 0
for line in fin:
    word = line.strip()
    # print(word)
    if has_no_e(word) == True:
        word_count += 1
        # print(word_count, word)
# print("total words without 'e'= ", word_count)


print("\nEx_9-3")
"""
write a function that returns True if a word does not conain a
list of forbidden letters

input:  word (a string)
        list of letters
return: True or False
"""
def avoids(word, avoid_list):
    for letter in avoid_list:
        if letter in word:
            # print(word, letter)  # debugging
            # if letter == letter:
            return False
    return True


# avoid_list = ["a", "x", "q", "e",]   
print(avoids(word = "muny", avoid_list = ["a", "x", "q", "e",]))
# shou;d be True - OK
print(avoids(word = "max", avoid_list = ["a", "x", "q", "e",]))
# should be false - OK

print("\nEx_9-4")
"""
write a function that returns True if a word uses only the letters
in the allowed list

input:  word (a string)
        list of letters
return: True or False
"""
def uses_only(word, allowed_list):
    for letter in word:
        if letter not in allowed_list:
            # print(letter, letter)  # debugging
            return False
    return True

# allowed_list = ["a", "e", "d", "m", "s"]   
print(uses_only(word = "made", allowed_list = ["a", "e", "d", "m", "s"]))
# shou;d be True - OK
print(uses_only(word = "muse", allowed_list = ["a", "e", "d", "m", "s"]))
# should be False - OK

print("\nEx_9-5")
"""
write a function that returns True if a word uses all of the 
letters in the required list

input:  word (a string)
        list of letters
return: True or False
"""
def uses_all(word, required_list):
    for letter in required_list:
        #print(word, letter) # debugging
        if letter not in word: 
            return False 
    return True

print(uses_all(word = "bond", required_list = ["b", "a", "n"]))
# should be False - OK
print(uses_all(word = "band", required_list = ["b", "a", "n"]))
# should be True - OK

print("\nEx_9-6")
"""
write a function that returns True if the letters in a word  appear in
alphbetical order (double letters are OK)

input:  word (a string)
        
return: True or False
"""
def is_abecedarian(word):  # this function not correct
    previous = word[0]   # start with first letter in word
    for letter in word:
        # print(letter, previous)  # for debugging
        if letter < previous:  # tests if alphabet order is decreasing
            return False
        previous = letter
    return True

print(is_abecedarian(word = "abb"))
# should be True 
print(is_abecedarian(word = "able"))
# should be False


print("\nEx_9-7")

"""
write a program to search a list of words to find a word from that contains three consecutive double letters.

input: a list of words
        
return: any word with three consecutive double letters
"""




"""
fin = open("Chapter_9/words.txt")
word_count = 0
for line in fin:
    word = line.strip()

    if three_double_letters(word) == True:
        word_count += 1
        print(word_count, word)
print("total words three double letter = ", word_count)
"""
"""
write a program to count the  number of concecutive (double) letters in a word

input: word(string)
        
return: number(int) of double letters
"""
def count_double_letters(word):
    counter = 1
    i = 0
    # print(i, counter)
    while i < len(word)-1:
        # test if concesutive letters are equal 
        if word[i] != word[i+1]:
            counter += 1
        i += 1 
    if counter == len(word):
        return 0
    return len(word) - counter

print(count_double_letters(word="committee"))
print(count_double_letters(word="dog"))

fin = open("Chapter_9/words.txt")
word_count = 0
for line in fin:
    word = line.strip()

    if count_double_letters(word) >= 3:
        word_count += 1
        print(word_count, word)
print("total words three double letter = ", word_count)

""" here are four words with three consecutive double letters
9 bookkeeper
10 bookkeepers
11 bookkeeping
12 bookkeepings
"""


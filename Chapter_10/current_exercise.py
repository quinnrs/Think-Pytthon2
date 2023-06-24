print("\nEx_10-8")
""" analyze the birthday paradox -- what are the odds that a class of 23 
    students will have two with the same birthday? """

def has_duplicates(t):
    """ Returns True if any element apears more than once in a sequence,
        otherwise returns False
        input , a list of integers (birthday_list)
    """
   # make a copy of the list to avoid moodificalion of original
    s = t[:]
    s.sort()

    # check if adjacent elements are equal
    for k in range(len(s)-1):
        if s[k] == s[k+1]:
            return True
    return False


# generate a list is 23 random birthdays
import random

def birthday_list(n):
    """ input: list of random birthdays  - int  from 1 - 365
                n - int for number of students
        returns a list of int
    """
    # birthday_list = []
    t = []
    for k in range(n):
        birthday = random.randint(1, 365)
        t.append(birthday) # word, not an index
    # print("\n",t)
    return t


def count_matches(n, simulations):
    """  generates a sample of birthdays and counts duplicates
        input  n - int for number of students
                simulations  - int number of simulations tested
        returns int - number of matches  
    """

    counter = 0
    for j in range(simulations):
        t =  birthday_list(n)
        # if has_duplicates(birthday_list):
        if has_duplicates(t):
            counter += 1    
    return counter

    


n = 23
simulations = 1000
counter = count_matches(n, simulations)

print(("number of students="), n)
print(("number of simulations ="), simulations)
print(("number of matches ="), counter)
print("percentage of similauions with a match ", (100 * (counter/simulations)))











def make_word_list(): 
    word_list = []
    fin = open("Chapter_9/words.txt")
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """ Checks whether a word is in a list using bisection search (my "aha" 
    this is recursion!)

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string

    returns: True if the word is in the list; False otherwise

    note: // is floor division operator (Python ver > 3)
        10 / 3   output is 3.3333333
        10 // 3  output = 3
    """

    

print("\nEx_10-12")
""" write a function that finds all pairs of words in a list of words 
    that interlock.
        example "shoe" and "cold" are interocked to form "schooled"
            by taking alternating letters from each word
    input:  list of strings 
            word - a string
    output: list of pairs of interlocked words
"""
def interlock(word_list, word):
    # separate word list into two new lists
    evens = word[::2]
    odds = word[1::2]
    # print (len(evens), len(odds))
    return in_bisect(word_list, evens) and in_bisect(word_list, odds)


# word_list = ['shoe', 'cold', 'no', 'on', 'me', 'you', 'he', 'her'] 
# word_list = my_word_list1
# word_list = t1
word_list = make_word_list()
print(len(word_list))
print(word_list[:10])

def interlock_general(word_list, word, n=3):
    """Checks whether a word contains n interleaved words.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True

"""   
for word in word_list:
    if interlock(word_list, word):
        print(word, word[::2], word[1::2])
# I was suprised at the length of number of interlocks

for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])
# I was again suprised at the number of triple interlocks
"""

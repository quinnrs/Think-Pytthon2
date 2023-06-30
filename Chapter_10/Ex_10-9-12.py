#
# new file named fin to read input

fin = open("Chapter_9/words.txt")
# # print(fin.readline()) # will stop at first new line
# read the next line # returns expected value
# print(fin.readline())

print("\nEx_10-9")


import time
""" 
    write a function that reads the file word.txt and builds a list with one 
    element per word.
    input:  words.txt   single column text file with one word per column 
    output: words - a list with one element per word  - words[]  
"""
# def my_word_list1(my_text_file):  # use append
def my_word_list1(): 
    t1 = []
    fin = open("Chapter_9/words.txt")
    for line in fin:
        word = line.strip()
        t1.append(word)
    return t1

start_time = time.time()
t1 = my_word_list1()
print(len(t1))
print(t1[:10])
elapsed_time =  1000 * (time.time() - start_time)
print (elapsed_time,  'millisec' )
""" t1 elapsed time = 11.3 milisec
    proaably slower because it modifies the original list """
def my_word_list2():  # use + operator
    t2 = []
    fin = open("Chapter_9/words.txt")
    for line in fin:
        word = line.strip()
        t2 += [word]
    return t2


start_time = time.time()
t2 = my_word_list2()
print("\n")
print(len(t2))
print(t2[:10])
elapsed_time = 1000 * (time.time() - start_time)
print (elapsed_time, 'millisec')
""" t2 elapsed time = 2.2 milisec using + operator
    probably faster because it creates a new list """
print("\nEx_10-10")


import bisect
""" 
use and understand the Python bisect module for searching long lists

bisect.insort_left(a, x, lo=0, hi=len(a), *, key=None)
Insert x in a in sorted order.

This function first runs bisect_left() to locate an insertion point. Next, it 
runs the insert() method on a to insert x at the appropriate position to 
maintain sort order.

To support inserting records in a table, the key function (if any) is applied 
to x for the search step but not for the insertion step.

bisect.bisect_right(a, x, lo=0, hi=len(a), *, key=None)
bisect.bisect(a, x, lo=0, hi=len(a), *, key=None)
Similar to bisect_left(), but returns an insertion point which comes after (to 
the right of) any existing entries of x in a.

The returned insertion point i partitions the array a into two halves so that 
all(val <= x for val in a[lo : i]) for the left side and all(val > x for val 
in a[i : hi]) for the right side.

key specifies a key function of one argument that is used to extract a 
comparison key from each element in the array. To support searching complex 
records, the key function is not applied to the x value.

If key is None, the elements are compared directly with no intervening 
function call.
"""

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

    if len (word_list) == 0:
        return False   # empty list
    
    i = len(word_list) // 2  # uses total list
    # print(i)   # used for debugging
    # k = len(word_list) // 2  # documentation uses i not k
    if word_list[i] == word:
        return True
    
    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else: 
        # search the second half
        return in_bisect(word_list[i + 1: ], word)
   

def in_bisect_cheat(word_list, word):
    """ Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """

    i = bisect.bisect_left(word_list, word) # uses bisect left list
    print(i) # used for debugging
    if i == len(word_list):
        return False
    return word_list[i] == word
    
word_list = my_word_list1()
#  print(len(word_list))  # used for debugging

start_time = time.time()

#for word in ['aa', 'alien', 'allen', 'zymurgy', 'zztop']:
for word in word_list:
    print(word, 'in list', in_bisect(word_list, word))

print(word, 'in list', in_bisect(word_list, word))
elapsed_time = (time.time() - start_time)
print (elapsed_time, 'seconds for bisect word list' )
""" elapsed time 38.25 seconds for bisect word list """

print('\n')
start_time = time.time()

# for word in ['aa', 'alien', 'allen', 'zymurgy', 'zztop']:
for word in word_list:
        print(word, 'in list', in_bisect_cheat(word_list, word))


# print(word, 'in list', in_bisect_cheat(word_list, word))


elapsed_time = (time.time() - start_time)
print (elapsed_time,  'seconds for bisect_cheat word list' )
"""  elapsed time  7.44 seconds for bisect_cheat word list"""

print("\nEx_10-11")
"""  write a program that that finds all the reverse pairs in a word list 
     example "pleh" and "help" are reverse pairs 

def reverse_pair(word_list, word):
    input:  word_list - a list of strings
        word - string
    output: single column of all reverse pairs in word_list
    
    rev_word = word[::-1]
    # print(word, rev_word)   # for debugging
    # print(in_bisect(word_list, rev_word))
    return in_bisect(word_list, rev_word)
    
# word_list = ['am', 'ma', 'me', 'mm', 'tu', 'xy']
word_list = t1

for word in word_list:
    # print(word, word[::-1])
    if reverse_pair(word_list, word):
        print(word, word[::-1])

elapsed_time = time.time() - start_time
print (elapsed_time,  'seconds' )
"""
"""elapsed time = 39.9 seconds for reverse_pair result """


"""- - -  alternate code option to compare elaosed times  - - - """

start_time = time.time()

def rev_word(s):  # s is a string
    """
    input:  string
    output: sing;e colum nof rev_words in the list
    """
    return ' '.join([x[::-1] for x in s.split(' ')])
    
    # .join  and .s are required to remove the ' ' separators
    # return ([x[::-1] for x in s])
    
# test_list = ['am', 'ma', 'me', 'my', 'em']
test_list = word_list
counter = 0
for s in test_list:
    rev_word(s) 
    # this returns the correct solution but is very slow 
    # removing the counter did not help much - still inefficient
    if rev_word(s) in test_list:
        counter += 1
        print(counter, s, rev_word(s))
        # print(s, rev_word(s)) 

elapsed_time = time.time() - start_time
print (elapsed_time,  'seconds' )
""" elapsed time 39.9 seconds for rev_words function """


""" used to bebug concept - runs as expected """
""""
def rev_word(s):  # s is a string
    return ' '.join([x[::-1] for x in s.split(' ')])
s = "help"
# print(rev_word(s))
print("rev_pair = ", s, rev_word(s))
"""

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



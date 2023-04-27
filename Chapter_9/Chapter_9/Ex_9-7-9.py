"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


print("Ex_9-7")
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

"""
write a program  to search a list of words to find words with three
pair of double letters whether consecutive or not
"""
fin = open("Chapter_9/words.txt")
word_count = 0
for line in fin:
    word = line.strip()
    if count_double_letters(word) >= 3:
        word_count += 1
        print(word_count, word)
print("total words three double letter = ", word_count)

# list contains 46 words with triple double letters

 
""" here are four words with three consecutive double letters
9 bookkeeper
10 bookkeepers
11 bookkeeping
12 bookkeepings
"""

print("\nEx_9-8")
"""
the challenge is to solve a puxzzle using an example for an odometer with six
integers that represnt whole miles
 - first event: last 4 digits are a palindrome
 - second event: after 1 mile, the last 5 gigits are a pailindrome
 - third event: after 1 mile, the middle 4 digits are a palindrome
 - fourth event: after 1 mile, all six digits are a palindrome

step 1 - decide how to test if a string is a palindrome
step 2 - create a list of string equivalent integers that are the odometer,
    max str length is '999,999'
step 3 - loop thru the list to return True when an integer satisfiea all four
    of the conditions above
return:    the odometer reading(s) that satisfy the criteria

"""

""" this code is from previous work 
for str , rev_str == str[::-1]
"""
def has_palindrome(i, start, length):
    """Checks if the string representation of i has a palindrome.
    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start:start+length]
    return s[::-1] == s

print(has_palindrome(i=101, start=0, length=10))  # True
print(has_palindrome(i=102, start=0, length=10))  # False

def check(i):
    """" checks if an integer (i) meets the four test criteria """
    """  using an if statement returns TypeError: 'int' object is not callable
        so must use code as shown below (without :) """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))
    
def check_all():
    """  loops check(i) thru int in range and prints any True number"""
    i = 100000
    while i <= 999996:
        if check(i) == True:
            print(i)
        i += 1

print('The following are the possible odometer readings:')
check_all()
print()



print("\nEx_9-9")
"""
how often can two people have ages that are reverse - person 1 is 37 wnen
person 2 is 73? If this has happend six time already, how old is the younger 
person?
"""

def str_fill(i, n):
    """  Returns i as a string with at least n digits by insertng '0s',
        in front of i.  This will allow use of string methods on i 

    i: int
    n: int length
    returns: string

    """
    return str(i).zfill(n)


def are_reversed(j, k):
    """  tests if i and j are reverse of each other
    input   j: int
            k: int
    returns: bool
    """
    return str_fill(j, 2) == str_fill(k, 2)[::-1]


# print(are_reversed (j=21, k=12))  # True
# print(are_reversed (j=20, k=2)) # also True


def count_palindrome_ages(delta, flag = False):
    """Counts the number of palindromic ages.
    Returns the number of times the mother and daughter have
    palindromic ages in their lives, given the difference in age.
    diff: int difference in ages
    """
    younger = 0
    counter = 0
    while True:
        older = younger + delta
        # print ("checking ", older, younger)  # debugging
        # check if ages are reversed
        if are_reversed(younger, older) or are_reversed(younger, older+1):
        # if are_palindrome_ages(younger, older): # did not work
            counter += 1
            # print(younger, older) # debugging
            if flag: 
                print(younger, older)
                # print("are not reversed")
        if older > 114:
            break
        younger += 1
    # print("when delta is",delta, "there will be", counter, "reverse ages")
    print(delta, counter) # debugging
    return counter

# count_palindrome_ages(delta=18) # returns expected results
def check_results():
    """
    Tabulate a range of age differnces (delta) betwee two people. For each delta. List the ages that will be reverse pairs.

    Assume minimum delta will be 10 and maximum 70
        
    input:  delta -int
    """
    delta = 15
    while delta < 65:
        n = count_palindrome_ages(delta)
        if n > 0:  #prints when n = 0 ??? why???
            print(delta, n)
        delta += 1

print("delta  #instances")
check_results() # runs as expected

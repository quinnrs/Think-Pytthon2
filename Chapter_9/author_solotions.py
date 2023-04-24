"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

print("/nEx 9_7  - RSQ code that was vever debogged")

"""
write a function to eveuate if triple doubles are consecutive, eg 
'  .. aa .. bb.cc..' is False but '. aabbcc . ' is True 

input:  word(string)
output: Boolean

"""
""" Error  - never closes
def consecutive_triple_doubles(word):
    i = 0
    while i <  len(word) - 1:
        print(len(word), i)
        if word[i] == word[i+1]:
            if word[i+2] == word[i+3]:
                if word[i+4] == word[i+5]:
                    return True
        else:
            i = (i + 2) 
    return False
 
consecutive_triple_doubles(word="afaabbgcc")
consecutive_triple_doubles(word="gfaabbgccd")
"""

print("Ex_9-7 RSQ code with manual inspection for 'consecutive' ")
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

fin = open("Chapter_9/words.txt")
word_count = 0
for line in fin:
    word = line.strip()

    if count_double_letters(word) >= 3:
        word_count += 1
        print(word_count, word)
print("total words three double letter = ", word_count)



print("\nEx_9-8")
"""
the challenge is to solve a puxzzle using an example for an odometer with six integers that represnt whole miles
 - first event: last 4 digits are a palindrome
 - second event: after 1 mile, the last 5 gigits are a pailindrome
 - third event: after 1 mile, the middle 4 digits are a palindrome
- fourth event: after 1 mile, all six digits are a palindrome
"""

""" this code is from previous work """
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

"""  a palindrome is a word that is spelled the same forwrard or backward.
examples are  "noon" and  "redivider". This function takes word as a string
and returns True if it is a palindrome or False otherwise. """
def is_palindrome(word):
    print(word)
    if len(word) <=1 :
        return True
    if last(word) != first(word):
        return False
    word =  middle(word)
    # print(word)
    # is_palindrome(word=middle(word))
    return is_palindrome(middle(word))


print("\nEx_9-8")
""" this is the solution from the website """
def has_palindrome(i, start, length):
    """Checks if the string representation of i has a palindrome.
    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start:start+length]
    return s[::-1] == s

    
def check(i):
    """Checks if the integer (i) has the desired properties.
    i: int
    """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))


def check_all():
    """Enumerate the six-digit numbers and print any winners.
    """
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1


print('The following are the possible odometer readings:')
check_all()
print()



print("\nEx_9-9")
"""
how often can two people have ages that are reverse - person 1 is 37 wnen person 2 is 73? If this has happend six time already, how old is the younger person?
"""
def str_fill(i, n):
    """Returns i as a string with at least n digits.
    i: int
    n: int length
    returns: string
    """
    return str(i).zfill(n)


def are_reversed(i, j):
    """Checks if i and j are the reverse of each other.
    i: int
    j: int
    returns:bool
    """
    return str_fill(i, 2) == str_fill(j, 2)[::-1]


def num_instances(diff, flag=False):
    """Counts the number of palindromic ages.
    Returns the number of times the mother and daughter have
    palindromic ages in their lives, given the difference in age.
    diff: int difference in ages
    flag: bool, if True, prints the details
    """
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff

        # assuming that mother and daughter don't have the same birthday,
        # they have two chances per year to have palindromic ages.
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """Finds age differences that satisfy the problem.
    Enumerates the possible differences in age between mother
    and daughter, and for each difference, counts the number of times
    over their lives they will have ages that are the reverse of
    each other.
    """
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1

print('diff  #instances')
check_diffs()

print()
print('daughter  mother')
num_instances(18, True)





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
the challenge is to solve a puxzzle using an example for an odometer with six integers that represnt whole miles
 - first event: last 4 digits are a palindrome
 - second event: after 1 mile, the last 5 gigits are a a pailindrome
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



print("\nEx_9-9")
"""
how often can two people have ages that are reverse - person 1 is 37 wnen person 2 is 73? If this has happend six time already, how old is the younger person?
"""






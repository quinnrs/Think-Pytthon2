"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

def str_fill(i, n):
    """Returns i as a string with at least n digits.
    i: int
    n: int length
    returns: string
    """
    return str(i).zfill(n)


# def two_ages(i, delta, n=3):
    """ write two columns of ages as string representaion of i 
    i: int - age of younger person
    n: int - length
    delta: int - age d1fference 
    returns: younger, older
    """
    younger = str_fill(i, n)
    older = str_fill(i + delta, n)
    return print(younger, older)

def are_reversed(i, j):
    """Checks if i and j are the reverse of each other.
    younger: int
    older: int
    returns:bool """
    return str_fill(i, 2) == str_fill(j, 2)[::-1]

# print (are_reversed(i=2, j=20)) # prints True

def are_palindrome_ages(younger, older):

    """  takes two ages and checks if they are palindromes
         assuming that younger and older don't have the same birthday,
         they have two chances per year to have palindromic ages.
    
    input:  younger - int
            older - int
    output; boolean      """
    if are_reversed(younger, older) or are_reversed(younger, older+1):
        return True
    else:
        return False
            
# print(are_palindrome_ages(younger=13, older=30)) # prints True


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
            # if flag: 
                # print(younger, older)
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
    delta = 10
    while delta < 60:
        n = count_palindrome_ages(delta)
        if n > 0:  #prints when n = 0 ??? why???
            print(delta, n)
        delta += 1

print("delta  #instances")
check_results() #runs as expected except for printing when n = 
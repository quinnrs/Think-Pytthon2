print("\nEx_10-1")
"""
write a program called nested_sums that computes the total of all numbers in a list of lists.
   
    input  t: list of list of numbers

    returns: number
    
"""
t = [[1, 2], [ 3, 4], [5, 6, 7]]
"""  reduce code  """"""
def nested_sum(t):
    total = 0
    for list in t:
        # print(list)
        for num in list:
            # print(num)
            total += num
            # print(total)
    return total
"""
def nested_sum(t):
    total = 0
    for nested in t:
        total += sum(nested)
    return total
    
total = nested_sum(t)   # predict 28
print(f"nested sum(t) =", total) 

print("\nEx_10-2")
"""
wrtte a function called cumsum that takes a list of numbers and returns a mew
list with cumulative sums of the original list
    input:      a list of numbers
    returns:    a list of numbers
"""
t = [1, 2, 3, 4]
def cumsum(t):
    cum = 0
    sums = []
    for num in t:
        cum += num
        # print(cum)
        sums.append(cum)
    return sums

sums = cumsum(t)    # predict [1, 3, 6, 10]
print(f"cumsum(t) =", sums)

print("\nEx_10-3")
"""Write a function called middle that returns all but the first and last
    elements of the list t.

    input   t: list

    returns: new list
    will use slice because it returns a new list
"""
t = [1, 2, 3, 4, 5]
def middle(t):
    return t[1:-1]

print(middle(t)) # predict[2, 3, 4]

print("\nEx_10-4")
"""Write a function called chop that takes a list t and modifies it by 
removing the first and last elements and returns None

    input   t: list

    returns: new list
    but I will commento ut the retuen
"""
t = [1, 2, 3, 4, 5]
def chop(t):
    del t[0]
    del t[-1]

print(chop(t)) # None

print("\nEx_10-5")
"""Write a function called is_sorted that takes a list t and returns True if 
   the list is sorted ia ascending order  and False if not. 

    input   t: list

    returns: True or False 
    but I will commento ut the retuen
"""

def is_sorted(t):
    for k in range(len(t) - 1):
        if t[k] >= t[k + 1]:
            return False
    return True

# t = [1, 2, 3, 4, 5] # predict True
# t = [6, 4, 5, 3, 1] # predict False
        
print(is_sorted(t)) # None

print("\nEx_10-6")
"""Write a function called is_anagram that takes takes two strings and returns
   True if the strings are anagramsm False if not. 

    input   word1: string or list
            word2; String or list

    returns: True or False 
    
"""

def is_anagram(s1, s2):
    """ does not work if s1 or s2 has duplicate letters   
    t = list(s1)
    for letter in t:
        if letter not in s2:
            return False
    return True
    """

    # sort s1 and s2  - if sorted list are equal, then True
    return sorted(s1) == sorted(s2)


s1 = "teem"
s2 = "meet"  # peredict True
# s2 = "meat"  #preditc False
        
print(is_anagram(s1, s2))

print("\nEx_10-7")
""" Write a function called has_duplicates that takes takes a list as a parameter
    and returns True if there is any element that appears more than once. It
    should not modify the original list.
   
    input  t, a list

    returns: True or False  
"""
def has_duplicates(t):
    # make a copy of the list to avoid moodificalion of original
    s = t[:]
    s.sort()

    # check if adjacent elements are equal
    for k in range(len(s) - 1):
        if s[k] == s[k+1]:
            return True
    return False

# t = [6, 9, 3, 1]        # predict False
# t = [3, 6, 9, 3]      # predict True
# print(has_duplicates(t))


print("\nEx_10-8")
""" analyze the birthday paradox -- what are the odds that a class of 23 
    students will have two with the same birthday? """


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
      


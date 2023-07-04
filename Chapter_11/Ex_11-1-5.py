import time

print("\nEx_11-1")
"""
write a function that reads the words in words.txt abd stores them as keys
 in a dictionary
"""
fin = open("Chapter_9/words.txt")
# # print(fin.readline()) # will stop at first new line
# read the next line # returns expected value
# print(fin.readline())
def my_dict():
    my_dict = dict()  # using dict function
    for line in fin:
        word = line.strip()
        # print(word)  it prints the list as a column
        my_dict[word] = ''  
    return my_dict

# print(my_dict())   # runs as expected
print(len(my_dict()))
"""  check time required and compare with ex 10-10
        using list in and bisect list approach  """
"""  
start_time = time.time()

def my_dict():
    my_dict = dict()  # using dict function
    for line in fin:
        word = line.strip()
        # print(word)  it prints the list as a column
        my_dict[word] = ''  
    return my_dict

print(my_dict())   # runs as expected

elapsed_time = (time.time() - start_time)
print (elapsed_time, 'seconds for dict function' )
""" 

""" elapsed time 38.25 seconds for bisect word list """
""" elapsed time 0.00011014938354492188 seconds 
    for dict function  """
print("\nEx_11-2")
"""   use dictionary method 'setdefault' to improve this function """   
def invert_dict(d):
    """Inverts a dictionary, returning a map from val to a list of keys.
        If the mapping key->val appears in d, then in the new dictionary
        val maps to a list that includes key.
    input d: dict
    return invert_dict
    """

# this function works, the task is to improve it 
def invert_dict(d):
    inverse1 = dict()
    for key in d:
        val = d[key]
        # if val not in inverse1:
        #    inverse1[val] = [key]
        # else:
        #    inverse1[val].append(key)
        inverse1.setdefault(val, []).append(key)
    return inverse1
"""    the deletions are replaced with a single line of code """

def histogram(s):
    d = dict()  # a function to create an empty dictionary
    for c in s:     # loops through each character in the string
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

hist = histogram('parrot')
print(hist)
inverse1 = (invert_dict(hist))
print(inverse1)

print("\nEx_11-3")
"""   Memoize the Ackermann function from Ex_6-2
        Computes the Ackermann function A(m, n)
        
        m, n: non-negative integers 

print("\nEx_6-2")
def ack(m, n):
    if m == 0:
        return n+1
    # if n == 0 and m > 0: redundant code
    if n == 0:
        return ack(m-1, 1)
    return ack(m - 1, ack(m, n-1))

print(ack(3, 4))
# reurned expexted result of 125

The is no original thought here, I used author code,
    probably because I have very little interest in this sort of problem 

""" 
known = {}
def ack(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ack(m-1, 1)
    if (m, n) in known:
        return known[m, n]
    else:
        known[m, n] = ack(m-1, ack(m, n-1))
        return known[m, n]
    
print(ack(3, 4))
# reurned expexted result of 125
print(ack(3, 6))
# returned 509

print("\nEx_11-4")
""" Write a function called has_duplicates that takes takes a list as a parameter
    and returns True if there is any element that appears more than once. It
    should not modify the original list.
   
    input  t, a list

    returns: True or False  

    upgrade previous solution by using a dict instrad of a list

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
"""
def histogram2(s):
    d = dict()  # a function to create an empty dictionary
    for c in s:     # loops through each character in the string
        # d.get('c', 1)
        d[c] = d.get('c', 1)
    return d

def has_duplicates(s):
    """ histogram1(s) will have all values = 1 if no duplicates
        so in any value > 1, has duplicates must be True""" 
    for value in histogram2(s):
        if value >= 2:
            return True
        return False
        
# s = [6, 9, 3, 1]        # predict False
s = [3, 6, 9, 3]      # predict True
print(has_duplicates(s))

print("\nEx_11-5")
# start with my_dict hrom Ex_11-1 
fin = open("Chapter_9/words.txt")
def word_dict():
    d = dict()  # using dict function
    for line in fin:
        word = line.strip()
        # print(word)  it prints the list as a column
        d[word] = None  
    return d

# call the function
my_long_dict = (word_dict())  # to  define a dict instead of a function
# print(type(my_long_dict))
print(len(my_long_dict))

def reverse_pair(d): 
    """Checks whether a reversed word appears in d: dict.
        Note - the reverse of any word is  rev_word = word[::-1]
        word: string  """ 
    rev_pair = []
    for word in d:
        rev_word = word[::-1]
        if rev_word in d:
            rev_pair.append(rev_word)
    return rev_pair

d = my_long_dict   #call the function
print("\nthe number of reverse pairs is ", len(reverse_pair(d)))
# print("reverse pair = ",reverse_pair(d))

print("\nEx_11-6")


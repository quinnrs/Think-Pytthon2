import time
import string
"""
write a program counts how many time each letter appears in a string
    there are several appraches, but this will compare two
    using a list and using a dictionaly
"""
start_time = time.time()
def histogram1(s):
    """ 
    input: s - a string
    returns d - dictionary
    """
    d = dict()  # a function to create an empty dictionary
    for c in s:     # loops through each character in the string
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print("")
print(histogram1('brontosarus'))
elapsed_time =  1000 * (time.time() - start_time)
print ("histogram1 run time = ", elapsed_time,  "millisec" )

start_time = time.time()
def histogram2(s):
    d = dict()  # a function to create an empty dictionary
    for c in s:     # loops through each character in the string
        # d.get('c', 1)
        d[c] = d.get('c', 1)
    return d

print("")
print(histogram2('brontosarus'))
elapsed_time =  1000 * (time.time() - start_time)
print ("histogram2 run time = ", elapsed_time,  "millisec" )

start_time = time.time()
import string
def histogram3(s):
    """ 
    input: s - a string
    returns d - dictionary
    use a list this time
        make a list of every letter in the alpabet
        loop through the characters in the alphabet list
            if character in string - add a key-value pair to dict
    """
    d = dict()
    alphabet = list(string.ascii_lowercase)
    # print(alphabet)
    for c in alphabet:
        if c in s:
            # print(c)
            # d.get('c', 0)
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
    return d

print("")
print(histogram3('brontosarus'))
elapsed_time =  1000 * (time.time() - start_time)
print ("histogram3 run time = ", elapsed_time,  "millisec" )


""" 
import string
alphabet = list(string.ascii_lowercase)
print(alphabet)
"""
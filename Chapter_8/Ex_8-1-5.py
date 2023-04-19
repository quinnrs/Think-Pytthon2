print("Ex_8-1")
""" from page 89 -  """
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

# print(find("doctor", "o"))

# from page 92
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1

    while j >= 0:
        print(i, j)  # print for debugging
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True

print(is_reverse("pots", "stop")) #returns True as expected


print("\nEx_8-2")
""" use string method count()to count "a"s in banana """
string = "bananas"
print(string.count("a"))

print("\nEx_8-3")
""" rewrite is_palindrome(word) as is_ palindrome_2 word by using
slice with optional 3rd index for step size -
given slice[::-1] returns a reversed string """

print("please refer to new code and solution in palindrome.py")

print("\nEx_8-4")
"""
here are five separate functions that are all intended to check whether a
string contains any lower case letters - the task is test and debug them
"""
def any_lowercase1(s):  # this returns the expected results
    for c in s:
        if c.islower():
            return True
        else:
            return False
         
def any_lowercase2(s):
    for c in s:
        """ this function only evaluates the character'c' rather than all
        characters in the string. it wall always return True  """
        if 'c'.islower(): #ERROR
            return True
        else:
            return False 

def any_lowercase3(s):
    """ this function runs as expected - I think this is because
        "flag = returns a boolean evaluation of the variable """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """ this function runs as expected - the value of 'flag' is reassigned
    in the for statement which overides the previous assigment inside the
    function """
    flag = False # ERROR - but does not change the result
    for c in s:
        flag =  flag or c.islower()
    return flag

def any_lowercase5(s):
    """ this function will always return 'True' - maybe  because the 'not' 
    operator negates every 'False' return   """
    for c in s:
        if not c.islower: #ERROR
            return False
    return True
    
print(any_lowercase5(s = "big deal c"))
print(any_lowercase5(s = "BFD"))


print("\nEx_8-5")
# aka Caesar cypher
def rotate_letter(letter, n):
    """ Rotates a letter by n spaces
    letter: single-letter string
    n: int
    returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    # print(c, i) # for debugging
    return chr(i)

def rotate_word(word, n):
    """
    Rotates a word by n spaces
    word: string
    n: int
    returns: rot_str
    """
    rot_str = ""
    for letter in word:
        rot_str += rotate_letter(letter, n)
    return rot_str
       

# print(rotate_letter("z", 1))
print(rotate_word("IBM", -1))




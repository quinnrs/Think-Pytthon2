""" word is a string object """

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

"""    test the simple functions -----
print("word_first = ", first(word="help"))
print("word_first = ", first(word="me"))
print("word_first = ", first(word="i"))
print("word_first = ", first(word=" "))

print("\nword_last = ", last(word="help"))
print("word_last = ", last(word="me"))
print("word_last = ", last(word="i"))
print("word_last = ", last(word=" "))

print("\nword_middle = ", middle(word="help"))
print("word_middle = ", middle(word="me"))
print("word_middle = ", middle(word="i"))
print("word_middle = ", middle(word=" "))
------ test the simple functions -------
""" 

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
    
print(is_palindrome(word = "redivider"))
print(is_palindrome(word = "noway"))
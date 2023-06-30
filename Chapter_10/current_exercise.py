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

d = my_long_dict
print("\nthe number of reverse pairs is ", len(reverse_pair(d)))
# print("reverse pair = ",reverse_pair(d))

print("\nEx_11-6")


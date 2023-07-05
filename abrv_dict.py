
import time
fin = open("Chapter_9/words.txt")


def limit_dict():
    """ write a function that reads the words in words.txt and stores them as 
    keys in a dictionary with these conditions:
        minimum length (excluding white space) is min
        maximum length (excluding white space) is min
        input:  words.txt
        min - int
        max - int
        return: dict
    """
    limit_dict = dict()  # using dict function
    for line in fin:
        word = line.strip()
        # print(word, len(word))  # debugging
        if len(word) <= 6:
            if len(word) >= 4:
                # print(word) prints as expected
                limit_dict[word] = ''
        pass
    return limit_dict

abrv_dict = limit_dict()  # to define dict instead of function
print(type(abrv_dict))  # returns dict
print(len(abrv_dict))   # returns 113809 without if logic, 27266 with if
print(type(limit_dict)) # returns function
# print(len(limit_dict())) # returns 0

def check_word_triple(word, word_dict): 
    """Checks to see if the word has the following property:
    removing the first letter yields a valid word , and removing 
    the second letter also yields another valid word

    word: string
    word_dict: dictionary with words as keys
    returns True or False
    """

    word_dict = abrv_dict
    # word in dict
    word1 = word[1:]
    word2 = word[0] + word[2:]
    # print(word, word1, word2) 
    if word1 not in word_dict:
        return False
    if word2 not in word_dict:
        return False
    
    return True
    
# call function
# word = "whale" # expect True
# word = "awful"  # expect False
# print(check_word_triple(word, abrv_dict))
# word_list = abrv_list
# print(f"\n",check_word_triple(word, word_list))
# elapsed_time = 1000 * ((time.time() - start_time))
# print (elapsed_time, 'millisec')

start = time.time()
# make a new list of word triples
word_triples = []

for word in abrv_dict:
    if check_word_triple(word, abrv_dict) == True:
        word_triples.append(word)

print(f"\nlen(word_triples) is", len(word_triples))
"""  returns 'len(word_triples) is 1365'  """
end = time.time()
elapsed_time = 1000 * ((end - start))
print (f"using word_ dict, elapsed_time ", elapsed_time, "millisec")

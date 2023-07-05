import time
fin = open("Chapter_9/words.txt")

def limit_list(word, min, max):
    """
write a program to read  each line of a file and make a new list with these
    conditions:
        minimum length (excluding white space) is min
        maximum length (excluding white space) is min
input:  words.txt
        min - int
        max - int
return: list

    """
    limit_list = []
    for line in fin:
        word = line.strip()
        if len(word)  >= min and len(word) <= max:
            limit_list.append(word)
    return limit_list

# call the function
abrv_list = limit_list(fin, min=4, max=6)
# print(type(abrv_list))
print(f"\nlen(abrv_list) is", len(abrv_list))
print(abrv_list[0:6:]) # list as expected
# print("wfuf" in abrv_list)

# def limit_dict(word):


def check_word_triple(word, word_list):
    """Checks to see if the word has the following property:
    removing the first letter yields a valid word , and removing 
    the second letter also yields another valid word

    word: string
    word_list: list of words
    returns True or False
    """
    # abrv_list = limit_list(fin, min=4, max=6)
    word_list = abrv_list
    word1 = word[1:]
    word2 = word[0] + word[2:]
    # print(word, word1, word2)
    # if "word1" not in abrv_list: 
    if word1 not in abrv_list:
        return False
    if word2 not in abrv_list:
        return False
    
    return True
    
# call function
# word = "whale" # expect True
# word = "awful"  # expect False
word_list = abrv_list
# print(f"\n",check_word_triple(word, word_list))

start = time.time()
# make a new list of word triples
word_triples = []
for word in abrv_list:
    if check_word_triple(word, abrv_list) == True:
        word_triples.append(word)

print(f"\nThe length of list(word_triples) is", len(word_triples))
print(word_triples[0:6:])
"""  returns 'len(word_triples) is 1035'  """
end = time.time()
elapsed_time = 1000 * (end - start)
print (f"using word_ list, elapsed_time ", elapsed_time, "millisec")
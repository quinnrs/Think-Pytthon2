# ex 3-1
def right_justify(s):
    # right=len(s)
    # spacer=70-right
    # print((" ")*spacer,s)
    print((" ")*(70-len(s)),s)

right_justify("sandy")

# ex 3-2
def do_twice(f):
    f()
    f()
def print_spam():
    print("spam")

    
do_twice(print_spam)

    
def do_twice_rev(f, value):
    f(value)
    f(value)

    
def print_twice(bruce):
    print(bruce)
    print(bruce) 

do_twice_rev(print_twice, "spam")
# out put was as expected


def do_four(f, value):
    do_twice_rev(f, value)
    do_twice_rev(f, value)

do_four(print_twice,  "spam")
# out put was as expected


# do_four(print_twice, 'spam') #syntax error
# do_four(print_twice,"spam")

print("+","-")   # printed + -

print("+", end="")
print("-")
# the two statments printed +-

print("+", end=" ")
print("-")
# the two statments printed + -
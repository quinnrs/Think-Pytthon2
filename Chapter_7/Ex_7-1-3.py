"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""


import math


print("Ex_7-1")
"""   """

def mysqrt(a, x):
    for n in range(4):
        y = (x + a/x) / 2
        # print(y)
        x = y
        n += 1
    return y
        

def test_square_root(a):
    print("-a- mysqrt(a)----   math.sqrt(a)----- diff---                  ")
    for a in range (1,10):
        diff = abs(mysqrt(a, x=a/2) - math.sqrt(a))
        print(a, mysqrt(a, x=1), math.sqrt(a), diff)
        # print(diff)
    return 

# mysqrt(a=2, x=1)
# test_square_root(a=2)

print("\nEx_7-2")
"""
write a function that uses python eval to take user input of a string
then prints the result - function will continue until user inputs "done"
"""
def eval_loop():
    # input requires neither () nor ""
    string = input("what 'string' do you wish to evaluate?\n")
    print(eval(string))
    print("print you can input 'done' at anytime to quit")
    print("you will get an error message, but you will be gone")
    if (string != 'done'):
        eval_loop()

eval_loop()

# print("\nEx_7-3")

def factorial(n):
    """computes factorial of n recursively."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
    
# print(factorial(6)) returned 720 as expected


"""
long math function to approxiamte pi  - my challenge is to convery the
mathmatical notation correctly (no syntax errors) so I will cude, run
and debug incrementally using expected value and for each step
"""
def estimat_pi():
    # 1/estimat_pi = factor * sum_total
    k = 0
    sum_total = 0
    # this is the formula before the summation
    factor =  (2 * (math.sqrt(2)) / 9801)
    # print(factor)

    # iterate through k until estmat < 1e-15
    while True:
        numerator = factorial(4*k) * (1103 + 26390*k)
        denominator = factorial(k)**4 * 396**(4*k)
        # print(numerator, denominator)
        sum_total += numerator / denominator
        # terminator = factor * sum_total #this causes recursion error
        terminator  = factor * (numerator / denominator)
        # print(k, terminator)
        if abs(terminator) < 1e-15:
            break
        k += 1
    return ( 1 /(factor * sum_total))

# print(estimat_pi())




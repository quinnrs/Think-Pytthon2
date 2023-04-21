print("Ex_5-1")
import time 

"""   get input for current date - remove # to run """
# date = input(" what is the date using mm/dd/yyyy ?\n")
# print(date) # result was "Thu Apr  6 09:13:19 EDT 2023"
current_year = 2023


"""   the epoch is 01/01/1970  - using the current date, calculate  
    the elapsed time in years and days since the epoch     
# print(time.time()) #elapsed since 1/1/1970   """
elapsed_years = (current_year -1) - 1970
elapsed_days = (31 + 28 +31 + 6) - 1
print(f"Time since epoch is {elapsed_years} years and {elapsed_days} days")

print("\nEx_5-2")
def check_fermat(a, b, c, n): # all parameter are integers
    if (int(a) ** int(n) + 
        int(b) ** int(n) == 
        int(c) ** int(n)):
        print("Holy smokes, Fermat was wrong")
    print("No, that doesn't work")

# check_fermat(a=3, b=4, c=5, n=3)
"""
a = input ("what is a\n")
print("a =", int(a))
# print(type(a))
# print(type(int(a)))
b = input ("what is b\n")
print("b =", int(b))
c = input ("what is c\n")
print("c =", int(c))
n = input ("what is n\n")
print("n =", int(n))
"""
# check_fermat(a, b, c, n)
""" this runs now - the error was not using int() in the function
#TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
check_fermat(a=3, b=4, c=2, n=3)
"""

print("\nEx_5-3")
def is_triangle(a, b, c):
    if int(a) > int(b) + int(c):
        return  "No"
    elif int(b) > int(a) + int(c):
        return "No"
    elif int(c) > int(a) + int(b):
        return "No"
    return "Yes"

# print(is_triangle(a=5, b=6, c=13))
      
a = input ("what is a\n")
print("a =", int(a))
# print(type(a))
# print(type(int(a)))
b = input ("what is b\n")
print("b =", int(b))
c = input ("what is c\n")
print("c =", int(c))

# print(is_triangle(a, b, c)) 

print("Ex_5-4")
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+5)

# print(recurse(3, 0))  # returns  "6"
# recurse(-1, 0) # returns "RecursionError: max recursion depth  . . . "




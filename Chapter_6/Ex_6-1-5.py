print("Ex_6-1")
def b(z):
    prod = a(z, z)
    # print("z = ",z, "prod = ,", prod)
    return prod
 
def a(x, y):
    x = x + 1
    # print("a = ", a)
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    # print("square = ", square)
    return square

x = 1
y = x + 1
print(c, y+3, x+y)
# output is "<function c at 0x104a14700> 5 3

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

print("\nEx_6-3")
print("solution in the file palindrome.py")

print("\nEx_6-4")
""" write a function with intergers a and b as arguments to determine
    if a in a power of b (a = b**n)  """
def is_power(a, b):
    # first test is a divisible by b
    if a % b != 0:
        return False
    # second test is quotient divisible by b
    # quotient = a/b
    # print(quotient)
    if (a/b) % b != 0:
        return False
    return True
    
print(is_power(a=8, b=2)) # True
print(is_power(a=10, b=2)) # False

print("\nEx_6-5")
"""  wite a function to determine the greatest common denominator (gcd)
     between two integers (a,b) given that remainder(r) = (a/b) and
     gcd(a, b) =  gcd(b,r)    """
def gcd(a, b):
    r = (a % b)   
    return gcd

# print(gcd(a=20, b=12))
   
    




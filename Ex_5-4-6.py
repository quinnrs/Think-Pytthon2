print("Ex-4")
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+5)

# recurse(3, 0)  # returns  "6"
# recurse(-1, 0) # returns "RecursionError: max recursion depth  . . . "
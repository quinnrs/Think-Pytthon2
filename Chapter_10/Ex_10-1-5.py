print("\nEx_10-1")
"""
write a program called nested_sums that computes the total of all numbers in a list of lists.
   
    input  t: list of list of numbers

    returns: number
    
"""
t = [[1, 2], [ 3, 4], [5, 6, 7]]
"""  reduce code  """"""
def nested_sum(t):
    total = 0
    for list in t:
        # print(list)
        for num in list:
            # print(num)
            total += num
            # print(total)
    return total
"""
def nested_sum(t):
    total = 0
    for nested in t:
        total += sum(nested)
    return total
    
total = nested_sum(t)   # predict 28
print(f"nested sum(t) =", total) 

print("\nEx_10-2")
"""
wrtte a function called cumsum that takes a list of numbers and returns a mew
list with cumulative sums of the original list
    input:      a list of numbers
    returns:    a list of numbers
"""
t = [1, 2, 3, 4]
def cumsum(t):
    cum = 0
    sums = []
    for num in t:
        cum += num
        # print(cum)
        sums.append(cum)
    return sums

sums = cumsum(t)    # predict [1, 3, 6, 10]
print(f"cumsum(t) =", sums) 

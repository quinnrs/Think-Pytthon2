"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com
Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import math
import turtle
bob = turtle.Turtle()
print(bob)
# turtle.mainloop()
# this is Ex_5-5 
print("\nEx_5-5")

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

# draw(bob, length=10, n=5) 

def equilateral(t, length, angle):
    """Draws an equilateral triangle.
    The turtle starts and ends at the peak, facing the middle of the base.
    t: Turtle
    length: length of each of the three legs
    angle: 120 for an equilateral triangle
    """
    t.lt(angle/2)
    t.fd(length)
    t.lt(angle)
    t.fd(length)
    t.lt(angle)
    t.fd(length)
    t.lt(180-angle)
# equilateral(bob, length=60,angle=120)

print("\nEx_5-6")

def koch(t, n):
    """ Draws a koch curve with length n """
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

# koch(bob, n=45)

def snowflake(t, n):
    for k in range(3):
        koch(t, n)
        t.rt(120)

# snowflake(bob, n=75)
    
turtle.mainloop()



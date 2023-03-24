"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import turtle
import math
"""  set turtle screen dimemsions """
from turtle import *
height = 480
width = 480
screen = Screen()
screen.setup(width, height)

from polygon import circle, arc

"""
plan:   all letters will be lower case
standard step size: n
length, width, radius and serif are radius  defined as multiples of n
grid  size: 4(n)wide and 8(n) high
base start position:    lower left
basic moves:    single functions
"""


# basic moves where r denotes right, l denotes left
def fd(t, length):
    t.fd(length)

def bk(t, length):
    t.bk(length)

def lt(t, angle=90):
    t.lt(angle)

def rt(t, angle=90):
    t.rt(angle)

def pd(t):
    t.pd()

def pu(t):
    t.pu()

# define combo moves
def fdlt(t,n, angle = 90):
    """ move forward anf turn left   """
    fd(t, n)
    lt(t, angle)

def fdbk(t,n):
    """  move forward then back to original position" """
    fd(t, n)
    bk(t, n)

def fdrt(t,n, angle = 90):
    """ move forward and turn right   """
    fd(t, n)
    rt(t, angle)


def skip(t, n):
    """  lift the pen and move """
    pu(t)
    fd(t, n)
    pd(t)


# define basic shapes
def stub(t, n, angle):
    """ makes a short line to support an arc
        angle is degrees
    """
def hump(t, n):
    """ draw an 180 degree arc on supported by
    two stubs - there is no predefined starting 
    position or teturn """
    fd(t,n/2)
    arc(t, n, angle=180)
    fd(t,n/2)



def hollow(t, n):
    """move the turtle vertically and leave it at the top, facing right
          # use for top-left starting position    """
    lt(t)
    skip(t, n)
    rt(t)

def post(t, n):
    """Makes a vertical line and return to the original position """
    lt(t)
    fdbk(t, n)
    rt(t)

def beam(t, n, height):
    """Makes a horizontal line at the given height and return """
    hollow(t, n*height)
    fdbk(t, n)
    hollow(t, -n*height)

def diagonal(t, n, angle):
    """ nakea a diagonal line from vertical plane 
        at angle in degrees and return """
    lt(t, angle)
    fdbk(t,n)

def serif(t, n, height):
    """ makes a vertical line to the given height then a hhorizontal line n and
        return to the vertical line """
    lt(t)
    fdlt(t, height)
    fdbk(t, n)
    


def hook_l(t, n):
    """ makes a vertical line to the given height and an arc with the given radius and then returns to start of hook """
    lt(t)
    fd(t, n)
    arc(t, r=n, angle=90)
    # return to start of hook
    pu(t)
    lt(t)
    fdlt(t,n*2, angle=90)
    fd(t,n)
    pd(t)

def hook_r(t, n):
    """ makes a vertical line to the given height then draws an arc, and then returns to baseline """
    lt(t)
    fd(t, n)
    arc(t, r=n, angle= - 180)
    # return to base line
    pu(t)
    fdlt(t, n, angle=90)




"""
each letter starts from the bottom left position
and ends in lower right facing right

"""
def draw_a(t, n):
    lt(t, angle=90)
    fdlt(t, n, angle=90)
    hump(t, n)
    hook_l(t, 1.5*n)

def draw_b(t, n):
    lt(t, angle=90)
    fdbk(t, 4*n)
    rt(t, angle=90)
    hump(t, n) # now return to start
    lt(t, angle=90)
    fdlt(t, 2*n, angle=90)
    skip(t, n=20)

def draw_d(t, n):
    skip(t, n=20)
    lt(t, angle=90)
    fdbk(t, 4*n)
    fd(t, 2*n)
    lt(t, angle=90)
    hump(t, n) 
    # skip(t, n=20)
    


# def draw_l(t, n, height):
#   serif(t, n, height)


# end of specific letters

if __name__ == "__main__":
    #create and position the turtle
    size = 20
    bob = turtle.Turtle()
   
# beam(t = bob, n=10, height=4)
# serif(t = bob, n=10, height=40)
# diagonal(t=bob, n=20 ,angle=60)
# arc(t=bob, r=20 ,angle=180)
# hook_l(t=bob, n=15)
# hook_r(t=bob, n=15)
# hump(t=bob, n=5)

# for f in [hook_l, draw_a]:
    # f(bob, size)
    # skip(bob, size)



# draw_l(bob, n=10, height=80)
draw_a(bob, n=10)
skip(bob,n=15)
draw_b(bob, n=10)
skip(bob,n=5)
draw_d(bob, n=10)
    
  

turtle.mainloop()

    




















    

    



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
return position:    lower right + 
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
    """  move forward then back to original position """
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
    """ makes a short line to support an arc"""
  


def hump(t, n, angle):
    """ draw an 180 degree arc counterclockwise 
    supported by two stubs - there is no predefined 
    starting position or return """
    fd(t,n/2)
    arc(t, n, angle)
    fd(t,n/2)

def hollow(t, n):
    """move the turtle vertically and leave it at the top, facing right
          # use for top-left starting position    """
    lt(t)
    skip(t, n)
    rt(t)

def post(t, n):
    """ makes a vertical line and return to the original position """
    lt(t)
    fdbk(t, n)
    rt(t)

def beam(t, n, height):
    """ makes a horizontal line at the given height and return """
    hollow(t, n*height)
    fdbk(t, n)
    hollow(t, -n*height)

def diagonal(t, n, angle):
    """ makes a diagonal line from vertical plane 
        at angle in degrees and return """
    lt(t, angle)
    fdbk(t,n)

def serif(t, n, height):
    """ makes a vertical line to the given height then a horizontal line n and return to the vertical line """
    lt(t)
    fdlt(t, height)
    fdbk(t, n)
    
def hook_l(t, n):
    """ makes a vertical line to the given height and an arc with the 
    given radius and then returns to start of hook """
    lt(t)
    fd(t, n)
    arc(t, r=n, angle=90)
    # return to start of hook
    pu(t)
    lt(t)
    fdlt(t,n*2, angle=90)
    fd(t, n)
    pd(t)

def hook_r(t, n):
    """ makes a vertical line to the given height then draws an arc, and then returns to baseline """
    lt(t)
    fd(t, n)
    arc(t, r=n, angle= -180)
    # return to base line
    pu(t)
    fdrt(t, n)
    rt(t, angle=180)
    pd(t)

"""
This functions are use as an aid to write code for any letter
by drawing a horizontal line at the top of each frame, then 
returing the pen to either the bottom left with the pen facing up

def frame(t,n ):
    beam(t, n, height=2)
    # fd(t, 2*n)
    # rt(t, angle=90)
    #skip(t, 2*n)
    # rt(t, angle=90)
    # fdbk(t, n)
    # hollow(t, -n*height)
"""

# -- specific letters ------------
def draw_a(t, n):
    skip(t, (3/2)*n)
    rt(t, 180)
    hump(t, n, 180)
    hook_l(t, 1.5*n) # return and spacing
    skip(t, n)

def draw_b(t, n):
    lt(t, angle=90)
    fdbk(t, 4*n)
    rt(t, angle=90)
    hump(t, n, angle=180) # return and spacing
    lt(t, angle=90)
    fdlt(t, 2*n, angle=90)
    skip(t, (2)*n)

def draw_c(t, n):
    skip(t, (3/2)*n)
    rt(t, angle=180)
    hump(t,n, angle=-180) # return and spacing 
    rt(t)
    skip(t, 2*n) # vertical alignment
    lt(t)

def draw_d(t, n):
    skip(t, n/2)
    draw_c(t, n)
    lt(t)
    fdbk(t, 4*n) #return and spaceing
    rt(t)
    fd(t, n)

def draw_e(t, n):
    hollow(t=bob, n=5)
    fdlt(t, 2*n)
    arc(t, n, angle=270)
    fd(t,n)  # return and spacing
    skip(t, n)

def draw_f(t, n):
    beam(t, 3/2*n, height=n/4)
    lt(t)
    fd(t, 5/2*n)
    hump(t,n, angle=-180)#return and spacing
    skip(t, 5/2*n)
    lt(t, angle=90)
    skip(t, n)

def draw_g(t, n):
    skip(t, (3/2)*n)
    rt(t, angle=180)
    hump(t, n, angle=180)
    lt(t)
    fdbk(t, 2*n)
    rt(t, angle=-90)
    hook_r(t, n/2) # return and spacing
    rt(t, angle=180)
    skip(t, 2*n)

def draw_h(t, n):
    lt(t)
    fdbk(t, 3.5*n)
    hump(t, n, angle=-180) #t\return and spacing
    lt(t)
    skip(t, 5/2*n)

# need i, j, k, l, m, n o, p
   
def draw_q(t, n):
    skip(t, (3/2)*n)
    rt(t, angle=180)
    hump(t, n, angle=-180)
    rt(t)
    fd(t, 4*n)
    hook_l(t, n/2) # return and spacing
    lt(t, angle=180)
    fd(t, 2*n)
    rt(t)
    skip(t, 2*n)

def draw_r(t, n):
    lt(t)
    fdbk(t, 2*n)
    fd(t, n)
    arc(t, n, -135) # return and spacing
    rt(t, 135)
    lt(t)
    skip(t, 3/2*n)
    lt(t)
    skip(t, 3/2*n)

def draw_s(t, n):
    fd(t, n)
    hump(t, n/3, 180)
    fd(t, n/4)
    hump(t, n/2, -180)
    fdrt(t, n, 90) # return and spacing
    skip(t, 2*n)
    lt(t)
    skip(t, 5/2*n)

def draw_u(t,n):
    lt(t)
    skip(t, 3/2*n)
    lt(t, 180)
    hump(t, n, 180)
    rt(t, 180)
    fdlt(t,3/2*n, 90)# return and space
    skip(t, n) 


def draw_v(t, n):
    lt(t)
    skip(t, 2*n)
    rt(t, 150)
    fdlt(t, 2.2*n, 120) 
    fdrt(t, 2.2*n, 150) # return and space
    skip(t, 2*n)
    lt(t)
    skip(t, n)

def draw_w(t, n):
    lt(t)
    skip(t, 2*n)
    rt(t, 150)
    fdlt(t, 2.2*n, 120)
    fdrt(t, 2.2*n, 120)
    fdlt(t, 2.2*n, 120)
    fdrt(t, 2.2*n, 120)# return and space
    rt(t, 30)
    skip(t, 2*n)
    lt(t)
    skip(t, 2*n)

def draw_x(t, n):
    lt(t, 45)
    fdbk(t, 2.8*n)
    lt(t, 45)
    skip(t, 2*n)
    rt(t, 135)
    fd(t, 2.8*n)# return and space
    lt(t, 45)
    skip(t, n)
    
def draw_y(t, n):
    lt(t)
    skip(t, 3/2*n)
    lt(t, 180)
    hump(t, n, 180)
    rt(t, 180)
    fd(t, 3*n)
    arc(t, n, -135) # return and spacing
    rt(t, 135)
    skip(t, 4*n)
    hollow(t, 5/2*n)

def draw_z(t, n):
    lt(t)

def draw_space(t,n):
    fd(t, n=" ")


"""
def dra#w_m(t, n)
def dra#w_n(t, n)
def dra#w_p(t, n)
#
#
#
#
#
end of #specific letters """
#
#
#
#



if __name__ == "__main__":
    #create and position the turtle
    size = 20
    bob = turtle.Turtle()

# draw_a(bob, n=5)
# draw_b(bob, n=5)
# draw_c(bob, n=5)
# draw_d(bob, n=5)
# draw_e(bob, n=5)
# draw_f(bob, n=5)
# draw_g(bob, n=5)
# draw_h(bob, n=5)
# draw_q(bob, n=5)
# draw_r(bob, n=5)
# draw_t(bob, n=5)
# draw_u(bob, n=5)
# draw_v(bob, n=5)
# draw_w(bob, n=5)
# draw_x(bob, n=5)
# draw_y(bob, n=5)
# draw_v(bob, n=5)
# draw_w(bob, n=5)

turtle.mainloop() # prints all code abpve to terminal   




















    

    



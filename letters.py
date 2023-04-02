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
    """ move forward and turn left   """
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
    skip(t, 4*n)
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
    """ makes a vertical line to the given height then a horizontal
        line nwide,  then return to the vertical line """
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

def baseline_return(t, n, angle):
    """ returns to baseline with with turtle in vertical position"""
    pu(t)
    rt(t, angle)
    fd(t, n)

def next_letter(t,n):
    """ sets correct spacing for next letter with turtle facing left """
    lt(t, 90)
    skip(t, n)

"""
This functions are use as avisual  aid to write code for any letter
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
    baseline_return(t, 2*n, 270)
    next_letter(t, 3*n)
    
def draw_c(t, n):
    skip(t, n)
    rt(t, angle=180)
    hump(t,n, angle=-180) # return and spacing 
    baseline_return(t, 2*n , 90)
    next_letter(t, n)
    # rt(t)
    # skip(t, 2*n) # vertical alignment
    # lt(t)

def draw_d(t, n):
    skip(t, n)
    lt(t)
    fdbk(t, 4*n)
    lt(t, angle=90)
    hump(t,n, angle=-180)
    baseline_return(t, n, angle=90)
    next_letter(t, n)
    # skip(t,n)
    

def draw_e(t, n):
    fdlt(t, 2*n)
    arc(t, r=n, angle=270)
    fd(t,n)  # return and spacing
    skip(t, n)

def draw_f(t, n):
    # beam(t, 3/2*n, height=1)
    beam(t, n/2, height=1)
    lt(t)
    fd(t, 5/2*n)
    hump(t, n/2, angle=-180)#return and spacing
    # hook_r(t, n)
    # hook_l(t, n)
    baseline_return(t, n/2, angle=0)
    next_letter(t, n/2)
    # skip(t, 5/2*n)
    # lt(t, angle=90)
    # skip(t, n)

def draw_g(t, n):
    skip(t, (3/2)*n)
    rt(t, angle=180)
    hump(t, n, angle=180)
    lt(t)
    fd(t, 2*n)
    rt(t, angle=180)
    fd(t, 3*n)
    # hook_r(t, n/2) # return and spacing
    hump(t, n/2, angle=-180)#return and spacing
    skip(t, n)
    rt(t)
    skip(t, 2*n)

def draw_h(t, n):
    lt(t)
    fdbk(t, 3.5*n)
    hump(t, n, angle=-180) # return and spacing
    lt(t)
    skip(t,n)
    # baseline_return(t, -2*n, angle=0)
    # next_letter(t, n)


def draw_i(t, n):
    lt(t)
    fd(t, 3/2*n)
    skip(t, n)
    circle(t, r=n/4) # now return and space
    rt(t, 180)
    baseline_return(t, 5/2*n, angle=0)
    # baseline_return(t, 3*n, angle=0)
    next_letter(t, -n)
    # skip(t, n=-1)
    # skip(t, n/2)
    # lt(t)
    # skip(t, n/2)


def draw_j(t,n):
    skip(t, 2*n)
    lt(t)
    fd(t, 3/2*n)
    skip(t, n)
    circle(t, r=n/4)
    rt(t, 180)
    skip(t, n)
    # fdrt(t, 3*n)
    fdrt(t, 2*n)
    hook_r(t,n/2) #now return and spacing
    lt(t, 180)
    skip(t, 2*n)

def draw_k(t, n):
    lt(t)
    fdrt(t, n, 135)
    fdbk(t, 1.8*n)
    lt(t)
    fdbk(t, 1.8*n)
    lt(t, 45)
    fdbk(t, 5/2*n) # now return and spacing
    lt(t, 180)
    fdlt(t, n)
    skip(t, 2*n)
    
def draw_l(t, n):
    serif(t, n, height=7/2*n) 
    #now return and spacing
    lt(t)
    fdlt(t, 7/2*n)
    skip(t, n)

def draw_m(t, n):
    lt(t)
    fdbk(t, 2*n)
    hump(t, n, -180)
    rt(t, 180)
    hump(t, n, -180) #now return and spacing
    lt(t)
    skip(t, n)

def draw_n(t, n):
    lt(t)
    fdbk(t, 2*n)
    hump(t, n, -180) #now return and spacing
    lt(t)
    skip(t, n)

def draw_o(t, n):
    # skip(t, n)
    fd(t, n/2)
    circle(t, r=n) #n ow space
    skip(t, 3/2*n)

def draw_p(t, n):
    hump(t, n, 180)
    lt(t)
    fdbk(t, 3.5*n) #return and spacing
    skip(t, 2*n)
    lt(t)
    skip(t, 2*n)

def draw_q(t, n):
    skip(t, (3/2)*n)
    rt(t, angle=180)
    hump(t, n, angle=-180)
    rt(t)
    fd(t, 4*n)
    hump(t, n/2, angle=180)
    baseline_return(t, 2*n, angle=0)
    # baseline_return(t, n, angle=- 90)
    rt(t)
    skip(t, n)

def draw_r(t, n):
    lt(t)
    fdbk(t, 2*n)
    fd(t, n)
    arc(t, n, -135) # return and spacing
    baseline_return(t, 3/2*n, angle=45)
    baseline_return(t, 2*n, angle=45)
    baseline_return(t, 7/4*n, angle=45)
    next_letter(t, n)
    
def draw_s(t, n):
    fd(t, n)
    hump(t, n/2, 180)
    fd(t, n/4)
    hump(t, n/2, -180)
    fdrt(t, n, 90) # return and spacing
    skip(t, 2*n)
    lt(t)
    skip(t, n)

def draw_t(t, n):
    lt(t)
    skip(t, 3/2*n)
    rt(t)
    fdbk(t, 2*n)
    fdlt(t, n)
    fdrt(t, n, 180)
    fdrt(t, 2*n)
    hook_l(t, n)# now return and spacing
    lt(t, 180)
    skip(t, 2*n)
    # lt(t)
    # skip(t, 3*n)

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
    baseline_return(t, n*2, angle =30)
    next_letter(t,n)
    # rt(t, 30)
    # skip(t, 2*n)
    # lt(t)
    # skip(t, 2*n)

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
    rt(t, 45)
    # skip(t, 5/2*n)
    skip(t, 2*n)
    rt(t)
    skip(t, 3*n)

def draw_z(t, n):
    lt(t)# 
    skip(t, 2*n)# 
    rt(t)# 
    fdrt(t, 2*n, 135)# 
    fdlt(t, 2.5*n, 135)# 
    fd(t, 2*n)# 
    skip(t, n)# 

def draw_space(t,n):
    fd(t, n=" ")


"""  end of #specific letters """


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
# draw_s(bob, n=5)
# draw_t(bob, n=5)
# draw_u(bob, n=5)
# draw_v(bob, n=5)
# draw_w(bob, n=5)
# draw_x(bob, n=5)
# draw_y(bob, n=5)
# draw_z(bob, n=5)

    # for f in [draw_a, draw_b, draw_c, draw_d, draw_e, draw_f, draw_g]:
    # for f in [draw_g, draw_h, draw_i, draw_j, draw_k, draw_l, draw_m]:
    # for f in [draw_m, draw_n, draw_o, draw_p, draw_q, draw_r,draw_s, draw_t]:
    for f in [draw_t, draw_u, draw_v, draw_w, draw_x, draw_y, draw_z, draw_a]:
        f(bob, size)
        skip(bob, size)

turtle.mainloop() # prints all code above to terminal   




















    

    



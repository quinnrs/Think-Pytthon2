
"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com
Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import math
import turtle
# bob = turtle.Turtle()
# print(bob)
# turtle.mainloop()

def draw_pie(t, n, r):
    """Draws a pie, then moves into position to the right.
    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    polypie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()

    
def polypie(t, n, r):
    """Draws a pie divided into radial segments.
    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        t.lt(angle)


def isosceles(t, r, angle):
    """Draws an icosceles triangle.
    The turtle starts and ends at the peak, facing the middle of the base.
    t: Turtle
    r: length of the equal legs
    angle: peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)


# create the world and bob
# world = TurtleWorld()
bob = turtle.Turtle()
# bob.delay = 0
bob.pu()
bob.bk(130)
bob.pd()

# draw polypies with various number of sides
size = 40
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
draw_pie(bob, 8, size)
# bob.die(bob)
# bob.hide.turtle

#wait_for_user()
turtle.mainloop()

# dump the contents of the campus to the file canvas.eps
# bob.world.canvas.dump()








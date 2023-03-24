import math
import turtle
bob  = turtle.Turtle()
print(bob)
# turtle.mainloop()  needs to be after code below

# draw a square
for i in range(4):
    bob.fd(100)
    bob.rt(90)

# t is a turtle name
def square(t):  # one-time square
    for i in range(4):
        t.fd(100)
        t.rt(90)

# square(bob)

# len is the length of the square  - multiple use
def square(t, len):
    for i in range(4):
        t.fd(len)
        t.rt(90)

square(bob, 250)

# num is number of sides
def polygon(t, n, len):
    for i in range(n):
        t.fd(len)
        t.rt(360.0 / n)  # 360 caused TypeError

polygon(bob, 6, 100)


def circle(t, r):
    # PI = 3.14  use math.pi
    circum = 2 * r * math.pi
    # n = 36 
    n = int(circum / 3) + 1
    len = circum / n
    polygon(bob, len, 36)

def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polyline(bob, n = 12, length = 20, angle = 15)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    arc(t, r, 360)

circle(bob, r = 100)
turtle.mainloop() # prints all code abpve to terminal

"""
the folliwinging code nust be in the first line for book solution
from __future__ import print_function, division
# bob.die(bob)    # closes the funtion Turtle in line 3
bob.world.canvas.dump  # erases the canvas
wait_for_user   # user closes the screen
"""
bob.die(bob)
bob.world.canvas.dump
# wait_for_user









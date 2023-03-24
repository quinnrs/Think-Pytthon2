"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division
import math
import turtle
bob  = turtle.Turtle()

print(bob)
# turtle.mainloop()

def pie(t, n, length, angle):
    # Draws a triangle. then moves position
    # but does not draw a pie (yet)
    # t: Turtle object
    # n: number of segments
    # length: length of each segment
    # angle: degrees between segments
      
    for i in range(n):
        bob.fd(length)
        bob.rt(angle)
        bob.fd(length)
        bob.rt(angle)
        bob.fd(length)
        

pie(t = bob, n = 3, length = 100, angle = 120)


turtle.mainloop()

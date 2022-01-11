"""
Goal: A program that reads drawing instructions from a file and uses them along with the existing draw function
to draw spirals.
"""
from turtle import *
def draw_spiral(c, arc, r, growth, size):
    color(c)
    pensize(size)
    for a in range(arc):
        down()
        circle(r, 90)
        r = r + growth
        up()
def draw_from_file(filename):          
    with open(filename) as target:
        for i in target:
            rows = i.split(",")
            for a, part in enumerate(rows):
                rows[a] = part.strip()
            colour = rows[0]
            arc = int(rows[1])
            radius = int(rows[2])
            radius_growth = float(rows[3])
            pen_weight = int(rows[4])
            draw_spiral(colour, arc, radius, radius_growth, pen_weight)


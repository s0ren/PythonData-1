#!/usr/bin/env python3

import math

def triangle(g, h):
    return float(g) * float(h) / 2

def ui_triangle():
    g = input("Give base of the triangle: ")
    h = input("Give height of the triangle: ")
    return g, h

def rectangle(b, h):
    return float(b) * float(h)

def ui_rectangle():
    b = input("Give width of the rectangle: ")
    h = input("Give height of the rectangle: ")
    return b, h

def circle(r):
    return math.pi * float(r)**2

def ui_circle():
    r = input("Give radius of the circle: ")
    return r

def main():
    while (shape := input("Choose a shape (triangle, rectangle, circle): ") )!= '':
        if shape == 'triangle':
            print('The area is {:.6f}'.format(triangle(*ui_triangle())))
        elif shape == 'rectangle':
            print('The area is {:.6f}'.format(rectangle(*ui_rectangle())))
        elif shape == 'circle':
            print(f'The area is {circle(ui_circle()) :.6f}')
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()

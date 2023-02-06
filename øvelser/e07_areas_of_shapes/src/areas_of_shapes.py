#!/usr/bin/env python3

import math


def main():
    def triangle():
        b = float(input('Give base of the triangle: '))
        h = float(input('Give height of the triangle: '))
        return f"{0.5*b*h:.6f}"
    
    def rectangle():
        b = float(input('Give base of the rectangle: '))
        h = float(input('Give height of the rectangle: '))
        return f"{b*h:.6f}"
    
    def circle():
        r = float(input('Give radius of circle: '))
        return f"{math.pi * r**2 :.6f}"
    
    fortsæt = True
    while fortsæt:
        shape = input('Choose a shape (triangle, rectangle, circle): ')
        if shape == '':
            fortsæt = False
        elif shape == 'triangle':
            print('The area is', triangle())
        elif shape == 'rectangle':
            print('The area is', rectangle())
        elif shape == 'circle':
            print('The area is', circle())
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()

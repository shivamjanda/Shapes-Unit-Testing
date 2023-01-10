# Shivam Janda and Jade Bedlington
# Lab3_Jade_Shivam.py
# November 5th, 2022
# Description: This file has all the fixtures to calculate the area of each shape.

from math import pi


def rhombus_area(d1, d2):
    if not isinstance(d1, int) and not isinstance(d1, float):
        raise ValueError('d1 should be a number')
    elif not isinstance(d2, int) and not isinstance(d2, float):
        raise ValueError('d2 should be a number')
    elif d1 < 0:
        raise ValueError('a of ellipse should be greater than 0')
    elif d2 < 0:
        raise ValueError('b of ellipse should be greater than 0')
    return (d1 * d2) / 2


def circle_area(r):
    if not isinstance(r, int) and not isinstance(r, float):
        raise ValueError('Radius should be a number')
    elif r < 0:
        raise ValueError('Radius of circle should be greater than 0')

    area = pi * (r ** 2)
    return area


def trapezium_area(b1, b2, h):
    if not isinstance(b1, int) and not isinstance(b1, float):
        raise ValueError('Base 1 should be a number')
    elif not isinstance(b2, int) and not isinstance(b2, float):
        raise ValueError('Base 2 should be a number')
    elif not isinstance(h, int) and not isinstance(h, float):
        raise ValueError('Base 3 should be a number')
    elif b1 < 0:
        raise ValueError('B1 should be greater than zero')
    elif b2 < 0:
        raise ValueError('B2 should be greater than zero')
    elif h < 0:
        raise ValueError('h should be greater than zero')

    return ((b1 + b2) / 2) * h


def ellipse_area(a, b):
    if not isinstance(a, int) and not isinstance(a, float):
        raise ValueError('a should be a number')
    elif not isinstance(b, int) and not isinstance(b, float):
        raise ValueError('b should be a number')
    elif a < 0:
        raise ValueError('a of ellipse should be greater than 0')
    elif b < 0:
        raise ValueError('b of ellipse should be greater than 0')

    return pi * (a * b)

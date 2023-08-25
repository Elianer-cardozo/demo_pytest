# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1141vudL8HirQly2GegXPe7FWis3ntrKc
"""

pip install pytest

def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Not a triangle'
    elif a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'

def test_triangle_is_equilateral():
    assert triangle_type(5,5,5) == 'Equilateral'

def test_triangle_is_isoceles():
    assert triangle_type(3,5,3) == 'Isosceles'

def test_triangle_is_scalene():
    assert triangle_type(7,8,9) == 'Scalene'

def test_not_a_triangle():
    assert triangle_type(1,2,3) == 'Not a triangle'
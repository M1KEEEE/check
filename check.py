"""
480 x 360

размер - количество
12 - 50
8 - 100
"""

def show_squares(width, height):
    square = width * height
    for i in range(2, min(width, height)):
        if width % i == 0 and height % i == 0:
            print(i, square / (i * i))



show_squares(480, 360)
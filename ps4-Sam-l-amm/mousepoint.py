"""
Name:
Collaborators:
Date:
Description:
"""
from graphics import *

min_x = 100
min_y = 100
max_x = 200
max_y = 200


def main():

    # Create the graphics window.
    win = GraphWin('Mouse Pointer', 300, 300)

    # Draw a rectangle using the graphics library.
    rect = Rectangle(Point(min_x, min_y), Point(max_x, max_y))
    rect.setFill('blue')
    rect.draw(win)



    while True:
        # For now, all your code must be within this loop.
        # Without the loop, you would only be able to click once!
        mouse_point = win.getMouse()
        print(mouse_point)
        mouse_x = mouse_point.getX()
        mouse_y = mouse_point.getY()
        mouse_in_rectangle(rect, mouse_x, mouse_y, min_x, min_y, max_x, max_y)
        print('x: ', mouse_x, ', y: ', mouse_y)


def mouse_in_rectangle(rect, mouse_x, mouse_y, min_x, min_y, max_x, max_y):
    if (min_x <= mouse_x <= max_x) and (min_y <= mouse_y <= max_y):
        rect.setFill('green')
        print('green')
    else:
        rect.setFill('red')


# Run this file to test your solution!
if __name__ == '__main__':
    from ps4_unit_tests import run_tests, MousepointTests
    run_tests(MousepointTests)
    main()

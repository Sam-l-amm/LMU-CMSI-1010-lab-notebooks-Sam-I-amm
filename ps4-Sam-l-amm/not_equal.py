"""
Name:
Collaborators:
Date:
Description: This program implements our own version of the != operator.
"""
a = 2
b = 2
c = 5
d = 7
not_equal_test1 = None

def not_equal(a, b):
    if a == b:
        return False
    elif a is not b:
        return True
    


# UNIT TESTS -- Run this file to check your work!
if __name__ == '__main__':
    from ps4_unit_tests import run_tests, NotEqualTests
    run_tests(NotEqualTests)

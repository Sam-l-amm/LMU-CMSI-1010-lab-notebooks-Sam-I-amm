"""
Name:
Collaborators:
Date:
Description: This program finds the midpoint of a list of numbers.
"""
my_list = []

def midpoint(my_list):
    if not my_list:
        return None
    length = int(len(my_list))

   

    if length % 2 == 0:
        evenNumber1 = (length / 2)
        evenNumber2 = (length / 2)
        average = ((evenNumber1 + 1) + (evenNumber2)) / 2
        print("even numbers are ", evenNumber1, evenNumber2)
        

        print("Average is ", average)
        return(average)

    elif length % 2 != 0:
        oddNumber = length // 2
        print(oddNumber)
        return my_list[oddNumber]


midpoint(my_list)

if __name__ == '__main__':
    from ps4_unit_tests import run_tests, MidpointTests
    run_tests(MidpointTests)

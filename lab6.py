import random
# TODO: count_character is given a string s and a character c and returns the number
# of occurrences of c in s
def count_character(s, c):
    counter = 0
    for char in s:
        if char == c:
            counter += 1
    return counter

# Debugging function calls. You can add more or change
# The following should return 3
char_count = count_character('banana', 'a')
print(char_count)


# The following call should return 4
char_count = count_character('mississippi', 's')
print(char_count)

# The following tests your code. Do not modify it.
#assert (count_character('banana', 'a') == 3)
#assert (count_character('mississippi', 's') == 4)
#assert (count_character('loyola', 'l') == 2)

###############################################################################


# TODO: repeat_string is given the string s and returns a string that is n copies
# of it.
def repeat_string(s:str, n:str):
    out = ''
    for amountOfRepeats in range(n):
        out += s
    return out

print(repeat_string('hello', 3))

# The code below tests your function. Do not modify it.
#assert(repeat_string('hello', 3) == 'hellohellohello')
#assert(repeat_string('hi', 5) == 'hihihihihi')

##################################################################################


name1 = input('Please enter a FIRST NAME followed by a LAST NAME separated by a space:')
name2 = input('Please enter another FIRST NAME followed by a LAST NAME separated by a space:')

# TODO: Now process the user input to find the first names and last names
# Right now you have strings containing both, so find the space first
# and save the first name substrings and the last name substrings in separate variables
# If you prefer, you can also use split() to separate the first and last names


# TODO: In order to mix up the strings you need to find the midpoint of each name
# Challenge: How could you split strings at random points instead?

firstnamesplit = name1.split()
secondnamesplit = name2.split()


random.shuffle(firstnamesplit)
random.shuffle(secondnamesplit)



# TODO: Get the substrings for the first halves and second halves of each name
# You want to combine the names to create 2 new first and last names
# Make sure the capitalization is correct
# Use capitalize() to capitalize and lower() to make all lowercase
# Combine the first half of the first first name and the second half of the second
# first name to create a new first name




# TODO: Combine the first half of the first last name and the second half of the second
# last name to create a new last name

newName1 = (firstnamesplit[0] + ' ' + secondnamesplit[0])
newName2 = (firstnamesplit[1] + ' ' + secondnamesplit[1])




# print out both new names
# you do not need to change the following code.
print('Here are the new mixed up names:')
print(newName1)
print(newName2)

#assert(new_first_name1 != '')
#assert(new_first_name2 != '')
#assert(new_last_name1 != '')
#assert(new_last_name2 != '')
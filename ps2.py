import math
import random

famous_person = "Neil Armstrong"
their_quote = "That's one small step for a man, a giant leap for mankind."
favorite_number = 7
print("My favorite number is: " + str(favorite_number))
assert favorite_number >= 0

#######################################################################################################

print("{}, at age {}, said:\n\n\"{}\"".format(famous_person, favorite_number, their_quote))

assert len(famous_person) > 0
assert len(their_quote) > 0

########################################################################################################

line1 = 'Python supports multiple programming paradigms, including object-oriented, imperative\n'
line2 = '  and functional programming or procedural styles. It features a dynamic type\n'
line3 = ' system and automatic memory management and has a large and comprehensive standard library.\n '

strippedText = line1.strip(), line2.strip(), line3.strip()

print(strippedText)

#########################################################################################################

line1 = ' 495.59863 \n'
line2 = '\t134  '
line3 = '\n\t -5.4 \t'

num1 = line1.strip()
num2 = line2.strip()
num3 = line3.strip()
print(float(num1), float(num2), float(num3))

##########################################################################################################


number = 3.14159265359

strVersion = math.sqrt(number)

str(strVersion)

print(strVersion)


##########################################################################################################

def f1(x):
    print(x + 1)


def f2(x):
    return x + 1


f1(3)
f2(2)

# The return function is giving back a value that can be used by the computer,
# while the print is just printing to screen whatever string

############################################################################################################

a = f1(3)
b = f2(3)

a
b

#The values of A and B are both 4 I am getting this output because I am redefining f1 and f2 and having them rerun


#############################################################################################################

#f1(3) + 1
#f2(3) + 1

# I am getting an error code when running, I am getting this error because there are no
# parenthesis around f1(3) + 1 the corrected working code would look like, (f1(3) + 1)

# printing is useful when the user wants a readout, returning is useful when you want to declare
# a variable outside of def()

############################################################################################################

def b(z):
    print("this is z ", z)
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total) ** 2
    return square


x = 1
y = x + 1
print(c(x, y + 3, x + y))


######################################################################################
hi = 30
lo = 0





print("I made it here")
numberToGuess = random.randint(lo, hi)
print(numberToGuess)

print("Ready to guess? My number is between 0 and 30.")
guess = int(input("Enter your guess now:"))

while guess != numberToGuess or guess == numberToGuess:
    print("im here")
    if guess > numberToGuess:
        print("To high, guess again")
        guess = int(input("Guess again:"))
    elif guess < numberToGuess:
        print("To low, guess again")
        guess = int(input("Guess again:"))
    else:
        print("You guessed my number!")
        break
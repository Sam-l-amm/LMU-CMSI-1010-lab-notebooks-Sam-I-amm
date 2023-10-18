import random
coin = ''
position = 50
left_wall = 0
right_wall = 100
isHead = None
isHead2 = None
steps_right = 30
steps_left = 20


def coinFlip():
    global isHead
    flip = random.randint(1, 10)
    if flip <= 5:
      isHead = True
      print("Heads")
    else:
        isHead = False
        print("Tails")




coinFlip()

def secondCoinFlip():
    global isHead2
    secondFlip = random.randint(1, 10)
    if secondFlip <= 5:
      isHead2 = True
      print("Heads2")
    else:
        isHead2 = False
        print("Tails2")

secondCoinFlip()

def Movement():
    global position
    if (isHead == True) and (isHead2 == True):
        position = position + steps_right
        print("position and steps right ", position, steps_right)
    elif (isHead == False) and (isHead2 == False):
        position = position + steps_left
        print("position and steps left ", position, steps_left)
    else:
        if (isHead == True) or (steps_right > steps_left):
            position = position + (steps_right * 2)
            position = position + steps_left
            print("position and steps right *2 ", position, steps_right)
        else:
            position = position + (steps_left * 2)
            position = position + steps_right
            print("position and steps left *2 ", position, steps_right)
Movement()

def wallCorrect(right_wall, left_wall):
    global position
    if position > right_wall:
        position == 100
    elif position < left_wall:
        position == 0

wallCorrect(right_wall, left_wall)

print('You are at position', position, 'in the room.')

assert(0 <= position <= 100)


# Here we will have to practice using conditional statements also.
# We have already written code to set the random number of steps taken to the
# left or right
#steps_right = get_steps()
#steps_left = get_steps()

# For debugging you can set and change these values to check your conditions
# without coin flips. Can you figure out how to change these to test
# all the possible cases in your code that may occur?
#position = 50
#is_head1 = True
#is_head2 = True
#steps_right = 30
#steps_left = 20

#print('Your possible steps right are',  steps_right, 'or', 2*steps_right)
#print('Your possible steps left are',  steps_left, 'or', 2*steps_left)

# TODO: If both coin tosses were heads:
    # move yourself or your robot to the right
# TODO: But if both coin tosses are tails
#  (try to check this using an expression with `not`):
    # move yourself or robot to the left
# Otherwise:
    # TODO: If first toss is heads or steps right is greater than steps left:
        # move double number of steps right, and also the number of steps left
    # Otherwise:
        # move double number of steps left, and also the number of steps right





# Below, we make sure that your position does not exceed the left wall
# or the right wall, just as with the UFO.

# TODO: If your position is past left wall:
    # set it to the left wall
# TODO: But if your position is past the right wall:
    # set it to the right wall
"""
Name: Samuel Rambo
Date: 11/7/2023
Description: Highroller game
"""
import random
from random import randint



class Die():
    
    def __init__(self, initial_value, sides):
        self.sides = sides
        self.initial_value = 1
        pass

    def roll(self):
        self.initial_value = random.randint(1, self.sides)
        return self.initial_value
        pass

    def get_number_sides(self):
        return self._sides
        pass

    def get_current_value(self):
        return self._initial_value
        pass

    def __str__(self):
        return f'[{self._initial_value}]'
        pass

class DiceSet():

    def __init__(self, sides_each_die, number_of_dice):
        self.number_of_dice = number_of_dice
        self.sides_each_dice = sides_each_die
        self.dice = [Die(1, sides_each_die) for _ in range(number_of_dice)]
        
        pass

    def get_descriptor(self):
        return f'{self._number_of_dice}d{self._sides_each_die}'
        pass

    def get_total(self):
        result = die_set.roll_all()
        return(result)
        pass

    def roll_all(self):
        return [die.roll() for die in self.dice]
        pass

    def roll_all(self):
        return [die.roll() for die in self.dice]
        pass

    def get_current_values(self):
        
        pass

    def matches(self, dice_set):

        pass

    def __str__(self):

        pass

def main():
    print("Welcome to highroller dice game")
    number_of_dice = 0
    sides_each_dice = 0
    
    while True:

        command = input("Enter command or h or help for a command list: ")
        
        if command == 'h' or command == 'help':
            print('  q = quit', '\n', '<s> = declare amount of dice sides', '\n', '<n> = declare amount of dice', '\n', 'roll all = roll all dice')
        elif command =='q' or command == 'quit':
            print('Goodbye thank you for playing!')
            break
        elif command == '<s>':
            sides_each_dice = int(input("How many sides do you want your dice to have?: "))
            if number_of_dice < 0:
                print('you can now roll all dice')
            elif number_of_dice == 0:
                print('now set the number of dice before you can roll')
        elif command == '<n>':
            number_of_dice = int(input("How many dice would you like to roll?: "))
            if sides_each_dice < 0:
                print('you can now roll all dice')
            elif sides_each_dice == 0:
                print('now set the number of sides before you can roll')
        elif command == 'roll all':
            dice_set = DiceSet(sides_each_dice, number_of_dice)
            result = dice_set.roll_all()
            print(result)
        else:
            print('please only enter correct commmands!')


    
# Run this file to test your main program!
if __name__ == '__main__':
    main()



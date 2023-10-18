import random
totalCost = 0
print("Welcome in, what is your name?")
Name = input("Name:")
print("Thank you for coming in today " + Name + " can I get you something to drink?")
Drink = input("Drink:")
print(Drink + " is a great choice, can I get you anything to eat aswell?")
Food = input("Order:")
print("Okay just to repeat this back you would like " + Drink + " to drink and " + Food + " to eat")
totalBill = round(random.uniform(10, 30), 2)
tipTotal = random.randint(10, 25)
totalCost = totalBill + tipTotal
print("Wonderful! Your total bill is " + str(totalCost) + " we will have that food ready for you in a second")
print(" 1-Celsius to Fahrenheit")
print(" 2-Miles to Meters")
print(" 3-Total Bil")
calculate = int(input("What would you like to convert: "))

if calculate == 1:
    tempInC = int(input("What is your temperature in celsius?: "))
    tempInC = tempInC * 1.8 + 32
    print("This is your temperature in Fahrenheit " + str(tempInC))
elif calculate == 2:
    mileDistance = int(input("What distance in miles would you like to convert to meters?: "))
    mileDistance = mileDistance * 1609.34
    print("This is your total distance traveled in meters! " + mileDistance)
elif calculate == 3:
    price = int(input("What is your total bill cost?: "))
    tipPercent = int(input("What percentage will you tip?: "))
    tipPercent = tipPercent / 100
    price = price * tipPercent + price
    print("This is your total cost: " + str(price))
else:
    print("invalid choice")

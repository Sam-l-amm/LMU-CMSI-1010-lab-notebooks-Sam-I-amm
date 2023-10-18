

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0


print('After I have passed away, I want people to remember me as:')
print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')
firstQuestion = int(input("How would you like the be remembered?:"))

if firstQuestion == 1:
    gryffindor = gryffindor + 1
    print(gryffindor)
elif firstQuestion == 2:
    hufflepuff = hufflepuff + 1
    print(hufflepuff)
elif firstQuestion == 3:
    ravenclaw = ravenclaw + 1
    print(ravenclaw)
elif firstQuestion == 4:
    slytherin = slytherin + 1
    print(slytherin)
else:
    print("invalid choice")

print('Q2) Dawn or Dusk?')
print('  1) Dawn')
print('  2) Dusk')
secondQuestion = int(input("Dawn or Dusk?:"))

if secondQuestion == 1:
    gryffindor = gryffindor + 1
    ravenclaw = ravenclaw + 1
elif secondQuestion == 2:
    hufflepuff = hufflepuff + 1
    slytherin = slytherin + 1
else:
    print("invalid choice")

print('Which kind of instrument most pleases your ear?')
print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')
thirdQuestion = int(input("Instrument?:"))

if thirdQuestion == 1:
    slytherin = slytherin + 1
elif thirdQuestion == 2:
    hufflepuff = hufflepuff + 1
elif thirdQuestion == 3:
    ravenclaw = ravenclaw + 1
elif thirdQuestion == 4:
    gryffindor = gryffindor + 1
else:
    print("invalid choice")

print('Do roads in nature tempt you the most?')
print('  1) Yes')
print('  2) No')

fourthQuestion = int(input('Please enter a number to answer:'))

if fourthQuestion == 1:
    print("Which road tempts you the most?")
    print('  1) The wide, sunny grassy lane')
    print('  2) The twisting, leaf-strewn path through woods')
    fourthQuestionPT2 = int(input("Please enter a number to answer:"))
    if fourthQuestionPT2 == 1:
        hufflepuff = hufflepuff + 1
    elif fourthQuestionPT2 == 2:
        gryffindor = gryffindor + 1
elif fourthQuestion == 2:
    print("Which street would you prefer?:")
    print('  1) The narrow, dark, lantern-lit alley')
    print('  2) The cobbled street lined with ancient buildings')
    fourthQuestionPT3 = int(input("Please enter a number to answer:"))
    if fourthQuestionPT3 == 1:
        slytherin = slytherin + 1
    elif fourthQuestionPT3 == 2:
        ravenclaw = ravenclaw + 1

print("gryffindor:" + str(gryffindor))
print("slytherin:" + str(slytherin))
print("hufflepuff:" + str(hufflepuff))
print("ravenclaw:" + str(ravenclaw))

    
if gryffindor > max(ravenclaw, slytherin, hufflepuff):
    print("Congratulations you are a gryffindor!!")
elif ravenclaw > max(gryffindor, slytherin, hufflepuff):
    print("Congratulations you are a ravenclaw!!")
elif hufflepuff > max(gryffindor, slytherin, ravenclaw):
    print("Congratulations you are a hufflepuff!!")
else:
    print("Congratulations you are a slytherin!!")
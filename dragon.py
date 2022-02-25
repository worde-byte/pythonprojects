import random
import time


def intro():
    print('"You are in a land full of dragons. In front of you are two caves. In one cave is a friendly dragon, and the other is a mean dragon"')
    print()

treasure = 0

def getTreasure():
    return str(treasure)

def resetTreasure():
    global treasure
    treasure = 0

def incTreasure():
    global treasure
    treasure+=1

def chooseCave():
    myCave = 0
    print('"Which cave would you like to enter? Cave 1 or 2?"')
    while myCave != '1' and myCave != '2':
        print('Enter 1 or 2')
        myCave = input()

    return myCave

def checkCave(cave):
    print('You have chosen cave ' + str(cave))
    time.sleep(2)
    print('It is dark and spooky')
    time.sleep(3)
    print('A large dragon jumps out in front of you! He looks you up and down and...')
    print()
    time.sleep(4)

    goodCave = random.randint(1,2)
    if cave == str(goodCave):
        print('Gives you treasure!')
        incTreasure()
        time.sleep(1)
        print('You have ' + getTreasure() + ' treasure(s)!')
    else:
        print('Eats you!')
        print('You died with ' + getTreasure() + ' treasure(s)')
        resetTreasure()


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y' or playAgain == 'Y':
    intro()
    cave = chooseCave()
    checkCave(cave)

    print('Do you want to play again? (Y or N)')
    playAgain = input()

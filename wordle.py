import random
import time

def getTreasure():
    return str(treasure)

def resetTreasure():
    global treasure
    treasure = 0

def incTreasure():
    global treasure
    treasure+=1

def genWord():
    words = ["adult", "agent", "anger", "apple", "award", "basis", "beach", "birth", "block", "blood", "board", "brain", "bread", "break", "brown",
"buyer", "cause", "chain", "chair", "chest", "chief", "child", "claim", "class", "clock", "coach", "coast", "court", "cover", "cream", "crime", "cross", "crowd", "crown", "cycle", "dance", 
"death", "depth", "doubt", "draft", "drama", "dream", "dress", "drink", "drive", "earth", "enemy", "entry", "error", "event", "faith", "fault", 
"field", "fight", "final", "floor", "focus", "force", "frame", "frank", "front", "fruit", "glass", "grant", "grass", "green", "group", "guide", 
"heart", "horse", "hotel", "house", "image", "index", "input", "issue", "judge", "knife", "layer", "level", "light", "limit", "lions", "lunch", "major", "march", "match", "metal", "model", "money", "month", "motor", "mouth", "music", "night", "noise", 
"north", "novel", "nurse", "offer", "order", "other", "owner", "panel", "paper", "party", "peace", "phase", "phone", "piece", "pilot", 
"pitch", "place", "plane", "plant", "plate", "point", "pound", "power", "press", "price", "pride", "prize", "proof", "queen", "radio", "range", 
"ratio", "reply", "right", "river", "round", "route", "rugby", "scale", "scene", "scope", "score", "sense", "shape", "share", "sheep", "sheet", 
"shift", "shirt", "shock", "sight", "skill", "sleep", "smile", "smith", "smoke", "sound", "south", "space", "speed", "spite", "sport", 
"squad", "squid", "staff", "stage", "start", "state", "steam", "steel", "stock", "stone", "store", "study", "stuff", "style", "sugar", "table", "taste", 
"theme", "thing", "title", "total", "touch", "tower", "track", "trade", "train", "trend", "trial", "trust", "truth", "uncle", "union", 
"unity", "value", "video", "visit", "voice", "waste", "watch", "water", "while", "white", "whole", "woman", "world", "youth", "yacht", "yards", "zappy", "zumba"]
    i = random.randint(0, len(words)-1)
    return words[i]

def checkWord(guess, word):
    word = split(word)
    guess = split(guess)
    for i in range(5):
        if guess[i] == word[i]:
            print('There is a ' + str(guess[i]) + ' at position ' + str(i+1))
    j = 4
    while j>=0:
        if guess[j] == word[j]:
            guess.pop(j)
            word.pop(j)
        j-=1
    j = len(guess)-1
    while j>=0:
        if guess[j] in word:
            print('There is a ' + guess[j] + ' but you have it at the wrong position.')
            word.remove(guess[j])
            guess.pop(j)
        j-=1

def split(word):
    return [char for char in word]
        

def checkGuess(guess, word):
    time.sleep(1)
    incTreasure()
    if guess==word:
        print('You got it in ' + getTreasure() + ' guesses!')
    else:
        checkWord(guess, word)
        
def intro():
    print('Welcome to Worden, I am thinking of a 5 letter word, can you guess it?')
    print('I will provide hints along the way to help you out. Good luck!')
    print('Note: Please only guess lowercase letters')


playAgain = 'yes'
treasure = 0
while playAgain == 'yes' or playAgain == 'y' or playAgain == 'Y' or playAgain == 'Yes':
    intro()
    word = genWord()
    guess = ''
    while guess!=word:
        if int(getTreasure())>20:
            print("The word is " + word + " please enter it as your guess to start a new round")
        print('What is your guess?')
        guess = input()
        while len(guess)!=5:
            print("Please ensure your guess is 5 letters")
            guess = input()
        checkGuess(guess, word)
    print('Do you want to play again? (Y or N)')
    resetTreasure()
    playAgain = input()

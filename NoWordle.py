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
    words = 'young blood drink alone piece drunk debts stage false demon doubt holes alive heart light crowd alien heels grace break cynic green notes fears saved write hopes roads dream miles alibi abyss water tidal coast alone drift jaded anger teeth wires haunt maine lover ocean songs empty black blind caves sober older crazy sworn booze honey carlo trail raged light alive grief anger tired glass sharp break sorry close flaws drive covid stick split'.split()
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

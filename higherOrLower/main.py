#Import modules
import random
import sys

import art
import gameData

#A function to add two choices to a list to later be extracted
#The don't break is to fix the issue of running into pulling two of the same values from the dictionary.
def generate(optionOne):
    dontBreak = 0
    for i in range(1,3):
        numGen = random.randint(1, len(gameData.data))
        while numGen == dontBreak:
            numGen = random.randint(1, len(gameData.data))
        optionOne.append(gameData.data[numGen - 1])
        dontBreak = numGen
    return optionOne

def compareOptions(optionsList):
    a = 0
    if optionsList[0]['follower_count'] > optionsList[1]['follower_count']:
        a += 1
    elif optionsList[0]['follower_count'] < optionsList[1]['follower_count']:
        a += 2
    else:
        a += 3
    return a

def printResults(options):
    print(f"\n{options[0]['name']} has {options[0]['follower_count']} followers.")
    print(f"{options[1]['name']} has {options[1]['follower_count']} followers.\n")




def higherOrLower():
    #Print the logo
    print(art.logo)
    #instantiate variables
    usrScore = 0
    #While loop to keep game going until user guesses wrong
    gameOver = False
    while gameOver != True:
        print(f"Your score is {usrScore}")
        option = []
    #populate option one and two
        option = generate(option)
    #compare options one and two, value == (1 = a, 2 = b, 3 = tie)
        value = 0
        value = compareOptions(option)
    #Print options one and two
        print(f"Compare A: {option[0]['name']}, a {option[0]['description']}, from {option[0]['country']}")
        print(art.vs)
        print(f"Against B: {option[1]['name']}, a {option[1]['description']}, from {option[1]['country']}")
    #Gather user input
        usrGuess = input("Who has more followers? Type 'A' or 'B': ").lower()
    #compare to most popular option
        if usrGuess == 'a' and value == 1:
            usrScore += 1
        elif usrGuess == 'a' and value == 2:
            gameOver = True
        elif usrGuess == 'b' and value == 2:
            usrScore += 1
        else:
            gameOver = True
        printResults(option)
    print(f"Your final score is: {usrScore}")

higherOrLower()
playAgain = input("If you want to play again, press 'y'. Otherwise, press any other key.")
if playAgain == 'y':
    higherOrLower()
else:
    sys.exit("Thank you for playing")

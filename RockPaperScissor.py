import os
import random

os.system('cls')

# creates a dashline
def dashline():
    print('------------------------------------------')

# handles random computer play
def computerPlay():
    computerint = random.randint(0,2)
    if computerint == 0:
        return 'rock'
    elif computerint == 1:
        return 'paper'
    else:
        return'scissor'

# handles game logic
def playRockPaperScissor():
    os.system('cls')
    while True: # continutes game until there is a winner
        userinput = input('Rock Paper Scissor Says Shoot!\nSelect from the following option:\n1) Rock\n2) Paper\n3) Scissor\n')
        os.system('cls')
        # converts all possible user inputs to standard
        if userinput.lower() in ['1', 'one', 'rock', 'r']:
            userinput = 'rock'
        elif userinput.lower() in ['2', 'two', 'paper', 'p']:
            userinput = 'paper'
        elif userinput.lower() in ['3', 'three', 'scissor', 's']:
            userinput = 'scissor'
        else:
            print('That was not a valid input\nPlease input something else')
            dashline()

        computer = computerPlay()
        # decides who wins
        if userinput == computer:
            print(f"Your enemy selected {computer}, It's a tie!\nPlay another round")
            dashline()
        elif (userinput == 'rock' and computer == 'paper') or (userinput == 'paper' and computer == 'scissor') or (userinput == 'scissor' and computer == 'rock'):
            print(f'Your enemy selected {computer}, You Lose!')
            dashline()
            return 0
        elif (userinput == 'rock' and computer == 'scissor') or (userinput == 'paper' and computer == 'rock') or (userinput == 'scissor' and computer == 'paper'):
            print(f'Your enemy selected {computer}, You Win!')
            dashline()
            return 1

scoreCount = {'user': 0, 'computer': 0} #initializes score count when program is ran  
while True: # holds user in game until quits
    mainmenu = input(f'The ulitmate rock paper scissor show down!\n\nThe current score count is:\n\nYou:        {scoreCount["user"]}\nYour Enemy: {scoreCount["computer"]}\n\nDo you want to:\n1) Play a round of rock-paper-scissors\n2) Quit\n')
    os.system('cls')
    if mainmenu.lower() in ['1', 'one', 'yes', '', 'yeah', 'y', 'play', 'play a round', 'Play a round of rock-paper-scissors', 'rock-paper-scissors', 'rock', 'rock paper scissors']: # all possible user inputs for wanting to play
        result = playRockPaperScissor()
        # increases score count based on result
        if result == 0:
            scoreCount["computer"] += 1
        elif result == 1:
            scoreCount["user"] += 1
    elif mainmenu.lower() in ['2', 'two', 'quit', 'q']:
        print('See you later alligator!\n')
        break
    else:
        print('That was not a valid input\nPlease input something else')
        dashline()
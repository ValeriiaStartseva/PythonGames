import random

print('welcome to Tic Tac Toe')
print('----------------------')

possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3

def printGameBoard():
    for x in range(rows):
        print('\n+---+---+---+')
        print('|', end="")
        for y in range(cols):
            print('', gameBoard[x][y], end=' |')
    print('\n+---+---+---+')

def modifyArray(num, turn):
    num -= 1
    if num == 0:
        gameBoard[0][0] = turn
    elif num == 1:
        gameBoard[0][1] = turn
    elif num == 2:
        gameBoard[0][2] = turn
    elif num == 3:
        gameBoard[1][0] = turn
    elif num == 4:
        gameBoard[1][1] = turn
    elif num == 5:
        gameBoard[1][2] = turn
    elif num == 6:
        gameBoard[2][0] = turn
    elif num == 7:
        gameBoard[2][1] = turn
    elif num == 8:
        gameBoard[2][2] = turn

def checkForWinner(gameBoard):
    # X axis
    if gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][2] == 'X':
        print('X won`!')
        return 'X'
    elif gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O':
        print('O won`!')
        return 'O'
    elif gameBoard[1][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[1][2] == 'X':
        print('X won`!')
        return 'X'
    elif gameBoard[1][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[1][2] == 'O':
        print('O won`!')
        return 'O'
    elif gameBoard[2][0] == 'X' and gameBoard[2][1] == 'X' and gameBoard[2][2] == 'X':
        print('X won`!')
        return 'X'
    elif gameBoard[2][0] == 'O' and gameBoard[2][1] == 'O' and gameBoard[2][2] == 'O':
        print('O won`!')
        return 'O'
    # Y axis
    if gameBoard[0][0] == 'X' and gameBoard[1][0] == 'X' and gameBoard[2][0] == 'X':
        print('X won`!')
        return 'X'
    elif gameBoard[0][0] == 'O' and gameBoard[1][0] == 'O' and gameBoard[2][0] == 'O':
        print('O won`!')
        return 'O'
    elif gameBoard[0][1] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][1] == 'X':
        print('X won`!')
        return 'X'
    elif gameBoard[0][1] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][1] == 'O':
        print('O won`!')
        return 'O'
    elif gameBoard[0][2] == 'X' and gameBoard[1][2] == 'X' and gameBoard[2][2] == 'X':
        print('X won`!')
        return 'X'
    elif gameBoard[0][2] == 'O' and gameBoard[1][2] == 'O' and gameBoard[2][2] == 'O':
        print('O won`!')
        return 'O'
    # cross
    if gameBoard[0][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][2] == 'X':
        print('X won`!')
        return 'X'
    elif gameBoard[0][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][2] == 'O':
        print('O won`!')
        return 'O'
    elif gameBoard[0][2] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][0] == 'X':
        print('X won`!')
        return 'X'
    elif gameBoard[0][2] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][0] == 'O':
        print('O won`!')
        return 'O'
    else:
        return 'N'


leaveLoop = False
turnCounter = 0

while leaveLoop == False:
    # turn of player
    if turnCounter % 2 == 1:
        printGameBoard()
        while True:
            numberPicked = int(input('\nChoose a number [1=9]: '))
            if numberPicked not in possibleNumbers and 1 <= numberPicked <= 9:
                print('The field is busy. Choose another one.')
            elif 1 <= numberPicked <= 9:
                modifyArray(numberPicked, 'X')
                possibleNumbers.remove(numberPicked)
                break
            else:
                print('Invalid input. Choose another one.')

        turnCounter += 1
    # computer turn
    else:
        while True:
            cpuChoice = random.choice(possibleNumbers)
            print('\nCpu choice: ')
            if cpuChoice in possibleNumbers:
                modifyArray(cpuChoice, 'O')
                possibleNumbers.remove(cpuChoice)
                turnCounter += 1
                break
    winner = checkForWinner(gameBoard)
    if winner != "N":
        print("\nGame over! Thank you for playing :)")
        break









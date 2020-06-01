#-------- Global Variables --------

#If game is still going
gameStillGoing = True

#Who Win or Tie
winner = None

#Who's turn is it?
currentPlayer = 'X'



# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Display the game board to the screen
def displayBoard():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


def playGame():
    #dispaly inital board
    displayBoard()

    #Playing untill game over
    while gameStillGoing:


    #handel the single turns of an arbitrary palyer
        handleTurn(currentPlayer)

    #check if teh game has ended
        checkIfGameOver()
        
    #Filp to the other player
        flipPlayer()


    # The game has ended
    if (winner == 'X' or winner =='O'):
        print(winner+'   Won')
    elif winner == None:
        print('Game is Draw')
        


    





#handel the single turns of an arbitrary palyer
def handleTurn(player):

    print(player + "'s turn.")
    position = int(input('Choose a position from 1-9: '))

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in range(1,10):
            position = int(input('Choose a position from 1-9: '))

        # Get correct index in our board list
        position -=1
        
        # Then also make sure the spot is available on the board
        if board[position]=='-':
            valid = True
        else:
            print('You cant go there Try again')
        # Put the game piece on the board
    board[position]= player
    # Show the game board
    displayBoard()




def checkIfGameOver():
    checkForWinner()
    checkForDraw()

def checkForWinner():
    #set up global variables(because to change value of it inside functions)
    global winner


    # check row
    rowWinner = checkRows()
    # check columns
    columnWinner = checkColumns()
    # check diagonals
    diagonalWinner = checkDiagonals()

    if rowWinner:
        #there is win
        winner = rowWinner
    elif columnWinner:
        #there is win 
        winner = columnWinner
    elif diagonalWinner:
        #there is win
        winner = diagonalWinner
    else:
        # there is no win
        winner = None

    return


def checkRows():
    #set up global variables(because to change value of it inside functions)
    global gameStillGoing 

    #check if any rows have same value or not

    row1 = board[0] == board[1] == board [2] != '-'
    row2 = board[3] == board[4] == board [5] != '-'
    row3 = board[6] == board[7] == board [8] != '-'

    #if any row is same then flag value of game still going
    if (row1 or row2 or row3):
        gameStillGoing = False

    #say who is winner
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def checkColumns():
    #set up global variables(because to change value of it inside functions)
    global gameStillGoing 

    #check if any column have same value or not

    column1 = board[0] == board[3] == board [6] != '-'
    column2 = board[1] == board[4] == board [7] != '-'
    column3 = board[2] == board[5] == board [8] != '-'

    #if any column is same then flag value of game still going
    if (column1 or column2 or column3):
        gameStillGoing = False

    #say who is winner
    if column1:
        return board[0]
    elif column2:
        return board[3]
    elif column3:
        return board[6]
    return


def checkDiagonals():
    #set up global variables(because to change value of it inside functions)
    global gameStillGoing 

    #check if any diagonal have same value or not

    diagonal1 = board[0] == board[4] == board [8] != '-'
    diagonal2 = board[2] == board[4] == board [6] != '-'
    

    #if any diagonal is same then flag value of game still going
    if (diagonal1 or diagonal2 ):
        gameStillGoing = False

    #say who is winner
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[4]

    return





def checkForDraw():
    #set up global variables(because to change value of it inside functions)
    global gameStillGoing
    if '-' not in board:
        gameStillGoing = False

    return


def flipPlayer():
    # To change value of gobal palyer 
    global currentPlayer

    #if x was a palyer
    if currentPlayer=='X':
        currentPlayer='O'

    #if O was a palyer   
    elif currentPlayer == 'O' :
        currentPlayer = 'X'
        
    return





playGame()











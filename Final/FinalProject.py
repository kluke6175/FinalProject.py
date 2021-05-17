import random

def inputPlayerLetter():
    '''Lets the player choose which letter they want to be.
    
    Returns a list with player 1's letter as the first item,
    and player 2's letter as the second.'''
    letter = None
    allowed_letters = ['X', 'O']
    prompt = 'Player 1, Do you want to be X or O? '
    while letter not in allowed_letters:
        letter = input(prompt).upper()
    return ['X', 'O'] if letter.upper() == 'X' else ['O', 'X']

def whoGoesFirst(p1, p2):
    '''Randomly choose the player who goes first.'''
    return p1 if random.randint(0, 1) == 0 else p2

def togglePlayer(currentPlayer):
    '''Returns the letter of the next player'''
    return 'O' if currentPlayer == 'X' else 'X'

def playAgain():
    '''This function returns True if the player wants to play again, otherwise
    it returns False.'''
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

class TicTacToe:
    '''A game of TicTacToe'''
    board = None
    p1 = None
    p2 = None
    
    def start(self):
        '''Starts a game loop of TicTacToe'''
        
        print('Welcome to Tic Tac Toe!')
        self.board = [' '] * 10
        self.p1, self.p2 = inputPlayerLetter()
        turn = whoGoesFirst(self.p1, self.p2)
        print(turn + ' will go first.')
        
        gameIsPlaying = True
        while gameIsPlaying:
            self.drawBoard()
            move = self.getPlayerMove(turn)
            self.makeMove(turn, move)

            if self.isWinner(turn):
                self.drawBoard()
                print('{} has won the game!'.format(turn))
                gameIsPlaying = False
            else:
                if self.isBoardFull():
                    self.drawBoard()
                    print('The game is a tie!')
                    gameIsPlaying = False
                    break
                else:
                    turn = togglePlayer(turn)

    def drawBoard(self):
        '''Displays the board.

        "board" is a list of 10 strings representing the board (ignore index 0)'''
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')

    def getPlayerMove(self, letter):
        '''Prompt the player to type in their move.'''
        move = None
        while move not in range(1,10) or not self.isSpaceFree(move):
            print('What is your next move, {}? (1-9)'.format(letter))
            move = int(input())
        return move

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isWinner(self, letter):
        '''Given a board and a player's letter, this function returns True if
        that player has won. We use bo instead of board and le instead of
        letter so we don't have to type as much.'''
        return (
            (self.board[7] == letter and self.board[8] == letter and self.board[9] == letter) or # across the top
            (self.board[4] == letter and self.board[5] == letter and self.board[6] == letter) or # across the middle
            (self.board[1] == letter and self.board[2] == letter and self.board[3] == letter) or # across the bottom
            (self.board[7] == letter and self.board[4] == letter and self.board[1] == letter) or # down the left side
            (self.board[8] == letter and self.board[5] == letter and self.board[2] == letter) or # down the middle
            (self.board[9] == letter and self.board[6] == letter and self.board[3] == letter) or # down the right side
            (self.board[7] == letter and self.board[5] == letter and self.board[3] == letter) or # diagonal
            (self.board[9] == letter and self.board[5] == letter and self.board[1] == letter)    # diagonal
        )

    def isBoardFull(self):
        '''Return True if every space on the board has been taken.
        Otherwise return False.'''
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    def isSpaceFree(self, move):
        '''Return true if the passed move is free on the passed board.'''
        return self.board[move] == ' '


while True:
    game = TicTacToe()
    game.start()
    if not playAgain():
        break

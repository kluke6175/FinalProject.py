import random

class TicTacToe:
    '''A game of TicTacToe'''
    board = None
    p1 = None
    p2 = None
    
    def start(self):
        '''Starts a game loop of TicTacToe'''
        
        print('Welcome to Tic Tac Toe!')
        self.board = Board()
        self.p1, self.p2 = self.inputPlayerLetter()
        player = self.whoGoesFirst(self.p1, self.p2)
        print(player + ' will go first.')
        
        gameIsPlaying = True
        while gameIsPlaying:
            self.board.draw()
            move = self.getMove(player)
            self.board.makeMove(player, move)

            if self.board.isWinner(player):
                self.board.draw()
                print('{} has won the game!'.format(player))
                gameIsPlaying = False
            else:
                if self.board.isFull():
                    self.board.draw()
                    print('The game is a tie!')
                    gameIsPlaying = False
                    break
                else:
                    player = self.togglePlayer(player)

    def getMove(self, letter):
        '''Prompt the player to type in their move.'''
        move = None
        while not self.board.isValidMove(move):
            print('What is your next move, {}? (1-9)'.format(letter))
            move = int(input())
        return move

    def inputPlayerLetter(self):
        '''Lets the player choose which letter they want to be.
        
        Returns a list with player 1's letter as the first item,
        and player 2's letter as the second.'''
        letter = None
        allowed_letters = ['X', 'O']
        prompt = 'Player 1, Do you want to be X or O? '
        while letter not in allowed_letters:
            letter = input(prompt).upper()
        return ['X', 'O'] if letter.upper() == 'X' else ['O', 'X']

    def whoGoesFirst(self, p1, p2):
        '''Randomly choose the player who goes first.'''
        return p1 if random.randint(0, 1) == 0 else p2

    def togglePlayer(self, currentPlayer):
        '''Returns the letter of the next player'''
        return 'O' if currentPlayer == 'X' else 'X'

    def playAgain(self):
        '''This function returns True if the player wants to play again, otherwise
        it returns False.'''
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')


class Board:
    boxes = None

    def __init__(self):
        self.boxes = [' '] * 10

    def draw(self):
        '''Displays the board.
        "board" is a list of 10 strings representing the board (ignore index 0)'''
        print('   |   |')
        print(' ' + self.boxes[1] + ' | ' + self.boxes[2] + ' | ' + self.boxes[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.boxes[4] + ' | ' + self.boxes[5] + ' | ' + self.boxes[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.boxes[7] + ' | ' + self.boxes[8] + ' | ' + self.boxes[9])
        print('   |   |')

    def isFull(self):
        '''Return True if every space on the board has been taken.
        Otherwise return False.'''
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    def isSpaceFree(self, box):
        '''Return true if the specified box is free on this board.'''
        return self.boxes[box] == ' '

    def isWinner(self, letter):
        '''Returns True if letter has won.'''
        return (
            (self.boxes[7] == letter and self.boxes[8] == letter and self.boxes[9] == letter) or # across the top
            (self.boxes[4] == letter and self.boxes[5] == letter and self.boxes[6] == letter) or # across the middle
            (self.boxes[1] == letter and self.boxes[2] == letter and self.boxes[3] == letter) or # across the bottom
            (self.boxes[7] == letter and self.boxes[4] == letter and self.boxes[1] == letter) or # down the left side
            (self.boxes[8] == letter and self.boxes[5] == letter and self.boxes[2] == letter) or # down the middle
            (self.boxes[9] == letter and self.boxes[6] == letter and self.boxes[3] == letter) or # down the right side
            (self.boxes[7] == letter and self.boxes[5] == letter and self.boxes[3] == letter) or # diagonal
            (self.boxes[9] == letter and self.boxes[5] == letter and self.boxes[1] == letter)    # diagonal
        )

    def makeMove(self, letter, box):
        self.boxes[box] = letter
    
    def isValidMove(self, move):
        return move in range(1,10) and self.isSpaceFree(move)


while True:
    game = TicTacToe()
    game.start()
    if not game.playAgain():
        break

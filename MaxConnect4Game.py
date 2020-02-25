#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import random
import sys
from copy import deepcopy

from anytree import Node, PreOrderIter, RenderTree


def playPieceOn(gameBoard, currentTurn, column):
    if not gameBoard[0][column]:
        for i in range(5, -1, -1):
            if not gameBoard[i][column]:
                gameBoard[i][column] = currentTurn
                return True
    return False


def checkPieceCountOn(gameBoard):
    pieceCount = sum(
        1 for row in gameBoard for piece in row if piece)


def evaluateBoard(gameBoard, maxPlayer):
    if checkPieceCountOn(gameBoard):
        player1Score = 0
        player2Score = 0

        # Check horizontally
        for row in gameBoard:
            # Check player 1
            if row[0:4] == [1] * 4:
                player1Score += 1
            if row[1:5] == [1] * 4:
                player1Score += 1
            if row[2:6] == [1] * 4:
                player1Score += 1
            if row[3:7] == [1] * 4:
                player1Score += 1
            # Check player 2
            if row[0:4] == [2] * 4:
                player2Score += 1
            if row[1:5] == [2] * 4:
                player2Score += 1
            if row[2:6] == [2] * 4:
                player2Score += 1
            if row[3:7] == [2] * 4:
                player2Score += 1

        # Check vertically
        for j in range(7):
            # Check player 1
            if (gameBoard[0][j] == 1 and gameBoard[1][j] == 1 and
                    gameBoard[2][j] == 1 and gameBoard[3][j] == 1):
                player1Score += 1
            if (gameBoard[1][j] == 1 and gameBoard[2][j] == 1 and
                    gameBoard[3][j] == 1 and gameBoard[4][j] == 1):
                player1Score += 1
            if (gameBoard[2][j] == 1 and gameBoard[3][j] == 1 and
                    gameBoard[4][j] == 1 and gameBoard[5][j] == 1):
                player1Score += 1
            # Check player 2
            if (gameBoard[0][j] == 2 and gameBoard[1][j] == 2 and
                    gameBoard[2][j] == 2 and gameBoard[3][j] == 2):
                player2Score += 1
            if (gameBoard[1][j] == 2 and gameBoard[2][j] == 2 and
                    gameBoard[3][j] == 2 and gameBoard[4][j] == 2):
                player2Score += 1
            if (gameBoard[2][j] == 2 and gameBoard[3][j] == 2 and
                    gameBoard[4][j] == 2 and gameBoard[5][j] == 2):
                player2Score += 1

        # Check diagonally

        # Check player 1
        if (gameBoard[2][0] == 1 and gameBoard[3][1] == 1 and
                gameBoard[4][2] == 1 and gameBoard[5][3] == 1):
            player1Score += 1
        if (gameBoard[1][0] == 1 and gameBoard[2][1] == 1 and
                gameBoard[3][2] == 1 and gameBoard[4][3] == 1):
            player1Score += 1
        if (gameBoard[2][1] == 1 and gameBoard[3][2] == 1 and
                gameBoard[4][3] == 1 and gameBoard[5][4] == 1):
            player1Score += 1
        if (gameBoard[0][0] == 1 and gameBoard[1][1] == 1 and
                gameBoard[2][2] == 1 and gameBoard[3][3] == 1):
            player1Score += 1
        if (gameBoard[1][1] == 1 and gameBoard[2][2] == 1 and
                gameBoard[3][3] == 1 and gameBoard[4][4] == 1):
            player1Score += 1
        if (gameBoard[2][2] == 1 and gameBoard[3][3] == 1 and
                gameBoard[4][4] == 1 and gameBoard[5][5] == 1):
            player1Score += 1
        if (gameBoard[0][1] == 1 and gameBoard[1][2] == 1 and
                gameBoard[2][3] == 1 and gameBoard[3][4] == 1):
            player1Score += 1
        if (gameBoard[1][2] == 1 and gameBoard[2][3] == 1 and
                gameBoard[3][4] == 1 and gameBoard[4][5] == 1):
            player1Score += 1
        if (gameBoard[2][3] == 1 and gameBoard[3][4] == 1 and
                gameBoard[4][5] == 1 and gameBoard[5][6] == 1):
            player1Score += 1
        if (gameBoard[0][2] == 1 and gameBoard[1][3] == 1 and
                gameBoard[2][4] == 1 and gameBoard[3][5] == 1):
            player1Score += 1
        if (gameBoard[1][3] == 1 and gameBoard[2][4] == 1 and
                gameBoard[3][5] == 1 and gameBoard[4][6] == 1):
            player1Score += 1
        if (gameBoard[0][3] == 1 and gameBoard[1][4] == 1 and
                gameBoard[2][5] == 1 and gameBoard[3][6] == 1):
            player1Score += 1

        if (gameBoard[0][3] == 1 and gameBoard[1][2] == 1 and
                gameBoard[2][1] == 1 and gameBoard[3][0] == 1):
            player1Score += 1
        if (gameBoard[0][4] == 1 and gameBoard[1][3] == 1 and
                gameBoard[2][2] == 1 and gameBoard[3][1] == 1):
            player1Score += 1
        if (gameBoard[1][3] == 1 and gameBoard[2][2] == 1 and
                gameBoard[3][1] == 1 and gameBoard[4][0] == 1):
            player1Score += 1
        if (gameBoard[0][5] == 1 and gameBoard[1][4] == 1 and
                gameBoard[2][3] == 1 and gameBoard[3][2] == 1):
            player1Score += 1
        if (gameBoard[1][4] == 1 and gameBoard[2][3] == 1 and
                gameBoard[3][2] == 1 and gameBoard[4][1] == 1):
            player1Score += 1
        if (gameBoard[2][3] == 1 and gameBoard[3][2] == 1 and
                gameBoard[4][1] == 1 and gameBoard[5][0] == 1):
            player1Score += 1
        if (gameBoard[0][6] == 1 and gameBoard[1][5] == 1 and
                gameBoard[2][4] == 1 and gameBoard[3][3] == 1):
            player1Score += 1
        if (gameBoard[1][5] == 1 and gameBoard[2][4] == 1 and
                gameBoard[3][3] == 1 and gameBoard[4][2] == 1):
            player1Score += 1
        if (gameBoard[2][4] == 1 and gameBoard[3][3] == 1 and
                gameBoard[4][2] == 1 and gameBoard[5][1] == 1):
            player1Score += 1
        if (gameBoard[1][6] == 1 and gameBoard[2][5] == 1 and
                gameBoard[3][4] == 1 and gameBoard[4][3] == 1):
            player1Score += 1
        if (gameBoard[2][5] == 1 and gameBoard[3][4] == 1 and
                gameBoard[4][3] == 1 and gameBoard[5][2] == 1):
            player1Score += 1
        if (gameBoard[2][6] == 1 and gameBoard[3][5] == 1 and
                gameBoard[4][4] == 1 and gameBoard[5][3] == 1):
            player1Score += 1

        # Check player 2
        if (gameBoard[2][0] == 2 and gameBoard[3][1] == 2 and
                gameBoard[4][2] == 2 and gameBoard[5][3] == 2):
            player2Score += 1
        if (gameBoard[1][0] == 2 and gameBoard[2][1] == 2 and
                gameBoard[3][2] == 2 and gameBoard[4][3] == 2):
            player2Score += 1
        if (gameBoard[2][1] == 2 and gameBoard[3][2] == 2 and
                gameBoard[4][3] == 2 and gameBoard[5][4] == 2):
            player2Score += 1
        if (gameBoard[0][0] == 2 and gameBoard[1][1] == 2 and
                gameBoard[2][2] == 2 and gameBoard[3][3] == 2):
            player2Score += 1
        if (gameBoard[1][1] == 2 and gameBoard[2][2] == 2 and
                gameBoard[3][3] == 2 and gameBoard[4][4] == 2):
            player2Score += 1
        if (gameBoard[2][2] == 2 and gameBoard[3][3] == 2 and
                gameBoard[4][4] == 2 and gameBoard[5][5] == 2):
            player2Score += 1
        if (gameBoard[0][1] == 2 and gameBoard[1][2] == 2 and
                gameBoard[2][3] == 2 and gameBoard[3][4] == 2):
            player2Score += 1
        if (gameBoard[1][2] == 2 and gameBoard[2][3] == 2 and
                gameBoard[3][4] == 2 and gameBoard[4][5] == 2):
            player2Score += 1
        if (gameBoard[2][3] == 2 and gameBoard[3][4] == 2 and
                gameBoard[4][5] == 2 and gameBoard[5][6] == 2):
            player2Score += 1
        if (gameBoard[0][2] == 2 and gameBoard[1][3] == 2 and
                gameBoard[2][4] == 2 and gameBoard[3][5] == 2):
            player2Score += 1
        if (gameBoard[1][3] == 2 and gameBoard[2][4] == 2 and
                gameBoard[3][5] == 2 and gameBoard[4][6] == 2):
            player2Score += 1
        if (gameBoard[0][3] == 2 and gameBoard[1][4] == 2 and
                gameBoard[2][5] == 2 and gameBoard[3][6] == 2):
            player2Score += 1

        if (gameBoard[0][3] == 2 and gameBoard[1][2] == 2 and
                gameBoard[2][1] == 2 and gameBoard[3][0] == 2):
            player2Score += 1
        if (gameBoard[0][4] == 2 and gameBoard[1][3] == 2 and
                gameBoard[2][2] == 2 and gameBoard[3][1] == 2):
            player2Score += 1
        if (gameBoard[1][3] == 2 and gameBoard[2][2] == 2 and
                gameBoard[3][1] == 2 and gameBoard[4][0] == 2):
            player2Score += 1
        if (gameBoard[0][5] == 2 and gameBoard[1][4] == 2 and
                gameBoard[2][3] == 2 and gameBoard[3][2] == 2):
            player2Score += 1
        if (gameBoard[1][4] == 2 and gameBoard[2][3] == 2 and
                gameBoard[3][2] == 2 and gameBoard[4][1] == 2):
            player2Score += 1
        if (gameBoard[2][3] == 2 and gameBoard[3][2] == 2 and
                gameBoard[4][1] == 2 and gameBoard[5][0] == 2):
            player2Score += 1
        if (gameBoard[0][6] == 2 and gameBoard[1][5] == 2 and
                gameBoard[2][4] == 2 and gameBoard[3][3] == 2):
            player2Score += 1
        if (gameBoard[1][5] == 2 and gameBoard[2][4] == 2 and
                gameBoard[3][3] == 2 and gameBoard[4][2] == 2):
            player2Score += 1
        if (gameBoard[2][4] == 2 and gameBoard[3][3] == 2 and
                gameBoard[4][2] == 2 and gameBoard[5][1] == 2):
            player2Score += 1
        if (gameBoard[1][6] == 2 and gameBoard[2][5] == 2 and
                gameBoard[3][4] == 2 and gameBoard[4][3] == 2):
            player2Score += 1
        if (gameBoard[2][5] == 2 and gameBoard[3][4] == 2 and
                gameBoard[4][3] == 2 and gameBoard[5][2] == 2):
            player2Score += 1
        if (gameBoard[2][6] == 2 and gameBoard[3][5] == 2 and
                gameBoard[4][4] == 2 and gameBoard[5][3] == 2):
            player2Score += 1

        if maxPlayer == 1:
            return (player1Score - player2Score)
        else:
            return (player2Score - player1Score)

    else:
        score = 0
        for i in range(6):
            if maxPlayer == 1:
                if 1 in gameBoard[i] and 2 not in gameBoard[i]:
                    score += 1
            else:
                if 2 in gameBoard[i] and 1 not in gameBoard[i]:
                    score += 1
        return score


class maxConnect4Game:
    def __init__(self):
        self.gameBoard = [[0 for i in range(7)] for j in range(6)]
        self.currentTurn = 1
        self.player1Score = 0
        self.player2Score = 0
        self.maxPlayer = 0
        self.pieceCount = 0
        self.gameFile = None
        self.MAX, self.MIN = 1000, -1000

    # Count the number of pieces already played
    def checkPieceCount(self):
        self.pieceCount = sum(
            1 for row in self.gameBoard for piece in row if piece)

    # Checks if game is over
    def isOver(self):
        return self.checkPieceCount() == 6 * 7

    # Output current game status to console
    def printGameBoard(self):
        print(' -----------------')
        for i in range(6):
            print(' |', end=''),
            for j in range(7):
                print('%d' % self.gameBoard[i][j], end=''),
            print('| ')
        print(' -----------------')

    # Output current game status to file
    def printGameBoardToFile(self):
        for row in self.gameBoard:
            self.gameFile.write(''.join(str(col) for col in row) + '\r\n')
        self.gameFile.write('%s\r\n' % str(self.currentTurn))

    # Place the current player's piece in the requested column
    def playPiece(self, column):
        if not self.gameBoard[0][column]:
            for i in range(5, -1, -1):
                if not self.gameBoard[i][column]:
                    self.gameBoard[i][column] = self.currentTurn
                    self.pieceCount += 1
                    return True
        return False

    # The AI section. Currently plays randomly.
    def aiPlay(self):
        randColumn = random.randrange(0, 7)
        result = self.playPiece(randColumn)
        if not result:
            self.aiPlay()
        else:
            print('\n\nmove %d: Player %d, column %d\n' %
                  (self.pieceCount, self.currentTurn, randColumn + 1))
            if self.currentTurn == 1:
                self.currentTurn = 2
            elif self.currentTurn == 2:
                self.currentTurn = 1

    # Returns optimal value for current player
    def getTree(self, depth):
        root = Node('root', board=self.gameBoard, score=self.MIN)
        for i in range(depth):
            for n in PreOrderIter(root, maxlevel=i):
                if len(n.children) == 0:
                    ('no kids')
                    for j in range(7):
                        tempBoard = deepcopy(n.board)
                        if i % 2 == 0:
                            value = self.MIN
                        else:
                            value = self.MAX
                        if playPieceOn(tempBoard, (self.currentTurn + i) % 2 + 1, j):
                            print('success')
                            node = Node('{},{}'.format(i, j),
                                        parent=n, board=tempBoard, score=value)

        return root

    # Implements depth-limited alpha-beta pruning
    def minimax(self):
        column = -1

        # First asign values to the leafs
        self.getTree()
        for n in PreOrderIter(root, maxlevel=i):
            if len(n.children) == 0:
                n.value = evaluateBoard(n.board)
        return column

    # Calculate the number of 4-in-a-row each player has
    def countScore(self):
        self.player1Score = 0
        self.player2Score = 0

        # Check horizontally
        for row in self.gameBoard:
            # Check player 1
            if row[0:4] == [1] * 4:
                self.player1Score += 1
            if row[1:5] == [1] * 4:
                self.player1Score += 1
            if row[2:6] == [1] * 4:
                self.player1Score += 1
            if row[3:7] == [1] * 4:
                self.player1Score += 1
            # Check player 2
            if row[0:4] == [2] * 4:
                self.player2Score += 1
            if row[1:5] == [2] * 4:
                self.player2Score += 1
            if row[2:6] == [2] * 4:
                self.player2Score += 1
            if row[3:7] == [2] * 4:
                self.player2Score += 1

        # Check vertically
        for j in range(7):
            # Check player 1
            if (self.gameBoard[0][j] == 1 and self.gameBoard[1][j] == 1 and
                    self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[1][j] == 1 and self.gameBoard[2][j] == 1 and
                    self.gameBoard[3][j] == 1 and self.gameBoard[4][j] == 1):
                self.player1Score += 1
            if (self.gameBoard[2][j] == 1 and self.gameBoard[3][j] == 1 and
                    self.gameBoard[4][j] == 1 and self.gameBoard[5][j] == 1):
                self.player1Score += 1
            # Check player 2
            if (self.gameBoard[0][j] == 2 and self.gameBoard[1][j] == 2 and
                    self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[1][j] == 2 and self.gameBoard[2][j] == 2 and
                    self.gameBoard[3][j] == 2 and self.gameBoard[4][j] == 2):
                self.player2Score += 1
            if (self.gameBoard[2][j] == 2 and self.gameBoard[3][j] == 2 and
                    self.gameBoard[4][j] == 2 and self.gameBoard[5][j] == 2):
                self.player2Score += 1

        # Check diagonally

        # Check player 1
        if (self.gameBoard[2][0] == 1 and self.gameBoard[3][1] == 1 and
                self.gameBoard[4][2] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][0] == 1 and self.gameBoard[2][1] == 1 and
                self.gameBoard[3][2] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][1] == 1 and self.gameBoard[3][2] == 1 and
                self.gameBoard[4][3] == 1 and self.gameBoard[5][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][0] == 1 and self.gameBoard[1][1] == 1 and
                self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][1] == 1 and self.gameBoard[2][2] == 1 and
                self.gameBoard[3][3] == 1 and self.gameBoard[4][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][2] == 1 and self.gameBoard[3][3] == 1 and
                self.gameBoard[4][4] == 1 and self.gameBoard[5][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][1] == 1 and self.gameBoard[1][2] == 1 and
                self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][2] == 1 and self.gameBoard[2][3] == 1 and
                self.gameBoard[3][4] == 1 and self.gameBoard[4][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][4] == 1 and
                self.gameBoard[4][5] == 1 and self.gameBoard[5][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][2] == 1 and self.gameBoard[1][3] == 1 and
                self.gameBoard[2][4] == 1 and self.gameBoard[3][5] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][4] == 1 and
                self.gameBoard[3][5] == 1 and self.gameBoard[4][6] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][4] == 1 and
                self.gameBoard[2][5] == 1 and self.gameBoard[3][6] == 1):
            self.player1Score += 1

        if (self.gameBoard[0][3] == 1 and self.gameBoard[1][2] == 1 and
                self.gameBoard[2][1] == 1 and self.gameBoard[3][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][4] == 1 and self.gameBoard[1][3] == 1 and
                self.gameBoard[2][2] == 1 and self.gameBoard[3][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][3] == 1 and self.gameBoard[2][2] == 1 and
                self.gameBoard[3][1] == 1 and self.gameBoard[4][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][5] == 1 and self.gameBoard[1][4] == 1 and
                self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][4] == 1 and self.gameBoard[2][3] == 1 and
                self.gameBoard[3][2] == 1 and self.gameBoard[4][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][3] == 1 and self.gameBoard[3][2] == 1 and
                self.gameBoard[4][1] == 1 and self.gameBoard[5][0] == 1):
            self.player1Score += 1
        if (self.gameBoard[0][6] == 1 and self.gameBoard[1][5] == 1 and
                self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][5] == 1 and self.gameBoard[2][4] == 1 and
                self.gameBoard[3][3] == 1 and self.gameBoard[4][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][4] == 1 and self.gameBoard[3][3] == 1 and
                self.gameBoard[4][2] == 1 and self.gameBoard[5][1] == 1):
            self.player1Score += 1
        if (self.gameBoard[1][6] == 1 and self.gameBoard[2][5] == 1 and
                self.gameBoard[3][4] == 1 and self.gameBoard[4][3] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][5] == 1 and self.gameBoard[3][4] == 1 and
                self.gameBoard[4][3] == 1 and self.gameBoard[5][2] == 1):
            self.player1Score += 1
        if (self.gameBoard[2][6] == 1 and self.gameBoard[3][5] == 1 and
                self.gameBoard[4][4] == 1 and self.gameBoard[5][3] == 1):
            self.player1Score += 1

        # Check player 2
        if (self.gameBoard[2][0] == 2 and self.gameBoard[3][1] == 2 and
                self.gameBoard[4][2] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][0] == 2 and self.gameBoard[2][1] == 2 and
                self.gameBoard[3][2] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][1] == 2 and self.gameBoard[3][2] == 2 and
                self.gameBoard[4][3] == 2 and self.gameBoard[5][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][0] == 2 and self.gameBoard[1][1] == 2 and
                self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][1] == 2 and self.gameBoard[2][2] == 2 and
                self.gameBoard[3][3] == 2 and self.gameBoard[4][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][2] == 2 and self.gameBoard[3][3] == 2 and
                self.gameBoard[4][4] == 2 and self.gameBoard[5][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][1] == 2 and self.gameBoard[1][2] == 2 and
                self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][2] == 2 and self.gameBoard[2][3] == 2 and
                self.gameBoard[3][4] == 2 and self.gameBoard[4][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][4] == 2 and
                self.gameBoard[4][5] == 2 and self.gameBoard[5][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][2] == 2 and self.gameBoard[1][3] == 2 and
                self.gameBoard[2][4] == 2 and self.gameBoard[3][5] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][4] == 2 and
                self.gameBoard[3][5] == 2 and self.gameBoard[4][6] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][4] == 2 and
                self.gameBoard[2][5] == 2 and self.gameBoard[3][6] == 2):
            self.player2Score += 1

        if (self.gameBoard[0][3] == 2 and self.gameBoard[1][2] == 2 and
                self.gameBoard[2][1] == 2 and self.gameBoard[3][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][4] == 2 and self.gameBoard[1][3] == 2 and
                self.gameBoard[2][2] == 2 and self.gameBoard[3][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][3] == 2 and self.gameBoard[2][2] == 2 and
                self.gameBoard[3][1] == 2 and self.gameBoard[4][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][5] == 2 and self.gameBoard[1][4] == 2 and
                self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][4] == 2 and self.gameBoard[2][3] == 2 and
                self.gameBoard[3][2] == 2 and self.gameBoard[4][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][3] == 2 and self.gameBoard[3][2] == 2 and
                self.gameBoard[4][1] == 2 and self.gameBoard[5][0] == 2):
            self.player2Score += 1
        if (self.gameBoard[0][6] == 2 and self.gameBoard[1][5] == 2 and
                self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][5] == 2 and self.gameBoard[2][4] == 2 and
                self.gameBoard[3][3] == 2 and self.gameBoard[4][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][4] == 2 and self.gameBoard[3][3] == 2 and
                self.gameBoard[4][2] == 2 and self.gameBoard[5][1] == 2):
            self.player2Score += 1
        if (self.gameBoard[1][6] == 2 and self.gameBoard[2][5] == 2 and
                self.gameBoard[3][4] == 2 and self.gameBoard[4][3] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][5] == 2 and self.gameBoard[3][4] == 2 and
                self.gameBoard[4][3] == 2 and self.gameBoard[5][2] == 2):
            self.player2Score += 1
        if (self.gameBoard[2][6] == 2 and self.gameBoard[3][5] == 2 and
                self.gameBoard[4][4] == 2 and self.gameBoard[5][3] == 2):
            self.player2Score += 1

#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Vassilis Athitsos
# Written to be Python 2.4 compatible for omega

import random
import sys
from copy import deepcopy

from anytree import Node, PreOrderIter, RenderTree


# Play a piece on a child board
def playPieceOn(gameBoard, currentTurn, column):
    if not gameBoard[0][column]:
        for i in range(5, -1, -1):
            if not gameBoard[i][column]:
                gameBoard[i][column] = currentTurn
                return True
    return False


# Check piece count on a child board
def checkPieceCountOn(gameBoard):
    pieceCount = sum(
        1 for row in gameBoard for piece in row if piece)


# Assigns a score to a board
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
        self.depth = 0
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

    # Switches to the next player
    def changePlayer(self):
        if self.currentTurn == 1:
            self.currentTurn = 2
        else:
            self.currentTurn = 1

    # Place the current player's piece in the requested column
    def playPiece(self, column):
        print('in play piece')
        if not self.gameBoard[0][column]:
            for i in range(5, -1, -1):
                if not self.gameBoard[i][column]:
                    print(i,  ' ', column)
                    self.gameBoard[i][column] = self.currentTurn
                    self.pieceCount += 1
                    return True

        # Notifies the player that he/she cannot place a piece in a full column
        print('\n Invalid move: This column is full.')
        return False

    # The AI section. Currently plays randomly.
    def aiPlay(self):
        column = self.nextMove()
        result = self.playPiece(column)

        print('\n\nmove %d: Player %d, column %d\n' %
              (self.pieceCount, self.currentTurn, column + 1))

    # Returns the root of the moves tree
    def getTree(self):
        root = Node('root', board=self.gameBoard, score=self.MIN, move=-1)
        for i in range(self.depth):
            for n in PreOrderIter(root, maxlevel=self.depth):
                if len(n.children) == 0:
                    for j in range(7):
                        tempBoard = deepcopy(n.board)
                        if i % 2 == 0:
                            value = self.MIN
                        else:
                            value = self.MAX
                        if playPieceOn(tempBoard, (self.currentTurn + i) % 2 + 1, j):
                            node = Node('{},{}'.format(i, j), parent=n,
                                        board=tempBoard, score=value, move=j)

        return root

    # Implements depth-limited alpha-beta pruning
    def nextMove(self):
        # First asign values to the leafs
        root = self.getTree()
        for n in PreOrderIter(root, maxlevel=self.depth):
            if len(n.children) == 0:
                n.value = evaluateBoard(n.board, self.depth % 2 == 0)

        # Finds the best path
        score = self.minimax(root, True, self.MIN, self.MAX)

        # Returns the next move
        for n in root.children:
            if n.score == score:
                return n.move
        print(root.children)
        return

    # Depth limited alpha-beta pruning
    def minimax(self, node, maximizingPlayer,
                alpha, beta):

        # Terminating condition. i.e
        # leaf node is reached
        if len(node.children) == 0:
            return node.score

        if maximizingPlayer:

            best = self.MIN

            # Recur for left and right children
            for n in node.children:

                val = self.minimax(n, False, alpha, beta)
                best = max(best, val)
                alpha = max(alpha, best)

                # Alpha Beta Pruning
                if beta <= alpha:
                    break

            return best

        else:
            best = self.MAX

            # Recur for left and
            # right children
            for n in node.children:

                val = self.minimax(n, False, alpha, beta)
                best = min(best, val)
                beta = min(beta, best)

                # Alpha Beta Pruning
                if beta <= alpha:
                    break

            return best

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

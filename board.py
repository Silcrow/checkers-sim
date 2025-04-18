# File: board.py
import pygame
from piece import Piece

LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

class Board:
    def __init__(self, rows, cols, tile_size):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.board = []
        self.create_board()

    def draw_squares(self, win):
        for row in range(self.rows):
            for col in range(self.cols):
                color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
                pygame.draw.rect(win, color, (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))

    def create_board(self):
        self.board = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        # Add pawns and kings for 2 players
        for row in range(3):
            for col in range(self.cols):
                if (row + col) % 2 != 0:
                    self.board[row][col] = Piece(row, col, "pawn", 1)

        for row in range(self.rows - 3, self.rows):
            for col in range(self.cols):
                if (row + col) % 2 != 0:
                    self.board[row][col] = Piece(row, col, "pawn", 2)

        # Add kings manually for now (one each)
        self.board[0][1] = Piece(0, 1, "king", 1)
        self.board[self.rows - 1][6] = Piece(self.rows - 1, 6, "king", 2)

    def draw(self, win):
        self.draw_squares(win)
        for row in self.board:
            for piece in row:
                if piece:
                    piece.draw(win, self.tile_size)

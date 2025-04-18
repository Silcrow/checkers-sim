# File: board.py
import pygame
from piece import Piece
from capture_logic import PincerCapture

LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

class Board:
    def __init__(self, rows, cols, tile_size, setup):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.board = [[None for _ in range(cols)] for _ in range(rows)]
        self.capture_logic = PincerCapture()
        self.setup_board(setup)

    def draw_squares(self, win):
        for row in range(self.rows):
            for col in range(self.cols):
                color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
                pygame.draw.rect(win, color, (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))

    def setup_board(self, setup):
        for item in setup:
            row, col, piece_type, player = item
            self.board[row][col] = Piece(row, col, piece_type, player)

    def draw(self, win, selected=None):
        self.draw_squares(win)
        for row in self.board:
            for piece in row:
                if piece:
                    is_selected = (piece == selected)
                    piece.draw(win, self.tile_size, is_selected)

    def get_piece(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.board[row][col]
        return None

    def move_piece(self, piece, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return False
        if self.board[row][col] is not None:
            return False

        self.board[piece.row][piece.col] = None
        self.board[row][col] = piece
        piece.move(row, col)

        self.capture_logic.apply(self, piece)
        return True
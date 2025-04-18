# File: board.py
import pygame
from piece import Piece

LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

class Board:
    def __init__(self, rows, cols, tile_size, ruleset):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.ruleset = ruleset
        self.kill_rule = ruleset["kill_rule"]
        self.score_rule = ruleset["score_rule"]
        self.win_rule = ruleset["win_rule"]
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
            return False  # Can't move onto another piece

        killed = self.kill_rule.should_kill(self, piece, row, col)
        for enemy in killed:
            self.board[enemy.row][enemy.col] = None

        self.board[piece.row][piece.col] = None
        self.board[row][col] = piece
        piece.move(row, col)
        return True

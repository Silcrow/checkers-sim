# File: piece.py
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class Piece:
    def __init__(self, row, col, piece_type, player):
        self.row = row
        self.col = col
        self.type = piece_type  # "pawn" or "king" or others
        self.player = player    # 1 or 2

    def move(self, row, col):
        self.row = row
        self.col = col

    def draw(self, win, tile_size, is_selected=False):
        radius = tile_size // 2 - 10
        x = self.col * tile_size + tile_size // 2
        y = self.row * tile_size + tile_size // 2

        color = RED if self.player == 1 else BLUE
        pygame.draw.circle(win, color, (x, y), radius)

        if self.type == "king":
            pygame.draw.circle(win, WHITE, (x, y), radius // 2)

        if is_selected:
            pygame.draw.circle(win, GREEN, (x, y), radius + 4, 3)
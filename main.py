# File: main.py
import pygame
from board import Board
from templates.checkers import TEMPLATE as CHECKERS_TEMPLATE

# Constants
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
TILE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

# Initialize pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Board Simulation Phase 2")

# Game loop
def main():
    clock = pygame.time.Clock()
    board = Board(ROWS, COLS, TILE_SIZE, CHECKERS_TEMPLATE)
    selected_piece = None

    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // TILE_SIZE
                col = x // TILE_SIZE
                if selected_piece:
                    moved = board.move_piece(selected_piece, row, col)
                    if moved:
                        selected_piece = None
                    else:
                        selected_piece = None
                else:
                    piece = board.get_piece(row, col)
                    if piece:
                        selected_piece = piece

        board.draw(WIN, selected_piece)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()

# File: main.py
import pygame
from board import Board

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
pygame.display.set_caption("Board Simulation Phase 1")

# Game loop
def main():
    clock = pygame.time.Clock()
    board = Board(ROWS, COLS, TILE_SIZE)

    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()

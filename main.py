# File: main.py
import pygame
from board import Board
from game_templates import load_template

# Constants
WIDTH, HEIGHT = 640, 640

# Initialize pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Board Simulation Phase 2")

# Game loop
def main():
    clock = pygame.time.Clock()

    # Load game setup from template
    game_config = load_template("hnefatafl")
    TILE_SIZE = WIDTH // game_config["cols"]
    board = Board(game_config["rows"], game_config["cols"], TILE_SIZE, game_config["setup"])

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

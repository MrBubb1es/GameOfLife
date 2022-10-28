from random import randint
from config import *
import pygame
import logic
import draw

# Setup
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()

# Set title
pygame.display.set_caption("Conway's Game of Life")

# Generate new random board
def new_board(board_size):
    return [[randint(0,1) for x in range(board_size[0])] for y in range(board_size[1])]

def main():
    running = True

    board_size = list(BOARD_SIZE)
    board = new_board(board_size)
    last_generated = 0
    time = 0
    palettes = draw.initialize_palettes(PALETTES)
    current_palette = CURRENT_PALLET
    blend = COLOR_BLEND
    draw_mode = DRAW_MODE
    draw_point = draw.update_draw_point(time, (len(board[0]), len(board)))
    paused = False

    while running:
        if time - last_generated > 3:
            if not paused:
                board = new_board(board_size)
            last_generated = time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.TEXTINPUT:
                if event.text == 'c':
                    current_palette = (current_palette + 1) % len(palettes)
                elif event.text == 'b':
                    blend = not blend
                elif event.text == 'm':
                    draw_mode = (draw_mode + 1) % 6
                elif event.text == 'p':
                    paused = not paused
                elif event.text == 'f':
                    # fill board
                    board = [[1 for x in range(board_size[0])] for y in range(board_size[1])]
                elif event.text == 'e':
                    # empty board
                    board = [[0 for x in range(board_size[0])] for y in range(board_size[1])]


        draw.update_screen(screen, board, palettes[current_palette], blend, draw_mode, draw_point)
        if not paused:
            board = logic.update_board(board)
        # Limit framerate and keep track of total time elapsed in seconds
        time += clock.tick(FPS) / 1000
        # for wandering draw mode
        if draw_mode == 5:
            draw_point = draw.update_draw_point(time, board_size)

    pygame.quit()

main()

import pygame
import math

# Convert between hex color string to pygame color
def str_to_col(color_str):
    r = int(color_str[0:2], base=16)
    g = int(color_str[2:4], base=16)
    b = int(color_str[4:6], base=16)
    return pygame.Color(r, g, b)

# Take in a palettes list and return an identical list with pygame color objects instead of strings
def initialize_palettes(palette_list):
    palettes = []
    for palette in palette_list:
        new_pallete = []
        for color in palette:
            new_pallete.append(str_to_col(color))
        palettes.append(new_pallete)

    return palettes

def update_draw_point(t, board_size):
    draw_point_x = (math.cos(t)*.3 + .5) * board_size[0]
    draw_point_y = (math.sin(t)*.3 + .5) * board_size[1]

    return [draw_point_x, draw_point_y]

# Return the point to measure distance from for draw modes 0 - 4
def get_draw_point(board_size, mode):
    # Center
    if mode == 0:
        draw_point = [board_size[0]//2, board_size[1]//2]
    # Top left
    elif mode == 1:
        draw_point = [0,0]
    # Top right
    elif mode == 2:
        draw_point = [board_size[0], 0]
    # Bottom left
    elif mode == 3:
        draw_point = [0, board_size[1]]
    # Bottom right
    elif mode == 4:
        draw_point = [board_size[0], board_size[1]]
    
    return draw_point

# return the distance from cell to the point set with DRAW_MODE
def distance_to_draw_point(x, y, draw_point):
    dx = draw_point[0] - x
    dy = draw_point[1] - y
    return math.sqrt(dx**2 + dy**2)

# Return the longest possible distance from cell to point set with DRAW_MODE
def longest_distance(board_size, mode, draw_point):
    # Center of board
    if mode == 0:
        dx = board_size[0] / 2
        dy = board_size[1] / 2
    # One of the corners
    elif mode != 5:
        dx = board_size[0]
        dy = board_size[1]
    else:
        # find the quadrent of the draw_point
        #  0 1
        #  2 3
        quad = round(draw_point[0] / board_size[0]) + 2*round(draw_point[1] / board_size[1])
        # compute the distance between the draw point and the opposite corner
        if quad == 0:
            dx = board_size[0] - draw_point[0]
            dy = board_size[1] - draw_point[1]
        elif quad == 1:
            dx = draw_point[0]
            dy = board_size[1] - draw_point[1]
        elif quad == 2:
            dx = board_size[0] - draw_point[0]
            dy = draw_point[1]
        elif quad == 3:
            dx = draw_point[0]
            dy = draw_point[1]
        
    return math.sqrt(dx**2 + dy**2)

# Return the color that a certain cell should be
def get_color(x, y, board_size, palette, blend, draw_mode, draw_point):
    if draw_mode != 5:
        draw_point = get_draw_point(board_size, draw_mode)

    palette_size = len(palette) - 1

    dist = distance_to_draw_point(x, y, draw_point)
    longest_dist = longest_distance(board_size, draw_mode, draw_point)

    # fraction of the longest distance a cell can be from the draw point
    dist_frac = dist / longest_dist

    if blend:
        color1 = palette[int(dist_frac * palette_size)]
        color2 = palette[(int(dist_frac * palette_size) + 1) % palette_size]
        # Linear interpolation between 2 palette colors to achieve gradient look
        cell_color = color1.lerp(color2, (dist_frac * palette_size)%1)
    else:
        cell_color = palette[int(dist_frac * palette_size)]

    return cell_color


def update_screen(screen, board, palette, blend, draw_mode, draw_point):
    # Size of board (2D list)
    board_size = (len(board), len(board[0]))
    # Create new, all black surface of size board_size
    new_surface = pygame.Surface(board_size)
    new_surface.fill(pygame.Color(0,0,0))

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                cell_color = get_color(x, y, board_size, palette, blend, draw_mode, draw_point)
                new_surface.set_at((x, y), cell_color)
    
    # Scale surface to fit the screen and draw it to the screen
    new_surface = pygame.transform.scale(new_surface, pygame.display.get_window_size())
    screen.blit(new_surface, (0,0))
    pygame.display.flip()
    

# Return the number of neighbors a cell at (x,y) has
def count_neighbors(x, y, board):
    board_size_x, board_size_y = len(board[0]), len(board)
    neighbors = 0

    # Loop through 8 surrounding cells and count the living ones
    for dx in range(-1,2):
        for dy in range(-1,2):
            if dx != 0 or dy != 0:
                if (x + dx) >= 0 and (x + dx) < board_size_x:
                    if (y + dy) >= 0 and (y + dy) < board_size_y:
                        if board[x + dx][y + dy]:
                            neighbors += 1
    
    return neighbors


def update_board(board):
    new_board = board.copy()
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            neighbors = count_neighbors(x, y, board)
            # Rules for conway's game of life
            if neighbors < 2 or neighbors > 3:
                new_board[y][x] = 0
            if neighbors == 3:
                new_board[y][x] = 1
    
    return new_board

import pygame

pygame.init()

# Set up the window
width = 600
height = 600
size = (width, height)
screen = pygame.display.set_mode(size)

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the font
font = pygame.font.Font(None, 32)

# Set up the board
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

# Set up the player symbols
player1 = "X"
player2 = "O"

# Set up the current player
current_player = player1

# Set up the game over flag
game_over = False

# Set up the win message
win_message = ""

# Set up the cell size
cell_size = 200


def draw_board():
    # Draw the horizontal lines
    pygame.draw.line(screen, black, (cell_size, 0), (cell_size, height))
    pygame.draw.line(screen, black, (2 * cell_size, 0), (2 * cell_size, height))
    # Draw the vertical lines
    pygame.draw.line(screen, black, (0, cell_size), (width, cell_size))
    pygame.draw.line(screen, black, (0, 2 * cell_size), (width, 2 * cell_size))


def draw_symbol(row, col, symbol):
    # Calculate the center point of the cell
    x = (col * cell_size) + (cell_size // 2)
    y = (row * cell_size) + (cell_size // 2)
    # Draw the symbol
    text = font.render(symbol, True, black)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


def make_move(player, row, col):
    if board[row][col] != " ":
        return
    board[row][col] = player


def has_won(player):
    # Check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def draw_win_message(message):
    text = font.render(message, True, black)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)


#     ----------------------------------GAME LOOP-------------------------------------------


while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse coordinates
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Calculate the row and column that was clicked
            row = mouse_y // cell_size
            col = mouse_x // cell_size
            # Make the move
            make_move(current_player, row, col)
            if has_won(current_player):
                win_message = f"{current_player} has won!"
            else:
                # Switch players
                if current_player == player1:
                    current_player = player2
                else:
                    current_player = player1
    # Clear the screen
    screen.fill(white)
    # Draw the board
    draw_board()
    # Draw the symbols
    for row in range(3):
        for col in range(3):
            symbol = board[row][col]
            if symbol != " ":
                draw_symbol(row, col, symbol)
    # Draw the win message, if necessary
    if win_message:
        # Draw the win message in red
        text = font.render(win_message, True, (255, 0, 0))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)
        # Draw the restart and quit buttons
        restart_rect = pygame.Rect(width // 2 - 75, height // 2 + 50, 150, 50)
        quit_rect = pygame.Rect(width // 2 - 75, height // 2 + 125, 150, 50)
        pygame.draw.rect(screen, black, restart_rect, 2)
        pygame.draw.rect(screen, black, quit_rect, 2)
        restart_text = font.render("Restart", True, black)
        quit_text = font.render("Quit", True, black)
        restart_text_rect = restart_text.get_rect(center=restart_rect.center)
        quit_text_rect = quit_text.get_rect(center=quit_rect.center)
        screen.blit(restart_text, restart_text_rect)
        screen.blit(quit_text, quit_text_rect)
    # Update the display
    pygame.display.flip()

    # Check if the player wants to restart or quit
    if win_message:
        restart_rect = pygame.Rect(width // 2 - 75, height // 2 + 50, 150, 50)
        quit_rect = pygame.Rect(width // 2 - 75, height // 2 + 125, 150, 50)
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse coordinates
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Check if the player clicked the restart button
                    if restart_rect.collidepoint(mouse_x, mouse_y):
                        # Reset the game state
                        board = [[" ", " ", " "],
                                 [" ", " ", " "],
                                 [" ", " ", " "]]
                        current_player = player1
                        win_message = "DRAW"
                        screen.fill(white)
                        # Draw the board
                        draw_board()
                        break
                    # Check if the player clicked the quit button
                    elif quit_rect.collidepoint(mouse_x, mouse_y):
                        game_over = True
                        break


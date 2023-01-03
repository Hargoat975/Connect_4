import numpy as np 
# import pygame
# from sys import exit

# pygame.init()
# screen  = pygame.display.set_mode((800,400))
# pygame.display.set_caption('Connect 4')
# clock = pygame.time.Clock()
# surface = pygame.Surface((800,400))
# surface.fill('beige')
print("something")
while True:
    board_width = 7
    board_height = 6
    player_1 = 1
    player_2 = 2
    winner = 0

    def create_board():
        return np.zeros((board_height,board_width))

    def print_board(board):
        print(board)

    def add_piece(player, board, column): 
        if player == 1:
            piece = 1
        elif player == 2:
            piece = -1
        for row in np.arange(board_height):
            if board[row][column] == 0:
                board[row][column] = piece
            if row == board_height-1:
                return #throw error
        return board

    def check_winner(board):
        if horizontal_win(board):
            return horizontal_win(board)
        elif vertical_win(board):
            return vertical_win(board)
        elif left_diagonal_win(board):
            return left_diagonal_win(board)
        elif right_diagonal_win(board):
            return right_diagonal_win(board)
        else:
            return 0
        

    def horizontal_win(board):
        player_1_counter = 0
        player_2_counter = 0
        for row in np.arange(board_height):
            for column in np.arange(board_width):
                if board[row][column] == 1:
                    player_1_counter += 1
                elif board[row][column] == -1:
                    player_2_counter += 1
                else:
                    player_1_counter = 0
                    player_2_counter = 0
                if player_1_counter == 4:
                    return 1
                if player_2_counter == 4:
                    return -1

    def vertical_win(board):
        player_1_counter = 0
        player_2_counter = 0
        for column in np.arange(board_width):
            for row in np.arange(board_height):
                if board[row][column] == 1:
                    player_1_counter += 1
                elif board[row][column] == -1:
                    player_2_counter += 1
                else:
                    player_1_counter = 0
                    player_2_counter = 0
                if player_1_counter == 4:
                    return 1
                if player_2_counter == 4:
                    return -1

    def right_diagonal_win(board):
        for row in np.arange(3):
            for column in np.arange(3,board_width):
                if board[row][column] == 1:
                    what_player = 1
                elif board[row][column] == -1:
                    what_player = -1
                else:
                    what_player = 5
                if board[row-1][column-1] == what_player:
                    if board[row-2][column-2] == what_player:
                        if board[row-3][column-3] == what_player:
                            return what_player
        return 0

    def left_diagonal_win(board):
        for row in np.arange(3):
            for column in np.arange(4):
                if board[row][column] == 1:
                    what_player = 1
                elif board[row][column] == -1:
                    what_player = -1
                else:
                    what_player = 5
                if board[row+1][column+1] == what_player:
                    if board[row+2][column+2] == what_player:
                        if board[row+3][column+3] == what_player:
                            return what_player
        return 0

    def tie(board):
        if check_winner(board):
            return False
        for row in np.arange(board_height):
            for column in np.arange(board_width):
                if board[row][column] == 0:
                    return False
        return True

    def ask_for_number():
        val = 100
        while val == 100:
            val = input("Column: ")
            if val >= 0 and val <= 5:
                return val
            else:
                val = 100
                print("Enter Valid Number!")

    def play_game():
        board = create_board()
        while True:
            add_piece(player_1,board, ask_for_number())
            print_board()
            if check_winner(board) == 1:
                print('Player One Wins!')
                return
            add_piece(player_2,board, ask_for_number())
            print(board)
            if check_winner(board) == -1:
                print('Player Two Wins!')
                return
            elif tie(board):
                print('Game Ended in a Tie!')
                return  

    play_game()


    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         exit()
    # screen.blit(surface, (0,0))
    # pygame.display.update()
    # clock.tick(60)
            
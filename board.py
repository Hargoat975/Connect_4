import numpy as np 
import pygame
import sys
import math



gameOver = 0
BLUE = (0,0,255)
BLACK = (0,0,0)

board_width = 7
board_height = 6
square_size = 100
radius = int(square_size/2 - 5)
square_width = square_size * board_width
square_height = square_size * (board_height+1)
size = (square_width, square_height)

pygame.init()
screen = pygame.display.set_mode(size)


while not gameOver:

    board_width = 7
    board_height = 6
    player_1 = 1
    player_2 = 2
    winner = 0
    turn = 0
    

    def draw_board(board):
        for column in range(board_width):
            for row in range(board_height):
                pygame.draw.rect(screen, BLUE, (column*square_size, row*square_size + square_size, square_size, square_size))
                pygame.draw.circle(screen,BLACK, (int(column*square_size+square_size/2), int(row*square_size+square_size+square_size/2)), radius)

    

    def create_board():
        return np.zeros((board_height,board_width))
    
    sample = create_board()
    draw_board(sample)
    pygame.display.update()
    
    def print_board(board):
        output = board[::-1]
        print(output)

    def add_piece(player, board, column): 
        if player == 1:
            piece = 1
        elif player == 2:
            piece = -1
        if valid_move(board, column):
            for row in np.arange(board_height):
                if board[row][column] == 0:
                    board[row][column] = piece
                    return board
        else:
            print("Enter Valid Input")
            newValue = ask_for_number()
            add_piece(player, board, newValue)

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
                    player_2_counter = 0
                elif board[row][column] == -1:
                    player_2_counter += 1
                    player_1_counter = 0
                else:
                    player_1_counter = 0
                    player_2_counter = 0
                if player_1_counter == 4:
                    return 1
                if player_2_counter == 4:
                    return -1
            player_2_counter = 0
            player_1_counter = 0

    def vertical_win(board):
        player_1_counter = 0
        player_2_counter = 0
        for column in np.arange(board_width):
            for row in np.arange(board_height):
                if board[row][column] == 1:
                    player_1_counter += 1
                    player_2_counter = 0
                elif board[row][column] == -1:
                    player_2_counter += 1
                    player_1_counter = 0
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
            try:
                val = int(val)
            except ValueError:
                print("Enter a number!")
                ask_for_number()
        return val

    def play_game_manual():
        board = create_board()
        while True:
            add_piece(player_1,board, ask_for_number())
            print_board(board)
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

    def play_game_vs_AI():
        board = create_board()
        while True:
            input = ask_for_number()
            add_piece(player_1, board, input)
            print_board(board)
            if check_winner(board) == 1:
                print("You win!")
                return
            AI_move(board)
            print_board(board)
            if check_winner(board) == -1:
                print("AI won!")
                return
            elif tie(board):
                print('Game Ended in a Tie!')
                return
    
    def score(board):
        if check_winner(board) == 1:
            return -1000
        elif check_winner(board) == -1:
            return 1000
        else:
            return 0

    def gameOver(board):
        if tie(board) or check_winner(board):
            return True
        return False

    def minimax(board, depth, maximizingPlayer):
        if maximizingPlayer == player_1:
            opponent = player_2
        else:
            opponent = player_1
        if gameOver(board) or depth == 0:
            return score(board)
        if maximizingPlayer:
            bestValue = float("-inf")
            for col in range(board_width):
                testBoard = board.copy()
                if valid_move(testBoard, col):
                    add_piece(maximizingPlayer, testBoard, col)
                    value = minimax(testBoard, depth - 1, False)
                    bestValue = max(bestValue, value)
            return bestValue
        else:
            bestValue = float('inf')
            for col in range(board_width):
                testBoard = board.copy()
                if valid_move(testBoard, col):
                    add_piece(opponent, testBoard, col)
                    value = minimax(testBoard, depth-1, True)
                    bestValue = min(bestValue, value)
            return bestValue
                

    def valid_move(board, column):
        if (column >= 0) and (column <= 6):
            for row in np.arange(board_height):
                if board[row][column] == 0:
                    return True
                if row == board_height-1:
                    return False
        else:
            return False


    def AI_move(board):
        bestScore = float('-inf')
        bestMove = None
        for column in np.arange(board_width):
            testBoard = board.copy()
            if valid_move(testBoard, column):
                add_piece(player_2, testBoard, column)
                score = minimax(testBoard, 3, False)
                if score > bestScore:
                    bestScore = score
                    bestMove = column
        add_piece(player_2, board, bestMove)    
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('')
                # while not gameOver:
                #     posx = event.pos[0]
                #     col = int(math.floor(posx/square_size))
                #     if turn % 2 == 1:
                #         add_piece(player_1, sample, col)
                #         print_board()
                #         if check_winner(sample) == 1:
                #             print('Player One Wins!')
                #     else:
                #         add_piece(player_2, sample, col)
                #         print_board()
                #         if check_winner(sample) == 1:
                #             print('Player Two Wins!')
                #         elif tie(sample):
                #             print('Tie')
                        
    
    


    
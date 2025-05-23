"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count total number of moves made so far
    total = 0
    for row in board:
        for tile in row:
            if tile != EMPTY:
                total += 1
    
    # X goes first, so even number of moves = X's turn, odd = O's turn
    if total % 2 == 0:
        return X
    else:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_actions = set()
    row_number = 0
    for row in board:
        tile_number = 0
        for tile in row:
            # If tile is empty, add its coordinates as a possible action
            if tile == EMPTY:
                all_actions.add((row_number, tile_number))
            tile_number += 1
        row_number += 1
    
    return all_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_turn = player(board)
    # Create a deep copy to avoid modifying the original board
    new_board = copy.deepcopy(board)

    # raise exception if out of bound
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise Exception("Action out of bounds")

    # raise exception if not empty
    if new_board[action[0]][action[1]] != EMPTY:
        raise Exception("Not an empty space")
    
    # Place the current player's mark on the board
    new_board[action[0]][action[1]] = player_turn
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows for three in a row
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    # Check columns for three in a row
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    
    # Check diagonals for three in a row
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None

    # row_number = 0
    # tile_number = 0
    # possible_wins = initial_state()

    # # replace possible_wins with the board columns
    # for row in board:
    #     for tile in row:
    #         possible_wins[tile_number][row_number] = tile
    #         tile_number += 1
    #     tile_number = 0
    #     row_number += 1

    # # add the rows and the diagonals values
    # possible_wins.extend(board)
    # possible_wins.append([board[0][0],board[1][1],board[2][2]])
    # possible_wins.append([board[2][0],board[1][1],board[0][2]])
    
    # # check if any of possible_wins is true
    # for row in possible_wins:
    #     total_X = 0
    #     total_O = 0
    #     for tile in row:
    #         if total_X == 0 or total_O == 0:
    #             if tile == X:
    #                 total_X += 1
    #                 if total_X == 3:
    #                     return X
    #             elif tile == O:
    #                 total_O += 1
    #                 if total_O == 3:
    #                     return O
    #             else:
    #                 break
    #         else:
    #             break
    # return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game is over if there's a winner
    if (winner(board) == X) or (winner(board) == O):
        return True
    # Game is over if board is full (no more actions available)
    elif (len(actions(board)) == 0):
        return True
    # Game continues
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1  # X wins
    elif result == O:
        return -1  # O wins
    else:
        return 0  # Draw or game not over
    

def max_value(board):
    """
    Helper function for minimax: returns maximum value for the maximizing player (X).
    """
    # If game is over, return the utility value
    if terminal(board) == True:
        return utility(board)
    
    v = -math.inf

    # Try all possible actions and pick the maximum value
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    """
    Helper function for minimax: returns minimum value for the minimizing player (O).
    """
    # If game is over, return the utility value
    if terminal(board) == True:
        return utility(board)
    
    v = math.inf

    # Try all possible actions and pick the minimum value
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v
   

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Return None if the game is already over
    if terminal(board) == True:
        return None
    
    player_turn = player(board)
    best_turn = tuple()
    
    if player_turn == X:
        v = -math.inf
        for action in actions(board):
            # Get the minimum value the opponent can achieve
            new_v = min_value(result(board, action))
            # If this action is better than current best, update
            if new_v > v:
                v = new_v
                best_turn = action
    else:
        v = math.inf
        for action in actions(board):
            # Get the maximum value the opponent can achieve
            new_v = max_value(result(board, action))
            # If this action is better than current best, update
            if new_v < v:
                v = new_v
                best_turn = action

    return best_turn
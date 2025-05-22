"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    # return [[X, X, O],
    #         [X, O, X],
    #         [O, O, EMPTY]]
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
#board = initial_state()

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    total = 0
    for row in board:
        for tile in row:
            if tile != EMPTY:
                total += 1
    
    if total % 2 == 0:
        return X
    else:
        return O
# print(player(board))

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_actions = set()
    row_number = 0
    print(board)
    for row in board:
        tile_number = 0
        for tile in row:
            if tile == EMPTY:
                all_actions.add((row_number, tile_number))
            tile_number += 1
        row_number += 1
    
    return all_actions
# print(actions(board))

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_turn =  player(board)
    new_board = copy.deepcopy(board)

    # raise exception if out of bound
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise Exception("Action out of bounds")

    # raise exception if not empty
    if new_board[action[0]][action[1]] != EMPTY:
        raise Exception("Not an empty space")
    
    new_board[action[0]][action[1]] = player_turn
    return new_board
# next_turn = result(board,(0,1))


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    total = 0
    row_number = 0
    tile_number = 0
    possible_wins = initial_state()

    # replace possible_wins with the board columns
    for row in board:
        for tile in row:
            if tile != EMPTY:
                total += 1
            possible_wins[tile_number][row_number] = tile
            tile_number += 1
        tile_number = 0
        row_number += 1

    # if all the tiles filled up return true
    if total == 9:
        return None
    
    # add the rows and the diagonals values
    possible_wins.extend(board)
    possible_wins.append([board[0][0],board[1][1],board[2][2]])
    possible_wins.append([board[2][0],board[1][1],board[0][2]])
    
    # check if any of possible_wins is true
    for row in possible_wins:
        total_X = 0
        total_O = 0
        for tile in row:
            if total_X == 0 or total_O == 0:
                if tile == X:
                    total_X += 1
                    if total_X == 3:
                        return X
                elif tile == O:
                    total_O += 1
                    if total_O == 3:
                        return O
                else:
                    break
            else:
                break
    return None
# print(winner(board))

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        return False
    else:
        return True
# print(terminal(board))


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0
# print(utility(board))

# def max_value(board):


# def min_value(board):
    

# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     if terminal(board) == True:
#         return None
#     player_turn =  player(board)
#     for action in actions(board):
#         next_board = result(board, action)
#         if terminal(next_board):


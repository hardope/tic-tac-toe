"""
Tic Tac Toe Player
"""

import math

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
    x = 0
    o = 0

    for i in board:
        for j in i:
            if j == X:
                x += 1
            elif j == O:
                o += 1

    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None

    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")

    result_board = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
                
    for i in range(3):
        for j in range(3):
            result_board[i][j] = board[i][j]

    result_board[action[0]][action[1]] = player(board)

    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    """
Tic Tac Toe Player
"""

import math

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

    x = 0
    o = 0

    for i in board:
        for j in i:
            if j == X:
                x += 1
            elif j == O:
                o += 1

    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    if terminal(board):
        return None

    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("Invalid action")

    result_board = [[EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
                
    for i in range(3):
        for j in range(3):
            result_board[i][j] = board[i][j]

    result_board[action[0]][action[1]] = player(board)

    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    for i in board:
        for j in i:
            if j == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def maximum_value(board):
        if terminal(board):
            return utility(board)

        v = -math.inf

        for action in actions(board):
            v = max(v, minimum_value(result(board, action)))

        return v

def minimum_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    
    for action in actions(board):
        v = min(v, maximum_value(result(board, action)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:

        v = -math.inf

        for action in actions(board):

            minimum_result_value = minimum_value(result(board, action))

            if minimum_result_value > v:

                v = minimum_result_value
                optimal_action = action
    else:

        v = math.inf

        for action in actions(board):

            maximum_result_value = maximum_value(result(board, action))

            if maximum_result_value < v:

                v = maximum_result_value
                optimal_action = action

    return optimal_action


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def maximum_value(board):
        if terminal(board):
            return utility(board)

        v = -math.inf

        for action in actions(board):
            v = max(v, minimum_value(result(board, action)))

        return v

def minimum_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    
    for action in actions(board):
        v = min(v, maximum_value(result(board, action)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:

        v = -math.inf

        for action in actions(board):

            minimum_result_value = minimum_value(result(board, action))

            if minimum_result_value > v:

                v = minimum_result_value
                optimal_action = action
    else:

        v = math.inf

        for action in actions(board):

            maximum_result_value = maximum_value(result(board, action))

            if maximum_result_value < v:

                v = maximum_result_value
                optimal_action = action

    return optimal_action

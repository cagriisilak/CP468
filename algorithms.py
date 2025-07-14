#algorithims.py
import functions
import google.generativeai as genai
import re

# Add global counters for nodes
minimax_nodes = 0
alpha_beta_nodes = 0
_gemini_calls = 0

def reset_node_counters():
    global minimax_nodes, alpha_beta_nodes, _gemini_calls 
    minimax_nodes = 0
    alpha_beta_nodes = 0
    _gemini_calls  = 0

def get_minimax_nodes():
    return minimax_nodes

def get_alpha_beta_nodes():
    return alpha_beta_nodes

def get_gemini_calls():
    return _gemini_calls

def simple_algo(board_state, player):
    possible_moves = functions.get_possible_moves(board_state)
    return possible_moves[0]


def get_utility(board, player):
    """
    Calculates the utility of a given board state for a player.

    Args:
        board (list): The list of lists representing the board.
        player (int): The player to calculate the utility for (1 or 2).

    Returns:
        int: The utility of the board state (1 for win, -1 for loss, 0 for draw).
    """
    game_finished, winner = functions.check_game_status(board)
    if game_finished:
        if winner == player:
            return 1
        elif winner is None:
            return 0
        else:
            return -1
    return None  # Game is not over


def minimax(board, player, maximizing_player):
    """
    Minimax algorithm to find the best move.

    Args:
        board (list): The current board state.
        player (int): The current player.
        maximizing_player (int): The player for whom we are maximizing.

    Returns:
        int: The best score for the maximizing player.
    """
    global minimax_nodes
    minimax_nodes += 1

    utility = get_utility(board, maximizing_player)
    if utility is not None:
        return utility

    possible_moves = functions.get_possible_moves(board)
    if player == maximizing_player:
        best_score = -float('inf')
        for row, col in possible_moves:
            new_board = [row[:] for row in board]
            functions.make_move(new_board, row, col, player)
            score = minimax(new_board, 2 if player == 1 else 1, maximizing_player)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row, col in possible_moves:
            new_board = [row[:] for row in board]  # Create a copy
            functions.make_move(new_board, row, col, player)
            score = minimax(new_board, 2 if player == 1 else 1, maximizing_player)
            best_score = min(best_score, score)
        return best_score


def minimax_algo(board, player):
    """
    Algorithm that uses minimax to choose the best move.

    Args:
        board (list): The current board state.
        player(int): the current player

    Returns:
        tuple: The best move (row, col).
    """

    possible_moves = functions.get_possible_moves(board)
    best_move = None
    best_score = -float('inf')
    for row, col in possible_moves:
        new_board = [row[:] for row in board]
        functions.make_move(new_board, row, col, player)
        score = minimax(new_board, 2 if player == 1 else 1, player)
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move


def alpha_beta_minimax(board, player, maximizing_player, alpha, beta):
    """
    Alpha-Beta Pruning Minimax algorithm.

    Args:
        board (list): The current board state.
        player (int): The current player.
        maximizing_player (int): The player for whom we are maximizing.
        alpha (int): The best value that the maximizing player can guarantee.
        beta (int): The best value that the minimizing player can guarantee.

    Returns:
        int: The best score for the maximizing player.
    """
    global alpha_beta_nodes
    alpha_beta_nodes += 1

    utility = get_utility(board, maximizing_player)
    if utility is not None:
        return utility

    possible_moves = functions.get_possible_moves(board)
    if player == maximizing_player:
        best_score = -float('inf')
        for row, col in possible_moves:
            new_board = [row[:] for row in board]
            functions.make_move(new_board, row, col, player)
            score = alpha_beta_minimax(new_board, 2 if player == 1 else 1, maximizing_player, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # Beta cutoff
        return best_score
    else:
        best_score = float('inf')
        for row, col in possible_moves:
            new_board = [row[:] for row in board]
            functions.make_move(new_board, row, col, player)
            score = alpha_beta_minimax(new_board, 2 if player == 1 else 1, maximizing_player, alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break  # Alpha cutoff
        return best_score


def alpha_beta_algo(board, player):
    """
    Algorithm that uses Alpha-Beta Pruning to choose the best move.

    Args:
        board (list): The current board state.
        player (int): the current player

    Returns:
        tuple: The best move (row, col).
    """

    possible_moves = functions.get_possible_moves(board)
    best_move = None
    best_score = -float('inf')
    alpha = -float('inf')
    beta = float('inf')
    for row, col in possible_moves:
        new_board = [row[:] for row in board]
        functions.make_move(new_board, row, col, player)
        score = alpha_beta_minimax(new_board, 2 if player == 1 else 1, player, alpha, beta)
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move


genai.configure(api_key="AIzaSyAKCwoqMGg6Fb-y8W7wIRKomrfvj1VQ0Cg")

def gemini_algo(board, player):
    """
    Gemini-powered AI player that selects a move in a Tic-Tac-Toe game.

    Args:
        board (list): The current board state.
        player (int): The current player.

    Returns:
        tuple: The chosen move (row, col).
    """
    global _gemini_calls
    _gemini_calls += 1  # Track API calls

    possible_moves = functions.get_possible_moves(board)
    best_move = possible_moves[0]
    board_size = len(board)

    try:
        symbols = {0: " ", 1: "X", 2: "O"}
        board_desc = "\n".join(
            "|".join(symbols[cell] for cell in row) + "\n" + "-" * (board_size * 2 -1)
            for row in board
        )

        prompt = f"""You are Player {symbols[player]} in a {board_size}x{board_size} Tic-Tac-Toe game.
Current Board (0-based indices):
{board_desc}
Valid moves: {possible_moves}
Return ONLY the zero-based row and column as two numbers between 0-{board_size-1}, 
formatted exactly like: 'row,column' with no other text.
Examples of valid responses: '0,1' or '{board_size-1},{board_size-1}'"""

        model = genai.GenerativeModel('gemini-2.0-pro-exp')
        response = model.generate_content(prompt)

        def parse_gemini_response(text):
            clean_text = re.sub(r'[^0-9,]', '', text)
            matches = re.findall(r'\d', clean_text)

            if len(matches) >= 2:
                return int(matches[0]), int(matches[1])
            raise ValueError("Invalid response format")

        row, col = parse_gemini_response(response.text)

        if not (0 <= row < board_size and 0 <= col < board_size):
            raise ValueError("Move out of bounds")

        if not functions.is_valid_move(board, row, col):
            raise ValueError("Invalid move")

        return (row, col)

    except Exception as e:
        print(f"Gemini error: {str(e)[:50]}... Using fallback move.")
        return best_move
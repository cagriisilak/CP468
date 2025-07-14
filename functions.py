#functions.py
import time, algorithms

def check_input(input_value, valid_list):
  """
  Checks if an input value is in a given list.

  Args:
    input_value: The value to check.
    valid_list: The list of valid values.

  Raises:
    ValueError: If the input value is not in the valid list.
  """
  if input_value not in valid_list:
    raise ValueError(f"'{input_value}' is not a valid input. Valid inputs are: {valid_list}")
  

def create_board(board_size):
    """
    Creates an empty Tic-Tac-Toe board.

    Args:
        board_size (int): The size of the board (e.g., 3 for 3x3, 4 for 4x4).

    Returns:
        list: A list of lists representing the empty board.
    """
    return [[0 for _ in range(board_size)] for _ in range(board_size)]

def print_board(board):
    """
    Prints the Tic-Tac-Toe board to the console.

    Args:
        board (list): The list of lists representing the board.

    Returns:
        None
    """
    symbols = {0: " ", 1: "X", 2: "O"}
    board_size = len(board)
    for row in board:
        print(" | ".join(symbols[cell] for cell in row))
        print("-" * (board_size * 4 - 1))

def is_valid_move(board, row, col):
    """
    Checks if a move is valid.

    Args:
        board (list): The list of lists representing the board.
        row (int): The row index of the move.
        col (int): The column index of the move.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    board_size = len(board)
    return 0 <= row < board_size and 0 <= col < board_size and board[row][col] == 0

def get_possible_moves(board):
    """
    Generates a list of possible moves (coordinates) on the Tic-Tac-Toe board.

    Args:
        board (list): The list of lists representing the board.

    Returns:
        list: A list of tuples, where each tuple represents a possible move (row, col).
    """
    board_size = len(board)
    possible_moves = []
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == 0:
                possible_moves.append((row, col))
    return possible_moves

def make_move(board, row, col, player):
    """
    Makes a move on the board.

    Args:
        board (list): The list of lists representing the board.
        row (int): The row index of the move.
        col (int): The column index of the move.
        player (int): The player making the move (1 or 2).

    Returns:
        bool: True if the move was made, False otherwise (invalid move).
    """
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

def check_game_status(board):
    """
    Checks if the game is over and returns the status and winner (if any).

    Args:
        board (list): The list of lists representing the board.

    Returns:
        tuple: (bool, int or None). The first element is True if the game is over, False otherwise.
               The second element is the winning player (1 or 2) if there is a winner, or None if it's a draw or not over.
    """
    board_size = len(board)
    # Check for wins
    for player in [1, 2]:
        # Horizontal wins
        for row in board:
            if all(cell == player for cell in row):
                return True, player
        # Vertical wins
        for col in range(board_size):
            if all(board[row][col] == player for row in range(board_size)):
                return True, player
        # Diagonal wins
        if all(board[i][i] == player for i in range(board_size)) or all(
            board[i][board_size - 1 - i] == player for i in range(board_size)
        ):
            return True, player

    # Check for draw
    if all(cell != 0 for row in board for cell in row):
        return True, None

    # Game is not over
    return False, None

def run_game(player_1, player_2, board_size=3, visualize=False):
    """
    Runs a Tic-Tac-Toe game between two players.

    Args:
        player_1 (function): A function that takes a board and returns a move (row, col).
        player_2 (function): A function that takes a board and returns a move (row, col).
        board_size (int): The size of the board (default is 3).

    Returns:
        tuple: (bool, int or None, list). The first element is True if the game is over, False otherwise.
               The second element is the winning player (1 or 2) or None for a draw.
               The third element is the final board state.
    """
    board = create_board(board_size)
    game_finished = False
    current_player = 1
    
    # Track the previous total nodes for each algorithm type
    previous_minimax_nodes = 0
    previous_alpha_beta_nodes = 0
    previous_gemini_calls = 0
    
    algorithms.reset_node_counters()

    while not game_finished:
        # Get current counts before move
        if visualize:
            before_minimax_nodes = algorithms.get_minimax_nodes()
            before_alpha_beta_nodes = algorithms.get_alpha_beta_nodes()
            before_gemini_calls = algorithms.get_gemini_calls()
            
        if current_player == 1:
            row, col = player_1(board, current_player)
        else:
            row, col = player_2(board, current_player)
       
        start_time = time.perf_counter()
        if make_move(board, row, col, current_player):
            t = time.perf_counter() - start_time
            if visualize:
                print(f"Player {current_player}:")
                print(f"Time Spent: {t}")
                
                # Calculate node expansions for the current move
                if player_1.__name__ == 'minimax_algo' and current_player == 1:
                    new_nodes = algorithms.get_minimax_nodes() - before_minimax_nodes
                    print(f"New Nodes Expanded: {new_nodes}")
                    print(f"Total Nodes Expanded: {algorithms.get_minimax_nodes()}")
                elif player_1.__name__ == 'alpha_beta_algo' and current_player == 1:
                    new_nodes = algorithms.get_alpha_beta_nodes() - before_alpha_beta_nodes
                    print(f"New Nodes Expanded: {new_nodes}")
                    print(f"Total Nodes Expanded: {algorithms.get_alpha_beta_nodes()}")
                elif player_1.__name__ == 'gemini_algo' and current_player == 1:
                    new_calls = algorithms.get_gemini_calls() - before_gemini_calls
                    print(f"New Gemini API Calls: {new_calls}")
                    print(f"Total Gemini API Calls: {algorithms.get_gemini_calls()}")
                elif player_2.__name__ == 'minimax_algo' and current_player == 2:
                    new_nodes = algorithms.get_minimax_nodes() - before_minimax_nodes
                    print(f"New Nodes Expanded: {new_nodes}")
                    print(f"Total Nodes Expanded: {algorithms.get_minimax_nodes()}")
                elif player_2.__name__ == 'alpha_beta_algo' and current_player == 2:
                    new_nodes = algorithms.get_alpha_beta_nodes() - before_alpha_beta_nodes
                    print(f"New Nodes Expanded: {new_nodes}")
                    print(f"Total Nodes Expanded: {algorithms.get_alpha_beta_nodes()}")
                elif player_2.__name__ == 'gemini_algo' and current_player == 2:
                    new_calls = algorithms.get_gemini_calls() - before_gemini_calls
                    print(f"New Gemini API Calls: {new_calls}")
                    print(f"Total Gemini API Calls: {algorithms.get_gemini_calls()}")
                
                print_board(board)
                print("\n")
                
            current_player = 2 if current_player == 1 else 1
        else:
            print(f"invalid move from player {current_player}")
            exit

        game_finished, winner = check_game_status(board)
   
    if visualize:
        if winner is None:
            print("Result: Draw")
        else:
            print("Result: Win")
            print(f"Winner: Player {winner}")

    return game_finished, winner, board
# testing.py
import time
import algorithms
from functions import create_board, make_move, check_game_status

def run_game_with_metrics(player1, player2, board_size=3):
    """Run a game and collect metrics for each move."""
    board = create_board(board_size)
    metrics = {
        'player1_time': [], 
        'player1_operations': [],  # Changed from nodes to operations
        'player2_time': [],
        'player2_operations': [],  # Changed from nodes to operations
        'winner': None
    }
    current_player = 1

    while True:
        algorithms.reset_node_counters()  # Reset all counters before each move
        start_time = time.time()
        
        if current_player == 1:
            move = player1(board, current_player)
            metrics['player1_time'].append(time.time() - start_time)
            if player1 == algorithms.minimax_algo:
                metrics['player1_operations'].append(algorithms.get_minimax_nodes())
            elif player1 == algorithms.alpha_beta_algo:
                metrics['player1_operations'].append(algorithms.get_alpha_beta_nodes())
            else:  # Gemini
                metrics['player1_operations'].append(algorithms.get_gemini_calls())
        else:
            move = player2(board, current_player)
            metrics['player2_time'].append(time.time() - start_time)
            if player2 == algorithms.minimax_algo:
                metrics['player2_operations'].append(algorithms.get_minimax_nodes())
            elif player2 == algorithms.alpha_beta_algo:
                metrics['player2_operations'].append(algorithms.get_alpha_beta_nodes())
            else:  # Gemini
                metrics['player2_operations'].append(algorithms.get_gemini_calls())

        if not make_move(board, move[0], move[1], current_player):
            break

        game_finished, winner = check_game_status(board)
        if game_finished:
            metrics['winner'] = winner
            break
        current_player = 2 if current_player == 1 else 1

    return metrics

def run_performance_tests(num_games = 1, board_size = 3):
    test_cases = [
        (algorithms.minimax_algo, "Minimax", algorithms.alpha_beta_algo, "Alpha-Beta"),
        (algorithms.minimax_algo, "Minimax", algorithms.gemini_algo, "Gemini"),
        (algorithms.alpha_beta_algo, "Alpha-Beta", algorithms.gemini_algo, "Gemini")
    ]
    

    for p1_algo, p1_name, p2_algo, p2_name in test_cases:
        p1_wins = 0
        p2_wins = 0
        draws = 0
        p1_total_time = []
        p1_total_ops = []
        p2_total_time = []
        p2_total_ops = []

        for _ in range(num_games):
            metrics = run_game_with_metrics(p1_algo, p2_algo, board_size)
            if metrics['winner'] == 1:
                p1_wins += 1
            elif metrics['winner'] == 2:
                p2_wins += 1
            else:
                draws += 1

            p1_total_time.extend(metrics['player1_time'])
            p1_total_ops.extend(metrics['player1_operations'])
            p2_total_time.extend(metrics['player2_time'])
            p2_total_ops.extend(metrics['player2_operations'])

        # Calculate averages
        avg_time_p1 = sum(p1_total_time)/len(p1_total_time) if p1_total_time else 0
        avg_ops_p1 = sum(p1_total_ops)/len(p1_total_ops) if p1_total_ops else 0
        avg_time_p2 = sum(p2_total_time)/len(p2_total_time) if p2_total_time else 0
        avg_ops_p2 = sum(p2_total_ops)/len(p2_total_ops) if p2_total_ops else 0

        print(f"\nResults: {p1_name} vs {p2_name}")
        print(f"Games: {num_games}, {p1_name} Wins: {p1_wins}, {p2_name} Wins: {p2_wins}, Draws: {draws}")
        
        # Customize output based on algorithm type
        p1_metric = "Nodes" if p1_name in ["Minimax", "Alpha-Beta"] else "API Calls"
        p2_metric = "Nodes" if p2_name in ["Minimax", "Alpha-Beta"] else "API Calls"
        
        print(f"{p1_name} Avg Time/move: {avg_time_p1:.6f}s, Avg {p1_metric}/move: {avg_ops_p1:.1f}")
        print(f"{p2_name} Avg Time/move: {avg_time_p2:.6f}s, Avg {p2_metric}/move: {avg_ops_p2:.1f}")
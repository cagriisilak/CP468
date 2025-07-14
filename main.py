#main.py
import testing, algorithms, functions


def main():
    end = False
    while not(end):
        valid_inputs = [1, 2, 3, 4]
        try:
            user_input = int(input("\nEnter the number corresponding with the option you would like to select:\n"
                                "1: Standardized Test\n"
                                "2: Standardized Test with Selected Algorithim\n"
                                "3: Watch Game in Real Time\n"
                                "4: End Program\n"
                                "Enter here: "))
            functions.check_input(user_input, valid_inputs)

            if user_input == 1:
                try:
                    num_games = int(input("How many games should the test run? "))
                    board_size = int(input("How big should the board be (3 is standard)? "))
                    testing.run_performance_tests(num_games=num_games, board_size=board_size)
                except ValueError:
                    print("Invalid input. Please enter integer values for the number of games and board size.\n")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}\n")

            elif user_input == 2:
                print("\nAvalible Algorithims:\n"
                "1: simple_algo\n"
                "2: minimax\n"
                "3: alpha_beta_minimax\n"
                "4: gemini\n")
                algos = [algorithms.simple_algo, algorithms.minimax_algo, algorithms.alpha_beta_algo, algorithms.gemini_algo]
                try:
                    algo1 = int(input("Select Player 1's algorithim: "))
                    functions.check_input(algo1, valid_inputs)
                    algo2 = int(input("Select Player 2's algorithim: "))
                    functions.check_input(algo2, valid_inputs)
                    board_size = int(input("How big should the board be (3 is standard)? "))
                    algo1 = algo1 - 1
                    algo2 = algo2 - 1
                    testing.run_game_with_metrics(algos[algo1], algos[algo2], board_size)

                except ValueError as e:
                    print(f"Invalid input, please select from this list or select an appropriate board size - {valid_inputs}\n")

                except Exception as e:
                            print(f"An unexpected error occurred: {e}\n")
            
            elif user_input == 3:
                print("\nAvalible Algorithims:\n"
                "1: simple_algo\n"
                "2: minimax\n"
                "3: alpha_beta_minimax\n"
                "4: gemini\n")
                algos = [algorithms.simple_algo, algorithms.minimax_algo, algorithms.alpha_beta_algo, algorithms.gemini_algo]
                try:
                    algo1 = int(input("Select Player 1's algorithim: "))
                    functions.check_input(algo1, valid_inputs)
                    algo2 = int(input("Select Player 2's algorithim: "))
                    functions.check_input(algo2, valid_inputs)
                    board_size = int(input("How big should the board be (3 is standard)? "))
                    algo1 = algo1 - 1
                    algo2 = algo2 - 1
                    functions.run_game(algos[algo1], algos[algo2], board_size=board_size, visualize=True)

                except ValueError as e:
                    print(f"Invalid input, please select from this list or select an appropriate board size - {valid_inputs}\n")

                except Exception as e:
                            print(f"An unexpected error occurred: {e}\n")

            elif user_input == 4:
                print("Ending program")
                end = True

        except ValueError as e:
            print(f"Invalid input, please select from this list - {valid_inputs}\n")

        except Exception as e:
                    print(f"An unexpected error occurred: {e}\n")
        

if __name__=="__main__":
    main()
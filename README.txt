# Tic-Tac-Toe AI Showdown

This program allows you to run and visualize Tic-Tac-Toe games between different AI algorithms. You can also run performance tests to compare the algorithms.

## Features

* **Standardized Tests:** Run multiple games to compare the performance of different AI algorithms.
* **Custom Game Play:** Play games with selected algorithms and visualize the gameplay in real-time.
* **Algorithm Selection:** Choose from various AI algorithms, including:
    * `simple_algo`: A basic algorithm that makes the first available move.
    * `minimax_algo`: An AI using the Minimax algorithm.
    * `alpha_beta_algo`: An AI using the Alpha-Beta Pruning Minimax algorithm.
    * `gemini_algo`: An AI powered by Google's Gemini API.
* **Board Size Configuration:** Play on boards of different sizes (e.g., 3x3, 4x4).
* **Performance Metrics:** Track time and node/API call metrics for each move.

## Getting Started

### Prerequisites

* Python 3.x installed on your system.
* Required Python packages:
    * `google-generativeai` (for the Gemini algorithm)
* Google Gemini API Key (for the Gemini algorithm)

### Installation

1.  **Install the required packages:**

    ```bash
    pip install google-generativeai
    ```

2.  **Set your Google Gemini API key:**

    * In the `algorithms.py` file, replace `"AIzaSyAKCwoqMGg6Fb-y8W7wIRKomrfvj1VQ0Cg"` with your actual Gemini API key.

### Running the Program

You can run the program in two ways:

1.  **Using the executable file (`dist/main.exe`):**

    * Navigate to the `dist` folder and run the `main.exe` file.

2.  **Running the Python script (`main.py`):**

    * Open a terminal and navigate to the directory containing `main.py`.
    * Run the script using:

        ```bash
        python main.py
        ```

### Usage

The program will present you with a menu:

1.  **Standardized Test:** Runs performance tests between selected algorithms. You will be prompted to enter the number of games and board size.
2.  **Standardized Test with Selected Algorithm:** Runs a single game between two user selected algorithms. You will be prompted to select the algorithms and the board size.
3.  **Watch Game in Real Time:** Runs a game between two selected algorithms and displays the board and metrics for each move in the terminal.
4.  **End Program:** Exits the program.

For options 2 and 3, you'll be prompted to choose algorithms for Player 1 and Player 2. Available algorithms are listed in the terminal. You will also be prompted for the board size.

### File Structure

* `main.py`: The main script that runs the program.
* `functions.py`: Contains functions for board manipulation and game logic.
* `algorithms.py`: Contains the AI algorithms.
* `testing.py`: Contains functions for running performance tests.
* `dist/main.exe`: The executable version of the program.

### Notes

* The `gemini_algo` relies on the Google Gemini API, so you'll need an API key to use it (See algorithims.py). The exe uses our api key.
* The performance of the `gemini_algo` may vary depending on the API's response time.


(ADDITIONAL INFO: Many files such as files from group22_TermProject/venv/Lib/site-packages and group22_TermProject/build/main/main.pkg, and the file dist/main are MISSING from this repository as they were too large to upload to github. If anyone reading this needs access to those files, email me at cagri.isilak@gmail.com for the original file.)

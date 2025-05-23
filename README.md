# Tic Tac Toe with AI

A Python implementation of the classic Tic Tac Toe game featuring an AI player that uses the minimax algorithm to make optimal moves.

## Features

- **Human vs AI gameplay**: Play against an intelligent AI opponent
- **Interactive GUI**: Clean and intuitive graphical user interface using Pygame
- **Perfect AI**: The AI player will never lose - it will either win or draw

## Files

- `tictactoe.py` - Core game logic and AI implementation
- `runner.py` - Pygame-based graphical user interface
- `requirements.txt` - Python dependencies

## How to Run

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the game:
   ```bash
   python runner.py
   ```

## Game Rules

- Players take turns placing X's and O's on a 3x3 grid
- The first player to get three marks in a row (horizontally, vertically, or diagonally) wins
- If all squares are filled and no player has three in a row, the game is a draw

## AI Implementation

The AI uses the **minimax algorithm** to evaluate all possible game states and choose the optimal move:

- **X player** (maximizing player): Tries to maximize the score
- **O player** (minimizing player): Tries to minimize the score
- **Scoring**: +1 for X win, -1 for O win, 0 for draw

The algorithm recursively explores all possible future game states to determine the best move for the current player.
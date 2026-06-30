# Tic Tac Toe

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Repository Size](https://img.shields.io/github/repo-size/arnavmaheshwari/TicTacToe?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/arnavmaheshwari/TicTacToe?style=flat-square)

An interactive command-line implementation of the classic Tic Tac Toe game in Python.

</div>

---

## 📋 Overview

Tic Tac Toe is a simple yet engaging implementation of the timeless two-player strategy game. This Python-based application provides an interactive terminal interface where players can compete against each other in alternating turns.

**Key Highlights:**
- Turn-based gameplay with two human players
- Real-time board visualization
- Input validation and conflict detection
- Simple and intuitive command-line interface

---

## ✨ Features

- **Interactive Gameplay** — Players alternate turns entering cell numbers (0-8) to place their marks
- **Real-time Board Display** — Visual representation of the board after each move
- **Win Detection** — Automatically detects horizontal, vertical, and diagonal winning combinations
- **Tie Detection** — Identifies when the board is full with no winner
- **Input Validation** — Prevents players from overwriting occupied cells
- **Player Feedback** — Clear prompts and messages guiding players through the game

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.x |
| **Type** | Command-line Application |

---

## 📁 Project Structure

```
TicTacToe/
├── TicTacToe.py      # Main game logic and UI
└── README.md         # Project documentation
```

### File Description

- **TicTacToe.py** — Contains all game logic including:
  - `check()` — Validates win conditions
  - `printboard()` — Displays the current board state
  - `addToBoard()` — Handles player input and board updates
  - Main game loop for alternating turns

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Terminal or command-line interface

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/arnavmaheshwari/TicTacToe.git
   cd TicTacToe
   ```

2. **Verify Python installation:**
   ```bash
   python --version
   ```

### Running the Game

Execute the game with:

```bash
python TicTacToe.py
```

---

## 🎮 How to Play

1. **Start the Game** — Run the Python script
2. **View the Board** — The board displays cells numbered 0-8:
   ```
   0 | 1 | 2
   --------- 
   3 | 4 | 5
   ---------
   6 | 7 | 8
   ```
3. **Player Turn** — When prompted, enter a cell number (0-8) to place your mark
4. **Alternating Moves** — Players alternate turns (X goes first)
5. **Win or Tie** — The game announces the winner or declares a tie when appropriate

### Example Gameplay

```
Welcome To Tic Tac Toe!
Board: -
        0       |        1       |       2
--------------------------------------------------
        3       |        4       |       5
--------------------------------------------------
        6       |        7       |       8
X goes first...
Enter the cell number to add X  : 4
```

---

## 🎯 Game Rules

- The board is a 3×3 grid with cells numbered 0-8
- Player X moves first, alternating with Player O
- Players take turns selecting empty cells
- A player wins by placing three marks in a row (horizontal, vertical, or diagonal)
- If all 9 cells are filled with no winner, the game is a tie

---

## 🔮 Future Improvements

- **Difficulty Levels** — Implement AI opponent with varying skill levels
- **Game Statistics** — Track wins, losses, and ties across multiple games
- **Enhanced UI** — Develop a graphical interface using tkinter or pygame
- **Play Again** — Add functionality to replay without restarting the script
- **Move History** — Display a record of all moves made during the game
- **Network Play** — Enable multiplayer gaming over network connections

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request with a clear description of your changes

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 👤 Author

**Arnav Maheshwari**  
GitHub: [@arnavmaheshwari](https://github.com/arnavmaheshwari)

---

## 🙏 Acknowledgements

- Classic Tic Tac Toe game inspiration
- Python standard library for core functionality

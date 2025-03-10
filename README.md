# 🎰 Python Slot Machine 🎰

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-brightgreen.svg)](https://docs.python.org/3/library/tkinter.html)

<div align="center">
  <p><strong>A casino-style slot machine game built with Python!</strong></p>
  <p>Test your luck with this exciting slot machine simulator available in both CLI and GUI versions.</p>
</div>

## 📸 Screenshots

<div align="center">
  <img src="assets/app image.jpg" width="400" alt="GUI Version">
</div>

## ✨ Features

- 💰 **Deposit System** - Add funds to your virtual wallet
- 🎮 **Flexible Betting** - Choose 1-3 lines to bet on
- 💵 **Custom Wagers** - Place bets from $1 to $100 per line
- 🎲 **Authentic Experience** - Real casino-style randomized results
- 🏆 **Win Tracking** - Real-time balance and winnings display
- 💸 **Cash Out** - Leave with your winnings anytime
- 🎭 **Two Interfaces** - Choose between CLI or GUI versions
- ✅ **Visual Feedback** - Animated spins and highlighted winning lines (GUI)

## 🎮 How to Play

### CLI Version
1. Launch the terminal-based game
2. Deposit your starting funds
3. Select betting lines (1-3)
4. Set your bet amount per line
5. Spin and watch for matching symbols
6. Win when identical symbols line up
7. Play again or cash out your winnings

### GUI Version
1. Launch the graphical interface
2. Deposit funds using the deposit field
3. Adjust lines and bet amount with the spinboxes
4. Click **SPIN** to play a round
5. Watch for gold-highlighted winning lines
6. Click **CASH OUT** when you're ready to finish

## 💎 Symbol Values

<div align="center">

| Symbol | Rarity | Multiplier |
|:------:|:------:|:----------:|
| **A** | 🔶 Rare | 5× bet |
| **B** | 🔷 Uncommon | 4× bet |
| **C** | 🔹 Common | 3× bet |
| **D** | 🔸 Very Common | 2× bet |

</div>

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kabyik-kayal/python-slot-machine.git
   cd python-slot-machine
   ```

2. **Launch the game:**
   
   For CLI version:
   ```bash
   python main.py
   ```
   
   For GUI version:
   ```bash
   python app.py
   ```

## 📋 Requirements

- Python 3.x
- Tkinter (included in standard Python installation)

## 📁 Project Structure

- `main.py` - Command-line interface with core game logic
- `app.py` - GUI version built with Tkinter

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built as a Python programming exercise
- Inspired by classic casino slot machines
- CLI version based on Tech With Tim's Tutorial

#!/usr/bin/env python3
"""
Tic Tac Toe Game with Tkinter

Features:
- Single Player Mode: Player vs Computer (Minimax AI)
- Two Player Mode: Player vs Player
- Professional UI with animations
- Score tracking
- Reset and mode switching
"""

import tkinter as tk
from tkinter import messagebox, font
import copy
import random

class TicTacToeGame:
    """Tic Tac Toe game logic and AI"""
    
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
    
    def make_move(self, row, col, player):
        """Make a move on the board"""
        if self.board[row][col] == '' and not self.game_over:
            self.board[row][col] = player
            return True
        return False
    
    def check_winner(self):
        """Check if there's a winner or draw"""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return self.board[0][2]
        
        # Check for draw
        if all(self.board[row][col] != '' for row in range(3) for col in range(3)):
            return 'Draw'
        
        return None
    
    def get_available_moves(self):
        """Get list of available moves"""
        moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    moves.append((row, col))
        return moves
    
    def is_board_full(self):
        """Check if board is full"""
        return all(self.board[row][col] != '' for row in range(3) for col in range(3))
    
    def reset_game(self):
        """Reset the game board"""
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
    
    def minimax(self, board, depth, is_maximizing, alpha, beta):
        """
        Minimax algorithm with alpha-beta pruning for optimal AI moves
        
        Args:
            board: Current board state
            depth: Current depth in game tree
            is_maximizing: True if maximizing player (AI), False if minimizing (human)
            alpha: Alpha value for pruning
            beta: Beta value for pruning
        
        Returns:
            Best score for current board state
        """
        # Create temporary game state to check winner
        temp_game = TicTacToeGame()
        temp_game.board = board
        result = temp_game.check_winner()
        
        # Terminal states
        if result == 'O':  # AI wins
            return 10 - depth
        elif result == 'X':  # Player wins
            return depth - 10
        elif result == 'Draw':
            return 0
        
        if is_maximizing:
            # AI's turn (maximizing)
            max_eval = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = 'O'
                        eval_score = self.minimax(board, depth + 1, False, alpha, beta)
                        board[row][col] = ''
                        max_eval = max(max_eval, eval_score)
                        alpha = max(alpha, eval_score)
                        if beta <= alpha:
                            break  # Beta cutoff
            return max_eval
        else:
            # Player's turn (minimizing)
            min_eval = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = 'X'
                        eval_score = self.minimax(board, depth + 1, True, alpha, beta)
                        board[row][col] = ''
                        min_eval = min(min_eval, eval_score)
                        beta = min(beta, eval_score)
                        if beta <= alpha:
                            break  # Alpha cutoff
            return min_eval
    
    def get_best_move(self):
        """Get the best move for AI using minimax algorithm"""
        best_score = float('-inf')
        best_move = None
        
        # Try all available moves
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    # Make the move
                    self.board[row][col] = 'O'
                    
                    # Calculate score using minimax
                    score = self.minimax(self.board, 0, False, float('-inf'), float('inf'))
                    
                    # Undo the move
                    self.board[row][col] = ''
                    
                    # Update best move
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        
        return best_move


class TicTacToeGUI:
    """GUI for Tic Tac Toe game"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe Game")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg='#2c3e50')
        
        # Game state
        self.game = TicTacToeGame()
        self.mode = None  # 'single' or 'two_player'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.player_symbol = 'X'
        self.computer_symbol = 'O'
        
        # Score tracking
        self.scores = {'X': 0, 'O': 0, 'Draw': 0}
        
        # Fonts
        self.title_font = font.Font(family='Helvetica', size=24, weight='bold')
        self.button_font = font.Font(family='Helvetica', size=32, weight='bold')
        self.label_font = font.Font(family='Helvetica', size=12)
        
        # Colors
        self.colors = {
            'bg': '#2c3e50',
            'button_bg': '#ecf0f1',
            'button_hover': '#3498db',
            'X': '#e74c3c',
            'O': '#3498db',
            'win': '#27ae60'
        }
        
        # Show mode selection
        self.show_mode_selection()
    
    def show_mode_selection(self):
        """Show mode selection screen"""
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="TIC TAC TOE",
            font=self.title_font,
            bg=self.colors['bg'],
            fg='white'
        )
        title_label.pack(pady=30)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.root,
            text="Choose Game Mode",
            font=self.label_font,
            bg=self.colors['bg'],
            fg='white'
        )
        subtitle_label.pack(pady=10)
        
        # Mode buttons frame
        button_frame = tk.Frame(self.root, bg=self.colors['bg'])
        button_frame.pack(pady=30)
        
        # Single player button
        single_btn = tk.Button(
            button_frame,
            text="🤖 Single Player\n(vs Computer)",
            font=self.label_font,
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            activeforeground='white',
            width=20,
            height=4,
            relief=tk.RAISED,
            bd=3,
            cursor='hand2',
            command=lambda: self.start_game('single')
        )
        single_btn.pack(pady=10)
        
        # Two player button
        two_player_btn = tk.Button(
            button_frame,
            text="👥 Two Player\n(vs Friend)",
            font=self.label_font,
            bg='#e74c3c',
            fg='white',
            activebackground='#c0392b',
            activeforeground='white',
            width=20,
            height=4,
            relief=tk.RAISED,
            bd=3,
            cursor='hand2',
            command=lambda: self.start_game('two_player')
        )
        two_player_btn.pack(pady=10)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Single Player: You (X) vs Computer (O)\nTwo Player: Player 1 (X) vs Player 2 (O)",
            font=('Helvetica', 10),
            bg=self.colors['bg'],
            fg='#bdc3c7',
            justify=tk.LEFT
        )
        instructions.pack(pady=20)
    
    def start_game(self, mode):
        """Start the game with selected mode"""
        self.mode = mode
        self.game.reset_game()
        self.create_game_board()
    
    def create_game_board(self):
        """Create the game board UI"""
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Top frame with info and controls
        top_frame = tk.Frame(self.root, bg=self.colors['bg'])
        top_frame.pack(pady=10)
        
        # Mode indicator
        mode_text = "Single Player (vs Computer)" if self.mode == 'single' else "Two Player Mode"
        mode_label = tk.Label(
            top_frame,
            text=mode_text,
            font=self.label_font,
            bg=self.colors['bg'],
            fg='white'
        )
        mode_label.pack()
        
        # Current turn indicator
        self.turn_label = tk.Label(
            top_frame,
            text=self.get_turn_text(),
            font=self.label_font,
            bg=self.colors['bg'],
            fg='#3498db'
        )
        self.turn_label.pack(pady=5)
        
        # Score frame
        score_frame = tk.Frame(self.root, bg=self.colors['bg'])
        score_frame.pack(pady=10)
        
        self.score_label = tk.Label(
            score_frame,
            text=self.get_score_text(),
            font=('Helvetica', 11),
            bg=self.colors['bg'],
            fg='white'
        )
        self.score_label.pack()
        
        # Game board frame
        board_frame = tk.Frame(self.root, bg=self.colors['bg'])
        board_frame.pack(pady=10)
        
        # Create 3x3 grid of buttons
        for row in range(3):
            for col in range(3):
                btn = tk.Button(
                    board_frame,
                    text='',
                    font=self.button_font,
                    width=5,
                    height=2,
                    bg=self.colors['button_bg'],
                    activebackground=self.colors['button_hover'],
                    relief=tk.RAISED,
                    bd=3,
                    cursor='hand2',
                    command=lambda r=row, c=col: self.on_button_click(r, c)
                )
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = btn
        
        # Control buttons frame
        control_frame = tk.Frame(self.root, bg=self.colors['bg'])
        control_frame.pack(pady=20)
        
        # Reset button
        reset_btn = tk.Button(
            control_frame,
            text="🔄 New Game",
            font=self.label_font,
            bg='#27ae60',
            fg='white',
            activebackground='#229954',
            width=12,
            height=2,
            relief=tk.RAISED,
            bd=2,
            cursor='hand2',
            command=self.reset_game
        )
        reset_btn.grid(row=0, column=0, padx=5)
        
        # Change mode button
        mode_btn = tk.Button(
            control_frame,
            text="🏠 Change Mode",
            font=self.label_font,
            bg='#e67e22',
            fg='white',
            activebackground='#d35400',
            width=12,
            height=2,
            relief=tk.RAISED,
            bd=2,
            cursor='hand2',
            command=self.show_mode_selection
        )
        mode_btn.grid(row=0, column=1, padx=5)
    
    def get_turn_text(self):
        """Get the current turn text"""
        if self.mode == 'single':
            if self.game.current_player == 'X':
                return "Your Turn (X)"
            else:
                return "Computer's Turn (O)"
        else:
            return f"Player {self.game.current_player}'s Turn"
    
    def get_score_text(self):
        """Get score display text"""
        if self.mode == 'single':
            return f"You: {self.scores['X']} | Computer: {self.scores['O']} | Draws: {self.scores['Draw']}"
        else:
            return f"Player X: {self.scores['X']} | Player O: {self.scores['O']} | Draws: {self.scores['Draw']}"
    
    def on_button_click(self, row, col):
        """Handle button click"""
        if self.game.game_over:
            return
        
        # Player makes a move
        if self.game.make_move(row, col, self.game.current_player):
            self.update_button(row, col, self.game.current_player)
            
            # Check for winner
            winner = self.game.check_winner()
            if winner:
                self.end_game(winner)
                return
            
            # Switch player
            self.game.current_player = 'O' if self.game.current_player == 'X' else 'X'
            self.turn_label.config(text=self.get_turn_text())
            
            # If single player mode and now computer's turn
            if self.mode == 'single' and self.game.current_player == 'O':
                self.root.after(500, self.computer_move)
    
    def computer_move(self):
        """Make computer move using minimax"""
        if self.game.game_over:
            return
        
        # Get best move from minimax algorithm
        move = self.game.get_best_move()
        
        if move:
            row, col = move
            self.game.make_move(row, col, 'O')
            self.update_button(row, col, 'O')
            
            # Check for winner
            winner = self.game.check_winner()
            if winner:
                self.end_game(winner)
                return
            
            # Switch back to player
            self.game.current_player = 'X'
            self.turn_label.config(text=self.get_turn_text())
    
    def update_button(self, row, col, player):
        """Update button appearance after move"""
        self.buttons[row][col].config(
            text=player,
            fg=self.colors[player],
            state='disabled',
            disabledforeground=self.colors[player]
        )
    
    def end_game(self, winner):
        """Handle game end"""
        self.game.game_over = True
        self.game.winner = winner
        
        # Update scores
        self.scores[winner] += 1
        self.score_label.config(text=self.get_score_text())
        
        # Highlight winning cells
        self.highlight_winner()
        
        # Show result message
        if winner == 'Draw':
            message = "It's a Draw!"
            title = "Game Over"
        elif self.mode == 'single':
            if winner == 'X':
                message = "🎉 Congratulations! You Win!"
                title = "Victory!"
            else:
                message = "💻 Computer Wins! Better luck next time."
                title = "Game Over"
        else:
            message = f"🎉 Player {winner} Wins!"
            title = "Victory!"
        
        # Show message after a brief delay
        self.root.after(500, lambda: messagebox.showinfo(title, message))
    
    def highlight_winner(self):
        """Highlight winning cells"""
        winner = self.game.winner
        if winner == 'Draw':
            return
        
        # Check rows
        for row in range(3):
            if self.game.board[row][0] == self.game.board[row][1] == self.game.board[row][2] == winner:
                for col in range(3):
                    self.buttons[row][col].config(bg=self.colors['win'])
                return
        
        # Check columns
        for col in range(3):
            if self.game.board[0][col] == self.game.board[1][col] == self.game.board[2][col] == winner:
                for row in range(3):
                    self.buttons[row][col].config(bg=self.colors['win'])
                return
        
        # Check diagonals
        if self.game.board[0][0] == self.game.board[1][1] == self.game.board[2][2] == winner:
            for i in range(3):
                self.buttons[i][i].config(bg=self.colors['win'])
            return
        
        if self.game.board[0][2] == self.game.board[1][1] == self.game.board[2][0] == winner:
            for i in range(3):
                self.buttons[i][2-i].config(bg=self.colors['win'])
    
    def reset_game(self):
        """Reset the game"""
        self.game.reset_game()
        
        # Reset all buttons
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(
                    text='',
                    state='normal',
                    bg=self.colors['button_bg']
                )
        
        self.turn_label.config(text=self.get_turn_text())


def main():
    """Main function to run the game"""
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()


# Game Rules and Features:
"""
TIC TAC TOE GAME

GAME MODES:
1. Single Player Mode:
   - Player (X) vs Computer (O)
   - Computer uses Minimax algorithm for optimal moves
   - Computer and player alternate turns
   - Computer moves are delayed by 500ms for better UX

2. Two Player Mode:
   - Player 1 (X) vs Player 2 (O)
   - Players alternate turns
   - Local multiplayer on same device

MINIMAX ALGORITHM:
- The AI uses the minimax algorithm with alpha-beta pruning
- Evaluates all possible moves and chooses the optimal one
- The AI is unbeatable when playing optimally
- Depth-based scoring ensures the AI prefers quick wins

CONTROLS:
- Click on any empty cell to make a move
- "New Game" button: Start a new round (keeps scores)
- "Change Mode" button: Return to mode selection screen

SCORING:
- Wins, losses, and draws are tracked
- Scores persist across rounds until mode is changed
- Score display adapts to current game mode

WINNING CONDITIONS:
- Three in a row horizontally
- Three in a row vertically
- Three in a row diagonally
- Winning cells are highlighted in green

FEATURES:
- Professional UI with custom colors and fonts
- Turn indicator shows whose turn it is
- Score tracking for multiple rounds
- Visual feedback for moves and wins
- Responsive button interactions
- Mode selection screen
- Easy reset and mode switching
"""
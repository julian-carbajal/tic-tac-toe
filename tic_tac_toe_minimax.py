"""
Tic Tac Toe with Minimax AI Implementation
This module implements a Tic Tac Toe game with an unbeatable AI using the minimax algorithm.
The AI player always makes the optimal move by looking ahead at all possible game states.
"""

class TicTacToe:
    def __init__(self):
        """Initialize an empty board."""
        self.board = [' ' for _ in range(9)]
        self.human_player = 'X'
        self.ai_player = 'O'

    def print_board(self):
        """Display the current game board."""
        for i in range(0, 9, 3):
            print(f'{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}')
            if i < 6:
                print('---------')

    def available_moves(self):
        """Return list of available moves."""
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, position, player):
        """Make a move on the board."""
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def check_winner(self):
        """Check if there's a winner. Returns 'X', 'O', 'Tie', or None."""
        # Check rows, columns and diagonals
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != ' '):
                return self.board[combo[0]]

        if ' ' not in self.board:
            return 'Tie'
        
        return None

    def minimax(self, board, depth, is_maximizing):
        """
        Implement the minimax algorithm.
        Returns the best score possible for the current board state.
        """
        result = self.check_winner()
        if result == self.ai_player:
            return 1
        if result == self.human_player:
            return -1
        if result == 'Tie':
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for move in self.available_moves():
                board[move] = self.ai_player
                score = self.minimax(board, depth + 1, False)
                board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.available_moves():
                board[move] = self.human_player
                score = self.minimax(board, depth + 1, True)
                board[move] = ' '
                best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        """Get the best possible move for the AI using minimax."""
        best_score = float('-inf')
        best_move = None

        for move in self.available_moves():
            self.board[move] = self.ai_player
            score = self.minimax(self.board, 0, False)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def play_game(self):
        """Main game loop."""
        print("Welcome to Tic Tac Toe!")
        print("You are X and the AI is O")
        print("Positions are numbered 0-8, left to right, top to bottom")
        
        while True:
            self.print_board()
            
            # Human turn
            while True:
                try:
                    position = int(input("Enter your move (0-8): "))
                    if 0 <= position <= 8 and self.make_move(position, self.human_player):
                        break
                    print("Invalid move, try again.")
                except ValueError:
                    print("Please enter a number between 0 and 8.")

            # Check if human won
            if self.check_winner() == self.human_player:
                self.print_board()
                print("You win! Congratulations!")
                break
            elif self.check_winner() == 'Tie':
                self.print_board()
                print("It's a tie!")
                break

            # AI turn
            print("\nAI is thinking...")
            ai_move = self.get_best_move()
            self.make_move(ai_move, self.ai_player)

            # Check if AI won
            if self.check_winner() == self.ai_player:
                self.print_board()
                print("AI wins!")
                break
            elif self.check_winner() == 'Tie':
                self.print_board()
                print("It's a tie!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()

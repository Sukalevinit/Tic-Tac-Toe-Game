import os
import random
from colorama import Fore, Style, init
init(autoreset=True)

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.player1_score = 0
        self.player2_score = 0
        self.tie_score = 0

    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + "\n     TIC-TAC-TOE     ")
        print(Fore.MAGENTA + f" Player 1 (X): {self.player1_score} | Player 2/Computer (O): {self.player2_score} | Ties: {self.tie_score}\n")
        for i in range(3):
            print(Fore.YELLOW + f"  {self.board[i * 3]} | {self.board[i * 3 + 1]} | {self.board[i * 3 + 2]}")
            if i < 2:
                print(Fore.GREEN + " ---+---+---")

    def make_move(self, position, player):
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return self.board[condition[0]]
        if " " not in self.board:
            return "Tie"
        return None

    def reset_board(self):
        self.board = [" " for _ in range(9)]

    def computer_move(self):
        empty_positions = [i for i in range(9) if self.board[i] == " "]
        return random.choice(empty_positions)

    def start_game(self):
        print(Fore.CYAN + "\nWelcome to Advanced Tic-Tac-Toe!\n")
        game_mode = input("Choose game mode (1 for Player vs Computer, 2 for 2 Players): ")

        while game_mode not in ("1", "2"):
            game_mode = input("Invalid choice. Enter 1 or 2: ")

        while True:
            self.display_board()

            for turn in range(9):
                player = "X" if turn % 2 == 0 else "O"

                if game_mode == "1" and player == "O":
                    position = self.computer_move()
                else:
                    while True:
                        try:
                            position = int(input(Fore.CYAN + f"Player {player}'s turn. Enter position (1-9): ")) - 1
                            if position < 0 or position > 8 or not self.make_move(position, player):
                                raise ValueError
                            break
                        except ValueError:
                            print(Fore.RED + "Invalid input. Try again.")

                self.make_move(position, player)
                self.display_board()
                winner = self.check_winner()

                if winner:
                    if winner == "X":
                        print(Fore.GREEN + "\nPlayer X wins!")
                        self.player1_score += 1
                    elif winner == "O":
                        if game_mode == "1":
                            print(Fore.RED + "\nComputer wins!")
                        else:
                            print(Fore.GREEN + "\nPlayer O wins!")
                        self.player2_score += 1
                    else:
                        print(Fore.YELLOW + "\nIt's a tie!")
                        self.tie_score += 1
                    break

            if not winner:
                print(Fore.YELLOW + "\nIt's a tie!")
                self.tie_score += 1

            play_again = input(Fore.CYAN + "\nDo you want to play again? (y/n): ").lower()
            if play_again != "y":
                break
            self.reset_board()

if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()

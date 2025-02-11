from stockfish import Stockfish


def current_board_state():
    print("Board")

def current_player_state():
    print("Player")

def current_player_move():
    print("Move")

def current_board_state():
    print("Board")

class ChessBoard:
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        # Setup initial positions
        self.board[0] = ["R", "N", "B", "Q", "K", "B", "N", "R"]
        self.board[1] = ["P"] * 8
        self.board[6] = ["p"] * 8
        self.board[7] = ["r", "n", "b", "q", "k", "b", "n", "r"]

    def display(self):
        for row in self.board:
            print(" ".join(row))

    def move_piece(self, start, end):
        # Convert algebraic notation (e.g., 'e2') to board indices
        start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')
        end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')

        # Get the piece at the start position
        piece = self.board[start_row][start_col]

        if piece == " ":
            print(f"No piece at {start} to move.")
            return

        # Perform the move
        self.board[start_row][start_col] = " "
        self.board[end_row][end_col] = piece
        print(f"Moved {piece} from {start} to {end}.")




chessboard = ChessBoard()
chessboard.display()

# Example moves
chessboard.move_piece("e2", "e4")  # Move pawn from e2 to e4
chessboard.display()

chessboard.move_piece("g8", "f6")  # Move knight from g8 to f6
chessboard.display()

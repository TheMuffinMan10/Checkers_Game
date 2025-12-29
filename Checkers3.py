import tkinter as tk

BOARD_SIZE = 8

def in_bounds(r, c):
    return 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE


class Board:
    def __init__(self):
        self.virBoard = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.turn = "W"  # W or B


class Piece:
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour  # "W" or "B"

    def directions(self):
        # Normal pawns only
        return [(-1, -1), (-1, 1)] if self.colour == "B" else [(1, -1), (1, 1)]

    def enemy(self):
        return "B" if self.colour == "W" else "W"

    '''
    def move(self):
        clean_squares()
        for dr, dc in self.directions():
            self.check_direction(dr, dc)
    '''

    def check_direction(self, dr, dc):
        r1, c1 = self.row + dr, self.col + dc

        # Normal move
        if in_bounds(r1, c1) and game.virBoard[r1][c1] is None:
            highlight_square(r1, c1, self, False)

        # Capture
        elif in_bounds(r1, c1):
            target = game.virBoard[r1][c1]
            r2, c2 = self.row + 2 * dr, self.col + 2 * dc
            if (
                target
                and target.colour == self.enemy()
                and in_bounds(r2, c2)
                and game.virBoard[r2][c2] is None
            ):
                highlight_square(r2, c2, self, True)

    def transfer(self, r, c, capture):
        # Remove old
        board[self.row][self.col].config(text="")
        game.virBoard[self.row][self.col] = None

        # Capture
        if capture:
            mid_r = (self.row + r) // 2
            mid_c = (self.col + c) // 2
            board[mid_r][mid_c].config(text="")
            game.virBoard[mid_r][mid_c] = None

        # Place new
        new_piece = Piece(r, c, self.colour)
        game.virBoard[r][c] = new_piece

        btn = board[r][c]
        btn.config(
            text="O",
            font=("Consolas", 12, "bold"),
            foreground="white" if self.colour == "W" else "red",
            command=lambda p=new_piece: move(p),
        )

        clean_squares()
        switch_turn()

#----------------- New Capture functions --------- #

    def find_capture_sequences(self, row, col, visited=None):
        if visited is None:
            visited = set()

        sequences = []
        found_capture = False

        for dr, dc in self.directions():
            r1, c1 = row + dr, col + dc
            r2, c2 = row + 2*dr, col + 2*dc

            if (
                in_bounds(r2, c2)
                and (r1, c1) not in visited
                and game.virBoard[r1][c1]
                and game.virBoard[r1][c1].colour == self.enemy()
                and game.virBoard[r2][c2] is None
            ):
                found_capture = True

                new_visited = visited | {(r1, c1)}
                deeper = self.find_capture_sequences(r2, c2, new_visited)

                if deeper:
                    for seq in deeper:
                        sequences.append({
                            "path": [(r2, c2)] + seq["path"],
                            "captures": [(r1, c1)] + seq["captures"]
                        })
                else:
                    sequences.append({
                        "path": [(r2, c2)],
                        "captures": [(r1, c1)]
                    })

        return sequences

    def move(self):
        clean_squares()

        sequences = self.find_capture_sequences(self.row, self.col)

        if sequences:
            # Enforce MAX capture rule
            max_len = max(len(seq["captures"]) for seq in sequences)
            best = [s for s in sequences if len(s["captures"]) == max_len]

            # Highlight ONLY first step of best sequences
            for seq in best:
                r, c = seq["path"][0]
                highlight_square(r, c, self, True, seq)
        else:
            # No capture → allow normal moves
            for dr, dc in self.directions():
                r, c = self.row + dr, self.col + dc
                if in_bounds(r, c) and game.virBoard[r][c] is None:
                    highlight_square(r, c, self, False)

    

    def execute_sequence(self, r, c, sequence):
        # Remove current piece
        board[self.row][self.col].config(text="")
        game.virBoard[self.row][self.col] = None

        # Remove all captured pieces
        for cr, cc in sequence["captures"]:
            board[cr][cc].config(text="")
            game.virBoard[cr][cc] = None

        # Place new piece
        new_piece = Piece(r, c, self.colour)
        game.virBoard[r][c] = new_piece

        btn = board[r][c]
        btn.config(
            text="O",
            font=("Consolas", 12, "bold"),
            foreground="white" if self.colour == "W" else "red",
            command=lambda p=new_piece: move(p),
        )

        clean_squares()
        switch_turn()


# ---------------- UI HELPERS ---------------- #


'''
def highlight_square(r, c, piece, capture):
    btn = board[r][c]
    btn.config(
        background="green",
        command=lambda: piece.transfer(r, c, capture),
    )'''

def highlight_square(r, c, piece, capture, sequence=None):
        btn = board[r][c]
        btn.config(
            background="green",
            command=lambda: piece.execute_sequence(r, c, sequence) if capture else piece.transfer(r, c, False),
        )

def clean_squares():
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c]["background"] == "green":
                board[r][c].config(
                    background="black" if (r + c) % 2 else "white",
                    command=lambda rr=r, cc=c: move(game.virBoard[rr][cc]),
                )


def move(piece):
    if piece and piece.colour == game.turn:
        piece.move()


def switch_turn():
    game.turn = "B" if game.turn == "W" else "W"
    lblMove.config(
        text=f"{'White' if game.turn == 'W' else 'Black'} to move",
        background="white" if game.turn == "W" else "black",
        foreground="black" if game.turn == "W" else "white",
    )


# ---------------- SETUP ---------------- #

window = tk.Tk()
window.title("Checkers")
window.geometry("650x650")

main = tk.Frame(window, bg="grey")
main.pack()

lblMove = tk.Label(main, text="White to move", font=("Arial", 12))
lblMove.grid(row=0, column=0, columnspan=8, sticky="we")

board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
game = Board()

for i in range(BOARD_SIZE):
    main.grid_rowconfigure(i + 1, weight=1)
    main.grid_columnconfigure(i, weight=1)

for r in range(BOARD_SIZE):
    for c in range(BOARD_SIZE):
        colour = "white" if (r + c) % 2 == 0 else "black"
        btn = tk.Button(
                            main,
                            width=6,
                            height=3,
                            bg=colour,
                            bd=0,
                            highlightthickness=0,
                            relief="flat"
                        )
        btn.grid(row=r + 1, column=c, sticky="nsew") #allows squares to be flexible
        board[r][c] = btn

        if colour == "black" and (r < 3 or r > 4):
            piece_colour = "W" if r < 3 else "B"
            piece = Piece(r, c, piece_colour)
            game.virBoard[r][c] = piece
            btn.config(
                text="O",
                font=("Consolas", 12, "bold"),
                foreground="white" if piece_colour == "W" else "red",
                bd=0,
                highlightthickness=0,
                relief="flat",
                command=lambda p=piece: move(p),
            )

window.mainloop()

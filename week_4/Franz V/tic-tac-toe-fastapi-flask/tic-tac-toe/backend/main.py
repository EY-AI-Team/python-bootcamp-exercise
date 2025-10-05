# backend/main.py
from typing import List, Optional, Tuple
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="Tic-Tac-Toe AI (Minimax)")

# Allow the Flask UI (different origin) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # For local dev simplicity. Lock down in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diagonals
]

class MoveRequest(BaseModel):
    board: List[str] = Field(..., min_length=9, max_length=9)  # ["X","","O",...]
    ai: str = "O"
    human: str = "X"


def get_winner(board: List[str]) -> Optional[str]:
    for a, b, c in WIN_COMBOS:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board: List[str]) -> bool:
    return all(cell in ("X", "O") for cell in board)


def available_moves(board: List[str]) -> List[int]:
    return [i for i, cell in enumerate(board) if cell not in ("X", "O")]


def minimax_ab(board: List[str], current: str, ai: str, human: str,
               depth: int = 0, alpha: int = -10**9, beta: int = 10**9) -> Tuple[int, Optional[int]]:
    """
    Minimax with alpha-beta pruning.
    Returns (score, move_index) where positive is favorable to the AI.
    Depth is used so the AI prefers faster wins and delays losses.
    """
    winner = get_winner(board)
    if winner == ai:
        return 10 - depth, None
    elif winner == human:
        return depth - 10, None
    elif is_full(board):
        return 0, None

    moves = available_moves(board)

    if current == ai:
        best_score = -10**9
        best_move = None
        for move in moves:
            board[move] = ai
            score, _ = minimax_ab(board, human, ai, human, depth + 1, alpha, beta)
            board[move] = ""
            # Maximize for AI
            if score > best_score or (score == best_score and (best_move is None or move < best_move)):
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # beta cutoff
        return best_score, best_move
    else:
        best_score = 10**9
        best_move = None
        for move in moves:
            board[move] = human
            score, _ = minimax_ab(board, ai, ai, human, depth + 1, alpha, beta)
            board[move] = ""
            # Minimize for Human
            if score < best_score or (score == best_score and (best_move is None or move < best_move)):
                best_score = score
                best_move = move
            beta = min(beta, best_score)
            if beta <= alpha:
                break  # alpha cutoff
        return best_score, best_move


def best_ai_move(board: List[str], ai: str, human: str) -> Optional[int]:
    # Terminal? nothing to do.
    if get_winner(board) or is_full(board):
        return None

    # Opening heuristics are optional; minimax can handle them,
    # but these make the AI snappier on the first turn.
    turn_count = board.count("X") + board.count("O")
    if turn_count == 0:
        return 4  # Take center on the very first move
    if turn_count == 1 and board[4] == "":
        return 4  # If opp didn't take center, take it

    # Decide whose turn it is by parity (X always moves when counts are equal)
    x_count = board.count("X")
    o_count = board.count("O")
    current = "X" if x_count == o_count else "O"
    current = ai if current == ai else human

    # Run alpha-beta minimax
    _, move = minimax_ab(board[:], current, ai, human)
    return move


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/move")
def move(req: MoveRequest):
    board = [cell if cell in ("X", "O") else "" for cell in req.board]
    ai = req.ai
    human = req.human

    current_winner = get_winner(board)
    if current_winner or is_full(board):
        # Terminal state: nothing to play
        return {
            "move": None,
            "board": board,
            "winner": current_winner,
            "draw": (current_winner is None and is_full(board)),
            "next_player": None
        }

    # Compute AI move
    move_index = best_ai_move(board, ai, human)

    if move_index is not None:
        board[move_index] = ai

    # Compute new state
    winner_after = get_winner(board)
    draw_after = (winner_after is None and is_full(board))

    # Next player by parity
    x_count = board.count("X")
    o_count = board.count("O")
    next_player = "X" if x_count == o_count else "O"

    return {
        "move": move_index,
        "board": board,
        "winner": winner_after,
        "draw": draw_after,
        "next_player": next_player
    }

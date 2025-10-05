# Tic-Tac-Toe (FastAPI + Flask UI)

A simple Tic-Tac-Toe with a **FastAPI** backend that runs a **Minimax (alpha–beta)** AI opponent,
and a **Flask** frontend that renders a clickable board.

## Prerequisites
- Python 3.9+
- `pip`

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Run Backend (FastAPI)
```bash
uvicorn backend.main:app --reload --port 8000
```

## Run Frontend (Flask)
Open another terminal in the same project folder:
```bash
python frontend/app.py
```

Now open: http://127.0.0.1:5000

### Point the UI to a different API URL (optional)
If your FastAPI is on a different host/port:
```bash
# Example
export API_URL="https://your-api-host:8000"
python frontend/app.py
```
(Use `set API_URL=...` on Windows PowerShell/Command Prompt.)

## API
- `GET /health` → `{ "status": "ok" }`
- `POST /move` → body:
  ```json
  { "board": ["X","","","O","","", "", "", ""], "ai":"O", "human":"X" }
  ```
  Response:
  ```json
  { "move": 4, "board": ["X","","","O","O","", "", "", ""], "winner": null, "draw": false, "next_player": "X" }
  ```

## Notes
- The AI uses **Minimax with alpha–beta pruning**, scoring **+10 − depth** for AI wins, **−10 + depth** for human wins, and **0** for draws.
- The UI automatically calls the backend whenever it's the AI's turn.
- No database; state is held on the client (browser) and sent with each request.

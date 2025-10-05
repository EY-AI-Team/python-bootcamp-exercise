// frontend/static/app.js
const API_URL = document.getElementById("config").dataset.apiUrl;
const boardEl = document.getElementById("board");
const statusEl = document.getElementById("status");
const humanMarkSelect = document.getElementById("humanMark");
const resetBtn = document.getElementById("resetBtn");

let board = Array(9).fill("");
let human = "X";
let ai = "O";
let gameOver = false;

function renderBoard() {
  boardEl.innerHTML = "";
  board.forEach((mark, idx) => {
    const cell = document.createElement("button");
    cell.className = "cell";
    cell.textContent = mark;
    cell.addEventListener("click", () => onCellClick(idx));
    if (mark) cell.classList.add("filled");
    if (gameOver) cell.disabled = true;
    boardEl.appendChild(cell);
  });
}

function getWinner(b) {
  const wins = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
  ];
  for (const [a,b2,c] of wins) {
    if (b[a] && b[a] === b[b2] && b[a] === b[c]) return b[a];
  }
  return null;
}

function isFull(b) {
  return b.every(x => x === "X" || x === "O");
}

async function aiMoveIfNeeded() {
  if (gameOver) return;

  const xCount = board.filter(x => x === "X").length;
  const oCount = board.filter(x => x === "O").length;
  const aiTurn = (ai === "X") ? (xCount === oCount) : (xCount > oCount);
  if (!aiTurn) return;

  statusEl.textContent = "AI is thinking...";
  try {
    const res = await fetch(`${API_URL}/move`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ board, ai, human })
    });
    const data = await res.json();
    if (data.move !== null && data.move !== undefined) {
      board = data.board;
    }

    const winner = data.winner;
    if (winner) {
      statusEl.textContent = `Winner: ${winner}`;
      gameOver = true;
    } else if (data.draw) {
      statusEl.textContent = "Draw!";
      gameOver = true;
    } else {
      statusEl.textContent = "Your turn.";
    }
    renderBoard();
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Error contacting AI server. Is FastAPI running?";
  }
}

function onCellClick(idx) {
  if (gameOver) return;
  if (board[idx]) return; // occupied

  // Determine whose turn it is; block if it's AI's turn
  const xCount = board.filter(x => x === "X").length;
  const oCount = board.filter(x => x === "O").length;
  const aiTurn = (ai === "X") ? (xCount === oCount) : (xCount > oCount);
  if (aiTurn) return;

  board[idx] = human;
  renderBoard();

  const winner = getWinner(board);
  if (winner) {
    statusEl.textContent = `Winner: ${winner}`;
    gameOver = true;
    return;
  }
  if (isFull(board)) {
    statusEl.textContent = "Draw!";
    gameOver = true;
    return;
  }

  aiMoveIfNeeded();
}

function resetGame() {
  board = Array(9).fill("");
  gameOver = false;
  human = humanMarkSelect.value;
  ai = (human === "X") ? "O" : "X";
  statusEl.textContent = (human === "X") ? "Your turn." : "AI will start...";
  renderBoard();
  aiMoveIfNeeded(); // If AI goes first, it will move
}

resetBtn.addEventListener("click", resetGame);

humanMarkSelect.addEventListener("change", resetGame);

// Init
resetGame();
renderBoard();

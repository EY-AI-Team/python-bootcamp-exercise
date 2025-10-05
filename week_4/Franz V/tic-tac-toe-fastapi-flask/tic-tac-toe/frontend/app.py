
# frontend/app.py
import os
from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="templates",   # explicit
    static_folder="static"         # explicit
)

# Point to your FastAPI (defaults to local)
app.config["API_URL"] = os.environ.get("API_URL", "http://127.0.0.1:8000")

@app.route("/")
def index():
    return render_template("index.html", api_url=app.config["API_URL"])

if __name__ == "__main__":
    # Change the port to avoid collisions (5050), bind to 127.0.0.1
    app.run(debug=True, host="127.0.0.1", port=5050)

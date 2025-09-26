from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_ENDPOINT = "http://localhost:8000/get_employee"

@app.route("/", methods=["GET", "POST"])
def upload_file():
    result = None
    error = None

    if request.method == "POST":
        file = request.files.get('file')
        if file:
            try:
                response = requests.post(
                    API_ENDPOINT,
                    files={"file": (file.filename, file.stream, file.content_type)}
                )
                if response.status_code == 200:
                    result = response.json()
                else:
                    error = response.text
            except Exception as e:
                error = f"Error contacting API: {e}"

    return render_template("upload.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)

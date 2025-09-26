from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_ENDPOINT = "http://localhost:8000/get_employee"

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files['file']
        if file:
            response = requests.post(
                API_ENDPOINT,
                files={"file": (file.filename, file.stream, file.content_type)}
            )
            print("Status code:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 200:
                try:
                    result = response.json()
                    return render_template("upload.html", result=result)
                except Exception as e:
                    return f"Failed to parse JSON: {e}<br>Response content:<br>{response.text}"
            else:
                return f"Error: {response.text}", response.status_code

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)

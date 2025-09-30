from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    # Run Flask app
    app.run(
        host='0.0.0.0',
        port=5001,
        debug=True
    )

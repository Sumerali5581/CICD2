from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Your Flask app is successfully deployed!"

@app.route("/one")
def one():
    return "Hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

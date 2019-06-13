from flask import Flask, request

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello Flask from Docker!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

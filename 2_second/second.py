from collections import defaultdict

from flask import Flask, request

app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name):
    return "Hello " + name + "!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

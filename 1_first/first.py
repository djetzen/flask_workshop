from flask import Flask, request

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello Flask!"


@app.route("/hello/post", methods=["POST"])
def hello_post():
    return b"The data sent is: "+request.data


if __name__ == "__main__":
    app.run(host="0.0.0.0")

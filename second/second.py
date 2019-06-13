from flask import Flask, request, Response
from flask_api import status

app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name):
    return Response("Hello " + name + "!", status.HTTP_200_OK)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

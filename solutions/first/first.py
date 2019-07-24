from flask import Flask, request, Response
from flask_api import status

app = Flask(__name__)


@app.route("/hello")
def hello():
    return Response("Hello Flask!",status.HTTP_200_OK)


@app.route("/hello/post", methods=["POST"])
def hello_post():
    return Response(b"The data sent is: "+request.data, status.HTTP_200_OK)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

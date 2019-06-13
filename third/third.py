from flask import Flask, request, Blueprint, Response
from flask_api import status

app = Flask(__name__)

greeting = Blueprint("greeting", __name__, url_prefix="/greeting")


@greeting.route("/hello/<name>")
def hello(name):
    return Response("Hello " + name + "!", status.HTTP_200_OK)


@greeting.route("/gday/<name>")
def gday(name):
    return Response("Gday " + name + "!", status.HTTP_200_OK)


@greeting.route("/bonjour/<name>")
def bonjour(name):
    return Response("Bonjour " + name + "!", status.HTTP_200_OK)


if __name__ == "__main__":
    app.register_blueprint(greeting)
    app.run(host="0.0.0.0")

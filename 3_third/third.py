from flask import Flask, request, Blueprint

app = Flask(__name__)

greeting = Blueprint("greeting", __name__, url_prefix="/greeting")


@greeting.route("/hello/<name>")
def hello(name):
    return "Hello " + name + "!"


@greeting.route("/gday/<name>")
def gday(name):
    return "Gday " + name + "!"


@greeting.route("/bonjour/<name>")
def bonjour(name):
    return "Bonjour " + name + "!"


if __name__ == "__main__":
    app.register_blueprint(greeting)
    app.run(host="0.0.0.0")

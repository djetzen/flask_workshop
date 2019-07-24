from flask import Flask, Response, Blueprint
from flask_api import status

app = Flask(__name__)

greeting = Blueprint("greeting", __name__, url_prefix="/greeting")

@greeting.route("/hello")
def hello():
    return Response("Hello Flask!", status.HTTP_200_OK)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

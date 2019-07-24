import flask
from flask_api import status
from solutions.fifth.fifth import greeting

app = flask.Flask(__name__)
app.register_blueprint(greeting)

def test_hello_endpoint_is_available():

    rv = app.test_client().get("greeting/hello")

    assert rv.status_code == status.HTTP_200_OK
    assert rv.data == b"Hello Flask!"
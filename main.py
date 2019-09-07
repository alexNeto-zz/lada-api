import os

from flask import Flask
from flask_cors import CORS

from api.api_setup import global_init
from api.end_points import EndPoints

global_init()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

EndPoints(app).add_resources()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

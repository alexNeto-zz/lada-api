import os

from flask import Flask
from flask_cors import CORS

from api.end_points import EndPoints
from api.api_setup import global_init

global_init()

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "https://lada-app.com"}})

EndPoints(app).add_resources()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

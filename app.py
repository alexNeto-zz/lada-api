import os

from flask import Flask
from flask_cors import CORS

from api.today_resume.today_resume import today_resume_blueprint

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(today_resume_blueprint, url_prefix="/today_resume")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



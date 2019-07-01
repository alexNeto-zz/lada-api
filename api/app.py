from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

from api.today_resume.today_resume import today_resume_blueprint

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ladaDatabase"
mongo = PyMongo(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(today_resume_blueprint, url_prefix="/today_resume")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

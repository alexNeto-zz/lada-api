import os

from flask import Flask
from flask_cors import CORS

from api.end_points import EndPoints
from api.storage.mongo_setup import global_init
from api.today_resume.today_resume import today_resume_blueprint

global_init()
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(today_resume_blueprint, url_prefix="/today_resume")
EndPoints(app).add_resources()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

from flask import Blueprint

from api.today_resume.today_resume_model import TodayResumeModel

today_resume_blueprint = Blueprint('today_resume', __name__)


@today_resume_blueprint.route("/list/<string:x>/<string:y>")
def today_resume(x, y):
    return TodayResumeModel(x, y).get_today_resume_list()

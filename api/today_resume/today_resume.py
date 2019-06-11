from flask import Blueprint

today_resume_blueprint = Blueprint('today_resume', __name__)


@today_resume_blueprint.route("/list/<float:x>/<float:y>")
def today_resume(x, y):
    return 'reloi'

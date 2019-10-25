from flask_restful import Resource
from werkzeug.utils import redirect


class IndexController(Resource):

    @classmethod
    def get(cls):
        return redirect("https://lada-app.com", code=302)

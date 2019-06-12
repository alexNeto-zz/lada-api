from flask import Blueprint

from api.sources.cptec.cptec_model import CptecModel

cptec_blueprint = Blueprint(r'cptec', __name__)


@cptec_blueprint.route("/today_resume/<string:x>/<string:y>")
def today_resume(latitude, longitude):
    return CptecModel(latitude, longitude).make_request().get_today_resume()


@cptec_blueprint.route("/today_complete/<string:state>/<string:city>")
def today_complete(country, state, city):
    return CptecModel(country, state, city).make_request().get_today_complete()


@cptec_blueprint.route("/week_resume/<string:country>/<string:state>/<string:city>")
def week_resume(country, state, city):
    return CptecModel(country, state, city).make_request().get_week_resume()


@cptec_blueprint.route("/week_complete/<string:country>/<string:state>/<string:city>")
def week_complete(country, state, city):
    return CptecModel(country, state, city).make_request().get_week_complete()

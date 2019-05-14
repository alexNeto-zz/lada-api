from flask import Blueprint

from sources.cptec.cptec_model import CPTECModel

test_blueprint = Blueprint('test', __name__)


@test_blueprint.route("/today_resume/<string:country>/<string:state>/<string:city>")
def today_resume(country, state, city):
    return CPTECModel(country, state, city).make_request().get_today_resume()


@test_blueprint.route("/today_complete/<string:country>/<string:state>/<string:city>")
def today_complete(country, state, city):
    return CPTECModel(country, state, city).make_request().get_today_complete()


@test_blueprint.route("/week_resume/<string:country>/<string:state>/<string:city>")
def week_resume(country, state, city):
    return CPTECModel(country, state, city).make_request().get_week_resume()


@test_blueprint.route("/week_complete/<string:country>/<string:state>/<string:city>")
def week_complete(country, state, city):
    return CPTECModel(country, state, city).make_request().get_week_complete()

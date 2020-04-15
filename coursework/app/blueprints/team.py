from flask import Blueprint, abort, jsonify, json, make_response
from flask import request
from storage import teams_dict
from flask_cors import CORS, cross_origin

from models.team import Team
from models.team_decorator import IterableTeamDecorator

team_blueprint = Blueprint('team_api', __name__, )


@team_blueprint.route('/api/team', methods=['POST'])
@cross_origin()
def show():
    print(request)
    if not request.json:
        abort(400)

    req_body = request.json
    if req_body["teamName"] in teams_dict:
        return make_response(jsonify({"err": "name exists"}), 400)

    teams_dict[req_body["teamName"]] = Team()
    return make_response(jsonify([key for key in teams_dict.keys()]), 200)


@team_blueprint.route('/api/team', methods=['GET'])
@cross_origin()
def get_teams():
    return make_response(jsonify([key for key in teams_dict.keys()]), 201)


@team_blueprint.route('/api/team/<string:team_name>', methods=['GET'])
@cross_origin()
def show_team(team_name):
    print(request)

    if team_name not in teams_dict:
        return make_response(jsonify({"err" : "no such a team"}), 400)

    respose_list = []

    for worker in IterableTeamDecorator(teams_dict[team_name]).faster_workers_iterator():
        respose_list.append({
            "workerName" : worker.name,
            "hoursLeft" : worker.hours_left,
            "position" : worker.position
        })
    return make_response(jsonify(respose_list), 200)

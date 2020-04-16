from flask import Blueprint, abort, jsonify, json, make_response
from flask import request
from storage import teams_dict
from flask_cors import CORS, cross_origin

from models.team import Team
from models.team_decorator import IterableTeamDecorator

team_blueprint = Blueprint('team_api', __name__, )


@team_blueprint.route('/api/team', methods=['POST'])
@cross_origin()
def create_team():
    if not request.json:
        abort(400)

    req_body = request.json
    if req_body["teamName"] in teams_dict:
        return make_response(jsonify({"err": "name exists"}), 400)

    teams_dict[req_body["teamName"]] = Team()
    return make_response(jsonify([key for key in teams_dict.keys()]), 201)


@team_blueprint.route('/api/team', methods=['GET'])
@cross_origin()
def get_teams():
    resp_list = []
    for team_name in teams_dict.keys():
        tmp_team = teams_dict[team_name]
        tmp_resp_body = {
            "teamName": team_name,
            "workersCount": tmp_team.workers_count
        }
        resp_list.append(tmp_resp_body)

    return make_response(jsonify(resp_list), 200)


@team_blueprint.route('/api/team/<string:team_name>', methods=['GET'])
@cross_origin()
def show_team(team_name):
    if team_name not in teams_dict:
        return make_response(jsonify({"err": "no such a team"}), 400)

    respose_list = []

    for worker in IterableTeamDecorator(teams_dict[team_name]).faster_workers_iterator():
        respose_list.append({
            "workerName": worker.name,
            "hoursLeft": worker.hours_left,
            "position": worker.position,
            "experience": worker.experience
        })
    return make_response(jsonify(respose_list), 200)


@team_blueprint.route('/api/team/<string:team_name>', methods=['DELETE'])
@cross_origin()
def delete_team(team_name):
    if team_name not in teams_dict:
        abort(400)
    del teams_dict[team_name]
    return make_response("", 200)


@team_blueprint.route('/api/team/refreshTeam/<string:team_name>', methods=['POST'])
@cross_origin()
def refresh_team(team_name):
    if team_name not in teams_dict:
        return make_response(jsonify({"err": f'no team {team_name}'}), 400)

    teams_dict[team_name].refresh_workers()
    return make_response("", 200)

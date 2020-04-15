from flask import Blueprint, abort, jsonify, json, make_response
from flask import request
from storage import teams_dict
from flask_cors import CORS, cross_origin

from models.team import Team
from models.worker_fabric import WorkerCreator, JuniorWorkerCreator, MiddleWorkerCreator, SeniorWorkerCreator

worker_blueprint = Blueprint('worker_api', __name__, )


@worker_blueprint.route('/api/worker', methods=['POST'])
@cross_origin()
def create_worker():
    req_body = request.json
    print(req_body)
    team_name = req_body["teamName"]
    print(teams_dict)
    if team_name not in teams_dict:
        return make_response(jsonify({"err": "no team"}), 400)

    worker_fabric = None
    worker_position = req_body["workerPosition"].lower()

    if worker_position == "junior":
        worker_fabric = JuniorWorkerCreator
    elif worker_position == "middle":
        worker_fabric = MiddleWorkerCreator
    elif worker_position == "senior":
        worker_fabric = SeniorWorkerCreator
    else:
        print("compare Error")
        return make_response(jsonify({"err": "wrong position field"}), 400)

    print(worker_fabric)
    new_worker = worker_fabric.create_worker(req_body["workerName"], "-")
    teams_dict[team_name].add(worker_position, new_worker)

    return make_response(jsonify(""), 201)


from flask import Blueprint, abort, jsonify, json, make_response
from flask import request
from storage import teams_dict, tasks_dict
from flask_cors import cross_origin

from models.task_builder import AccessTaskBuilder
from models.team_decorator import IterableTeamDecorator

task_blueprint = Blueprint('task_api', __name__, )


@task_blueprint.route('/api/task', methods=['GET'])
@cross_origin()
def get_tasks():
    return_list = []

    for task_name in tasks_dict:
        tmp_task = tasks_dict[task_name]
        est_dict = tmp_task.estimate_list

        ret_obj = {
            "taskName": task_name,
            "juniorEst": est_dict["junior"],
            "middleEst": est_dict["middle"],
            "seniorEst": est_dict["senior"],
            "accessLevel": tmp_task.access_level[0]
        }
        return_list.append(ret_obj)
    return make_response(jsonify(return_list), 200)


@task_blueprint.route('/api/task', methods=['POST'])
@cross_origin()
def create_task():
    if not request.json:
        abort(400)

    req_body = request.json
    print(req_body)
    task_builder = AccessTaskBuilder()
    task_name = req_body["taskName"]

    if task_name in tasks_dict:
        return make_response(jsonify({"err": "name is already defined"}), 400)

    task_builder.set_junior_est(req_body["juniorEst"])
    task_builder.set_middle_est(req_body["middleEst"])
    task_builder.set_senior_est(req_body["seniorEst"])

    task_builder.set_access_level(req_body["accessLevel"])

    tmp_task = task_builder.built_task
    tasks_dict[task_name] = tmp_task

    return make_response("", 201)


@task_blueprint.route('/api/task/<string:task_name>', methods=['DELETE'])
@cross_origin()
def delete_task(task_name):
    print("deleting task" + " " + task_name)
    if task_name not in tasks_dict:
        abort(400)

    del tasks_dict[task_name]
    return make_response("", 200)

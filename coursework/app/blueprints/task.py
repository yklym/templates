from flask import Blueprint, abort, jsonify, json, make_response
from flask import request
from flask_cors import cross_origin

from storage import teams_dict, tasks_dict
from models.task_resolver import TaskResolver
from models.task_builder import AccessTaskBuilder

task_resolver = TaskResolver()

task_blueprint = Blueprint('task_api', __name__, )


@task_blueprint.route('/api/task', methods=['GET'])
@cross_origin()
def get_tasks():
    return_list = []

    for task_name in tasks_dict:
        tmp_task = tasks_dict[task_name]
        est_dict = tmp_task.estimate_list
        print(tmp_task.changes_log)
        ret_obj = {
            "taskName": task_name,
            "juniorEst": est_dict["junior"],
            "middleEst": est_dict["middle"],
            "seniorEst": est_dict["senior"],
            "accessLevel": tmp_task.access_level[0],
            "log": "\n".join(tmp_task.changes_log)
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
    if task_name not in tasks_dict:
        abort(400)

    del tasks_dict[task_name]
    return make_response("", 200)


@task_blueprint.route('/api/resolveTask/<string:task_name>', methods=['POST'])
@cross_origin()
def resolve_task(task_name):
    if (task_name not in tasks_dict) or (not request.json):
        abort(400)

    request_body = request.json

    response_obj = task_resolver.resolve(tasks_dict[task_name],
                                         teams_dict[request_body["team"]],
                                         request_body["mode"])

    if response_obj["err"]:
        print(response_obj)
        return make_response(jsonify(response_obj), 200)  # status 204 - NO CONTENT
    else:
        log = "\n".join(tasks_dict[task_name].changes_log)
        del tasks_dict[task_name]
        return make_response(jsonify({"log": log}), 200)

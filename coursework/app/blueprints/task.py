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
        ret_obj = {
            "taskName": task_name,
            "juniorEst": tmp_task.estimate_list["junior"],
            "middleEst": tmp_task.estimate_list["middle"],
            "seniorEst": tmp_task.estimate_list["senior"],
            "accessLevel": tmp_task.access_level[-1]
        }
        return_list.append(ret_obj)

    return make_response(jsonify(return_list), 200)

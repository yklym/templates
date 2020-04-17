from models.team import Team
from models.task_builder import AccessTaskBuilder
from models.worker_fabric import *
from models.task_resolver import TaskResolver
from models.team_decorator import IterableTeamDecorator

task_resolver = TaskResolver()
# from models.task_resolver import TaskResolver
# task_resolver = TaskResolver()

task_builder = AccessTaskBuilder()
task_builder.set_junior_est(5)
task_builder.set_middle_est(4)
task_builder.set_senior_est(3)
task_builder.set_access_level("junior")
task1 = task_builder.built_task

# task_builder.built_task
jun = JuniorWorkerCreator.create_worker("junname")
mid = MiddleWorkerCreator.create_worker("midNam")
sen = SeniorWorkerCreator.create_worker("senName")

team1 = Team()

team1.add("junior", jun)
team1.add("middle", mid)
team1.add("senior", sen)

task_builder.set_junior_est(5)
task_builder.set_middle_est(4)
task_builder.set_senior_est(3)
task_builder.set_access_level("junior")
task2 = task_builder.built_task

teams_dict = dict({"test": team1})

tasks_dict = dict({"test": task1, "test2": task2})

# response_obj = task_resolver.resolve(task1, team1, "favourite")

# print(task1.changes_log)
# print(task1.estimate_list)
# print(response_obj)
# for worker in IterableTeamDecorator(team1):
#     print(worker.hours_left)

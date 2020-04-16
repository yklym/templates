from models.team import Team
from models.task_builder import AccessTaskBuilder

task_builder = AccessTaskBuilder()
task_builder.set_junior_est(5)
task_builder.set_middle_est(4)
task_builder.set_senior_est(3)
task_builder.set_access_level("junior")

# task_builder.built_task

teams_dict = dict({"test": Team()})

tasks_dict = dict({"test": task_builder.built_task})



# class Team:
#     _team_counter = 0
#
#     def __init__(self):
#         self._name = f'team {Team._team_counter}'
#         Team._team_counter += 1
#         self._workers = {"junior": [], "middle": [], "senior": []}
#
#     @property
#     def workers(self):
#         return self._workers
#

class Team:

    def __init__(self):
        self.workers = {"junior": [], "middle": [], "senior": []}

    def add(self, position, worker):
        self.workers[position].append(worker)



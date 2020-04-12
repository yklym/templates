class Team:

    def __init__(self):
        self._workers = {"junior": [], "middle": [], "senior": []}

    @property
    def workers(self):
        return self._workers

    def add(self, position, worker):
        self._workers[position].append(worker)

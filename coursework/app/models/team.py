class Team:

    def __init__(self):
        self._workers = {"junior": [], "middle": [], "senior": []}

    @property
    def workers_count(self):
        return len(self._workers["junior"]) + len(self._workers["middle"]) + len(self._workers["senior"])

    @property
    def workers(self):
        return self._workers

    def add(self, position, worker):
        self._workers[position].append(worker)

    def delete_worker(self, name, position):
        # Filter list from deleted element
        self._workers[position] = list(filter(lambda worker: worker.name != name, self._workers[position]))

    def refresh_workers(self):

        for position in self._workers:
            for worker in self._workers[position]:
                worker.refresh()
from models.task import Task
from models.custom_exceptions import WorkerResolvingTaskException


class Proxy(Task):

    def __init__(self, real_subject: Task):
        self._real_subject = real_subject

    # incapsulating method
    def set_access_level(self, access_level):
        pass

    @property
    def access_level(self):
        return self._real_subject.access_level

    @property
    def estimate_list(self):
        return self._real_subject.estimate_list

    def add_estimate(self, key, value) -> None:
        self._real_subject.add_estimate(key, value)


class LoggerProxy(Proxy):
    _history = []

    def add_estimate(self, key, value, worker):
        self._history.append(f"Worker {worker.name} set [{key}] task to [{value}]")
        self._real_subject.add_stimate(key, value)

    @property
    def changes_log(self):
        return self._history


class WorkerAccessProxy(Proxy):
    @property
    def add_estimate(self, key, value, worker):
        if worker.access_level not in self._real_subject.access_level:
            raise WorkerResolvingTaskException
        return self._real_subject.add_estimate(key, value)

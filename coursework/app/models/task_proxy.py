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
    def __init__(self, real_subject: Task):
        self._history = []
        super().__init__(real_subject)

    def add_estimate(self, key, value, worker):
        if not worker:
            print("It's not a worker")
            # self._real_subject.add_estimate(key, value)
        else:
            self._history.append(f"Worker {worker.name} set [{key}] estimate to [{value}]")
            self._real_subject.add_estimate(key, value)

    @property
    def changes_log(self):
        return self._history


class WorkerAccessProxy(Proxy):
    def add_estimate(self, key, value, worker):

        if not worker or worker.access_level not in self._real_subject.access_level:
            print("access denied")
            raise WorkerResolvingTaskException
        print("access granted")
        if value == -1:
            print("Just a check")
            return True
        return self._real_subject.add_estimate(key, value, worker)

    @property
    def changes_log(self):
        if self._real_subject.changes_log:
            return self._real_subject.changes_log
        else:
            return " "

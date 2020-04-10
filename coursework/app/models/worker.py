from abc import ABC, abstractmethod
from models.custom_exceptions import *


class Worker(ABC):
    _experience = 0
    _salary = 0
    _hours_left = 8
    _efficiency = 1

    def __init__(self, name: str, photo: str):
        self.name = name
        self.photo = photo

    @property
    def _hours_left(self):
        return self._hours_left

    @_hours_left.setter
    def _hours_left(self, val):

        if self._hours_left - val < 0:
            self._hours_left = 0
            #  CHANGE STATE
            raise WorkerHasNoTimeException("Hours_left setter")

        self._hours_left = self._hours_left - val

    def resolve_task(self, task):
        self._resolve_junior_part(task)  # req op
        self._debugging(1)  # Hook
        self._resolve_middle_part(task)  # req op
        self._debugging(2)  # Hook
        self._resolve_senior_part(task)  # req op
        self._debugging(3)  # Hook
        self._rest()  # base operation

    def _rest(self):
        # base operation
        self._hours_left -= 1

    def _debugging(self, hours):
        # hook
        try:
            self._hours_left -= hours
        except WorkerHasNoTimeException:
            # actually nothing at all
            pass

    def _resolver(self, task, est_type, efficiency_koef: "<1 for more efficient" = 1):
        est_done = 0
        req_est = task.estimate_list[est_type]
        try:
            self._hours_left -= req_est * efficiency_koef
            est_done = req_est

        except WorkerHasNoTimeException:
            est_done = self._hours_left / efficiency_koef
            self._hours_left = 0
            raise WorkerHasNoTimeException
        finally:
            task.add_estimate(est_type, req_est - est_done)

    def _resolve_junior_part(self, task):
        self._resolver(task, "junior")

    def _resolve_middle_part(self, task):
        self._resolver(task, "middle")

    def _resolve_senior_part(self, task):
        self._resolver(task, "senior")


class JuniorWorker(Worker):
    """
    _debugging hook is not overwritten
    `cause we there is a price
    for stack overflow
    """

    def __init__(self, name, photo):
        self._hours_left = 10
        self._salary = 3
        super().__init__(name, photo)

    def _resolve_middle_part(self, task):
        self._resolver(task, "middle", 1.5)

    def _resolve_senior_part(self, task):
        self._resolver(task, "senior", 2)


class MiddleWorker(Worker):
    """
    Middle worker overrides hook of debugging
    and some req parts of template method
    """

    def __init__(self, name, photo):
        self._salary = 5
        super().__init__(name, photo)

    def _resolve_senior_part(self, task):
        self._resolver(task, "senior", 2)

    def _debugging(self, hours):
        if hours >= 2:
            hours -= 1
        else:
            hours = 0
        super()._debugging(hours)

    def _resolve_senior_part(self, task):
        self._resolver(task, "senior", 1.25)


class SeniorWorker(Worker):
    def __init__(self, name, photo):
        self._salary = 7
        super().__init__(name, photo)

    def _debugging(self, hours):
        if hours >= 2:
            hours -= 2
        else:
            hours = 0
        super()._debugging(hours)

    def _resolve_middle_part(self, task):
        self._resolver(task, "middle", 0.75)

    def _resolve_senior_part(self, task):
        self._resolver(task, "senior", 0.5)


class WorkerCreator(ABC):
    @abstractmethod
    def create_worker(self):
        pass


class JuniorWorkerCreator(WorkerCreator):
    @staticmethod
    def create_worker(self, name, photo) -> JuniorWorker:
        return JuniorWorker(name, photo)


class MiddleWorkerCreator(WorkerCreator):
    @staticmethod
    def create_worker(name, photo) -> MiddleWorker:
        return MiddleWorker(name, photo)


class SeniorWorkerCreator(WorkerCreator):
    @staticmethod
    def create_worker(self, name, photo) -> SeniorWorker:
        return SeniorWorker(name, photo)

# Obdumoi, yarek. Ty shze hochesh sozdat tyanochku?
# Opredielionno hochu
# class Recruiter:
#     def __init__(self, name):

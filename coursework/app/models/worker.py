from abc import ABC

from models.custom_exceptions import *

"""
To understand the code, you should go first to "task_resolver.py" gl hf
"""


class Worker(ABC):
    """
    there are abstract workers with something in common
    """
    _experience = 0
    _hours_amount = 8
    _access_level = ""

    def __init__(self, name: str):
        self.name = name
        self._hours_left = self._hours_amount

    @property
    def hours_left(self):
        return self._hours_left

    @property
    def experience(self):
        return self._experience

    @property
    def access_level(self):
        return self._access_level

    def refresh(self):
        self._hours_left = self._hours_amount

    def _reduce_hours_left(self, val):

        if self._hours_left - val < 0:
            raise WorkerHasNoTimeException("Hours_left setter")
        self._experience += val
        self._hours_left -= val

    def resolve_task(self, task):
        print("-----------------------")
        print("Resolving task ", self)
        self._resolve_junior_part(task)  # req op
        self._debugging(1)  # Hook
        print(f"Hours left {self.hours_left}")
        self._resolve_middle_part(task)  # req op
        self._debugging(2)  # Hook
        print(f"Hours left {self.hours_left}")
        self._resolve_senior_part(task)  # req op
        self._debugging(3)  # Hook
        print(f"Hours left {self.hours_left}")
        self._rest()  # base operation

    def _rest(self):
        # base operation
        if self._hours_left <= 1:
            self._hours_left -= 0
        else:
            self._hours_left -= 1

    def _debugging(self, hours):
        # hook
        try:
            self._reduce_hours_left(hours)
        except WorkerHasNoTimeException:
            # actually nothing at all
            pass

    def _resolver(self, task, est_type, efficiency_koef: "<1 for more efficient" = 1.0):
        est_done = 0
        # Check Access if no access raises error to handle
        task.add_estimate(est_type, -1, self)

        req_est = task.estimate_list[est_type]
        if not req_est:
            return

        print(f"Required estimate {req_est} [{est_type}]")
        try:

            self._reduce_hours_left(req_est * efficiency_koef)
            est_done = req_est

        except WorkerHasNoTimeException:
            print("can't handle resolving")
            est_done = self._hours_left / efficiency_koef
            self._reduce_hours_left(self._hours_left)
            raise WorkerHasNoTimeException
        finally:
            print(f"Estimate done: {est_done}")
            task.add_estimate(est_type, req_est - est_done, self)

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
    _access_level = "junior"
    _hours_amount = 10

    def _resolve_middle_part(self, task):
        self._resolver(task, "middle", 1.5)

    def _resolve_senior_part(self, task):
        self._resolver(task, "senior", 2)

    @property
    def position(self):
        return "junior"


class MiddleWorker(Worker):
    """
    Middle worker overrides hook of debugging
    and some req parts of template method
    """
    _access_level = "middle"
    _hours_amount = 8

    def _debugging(self, hours):
        if hours >= 2:
            hours -= 1
        else:
            hours = 0
        super()._debugging(hours)

    def _resolve_senior_part(self, task):
        self._resolver(task, "senior", 1.5)

    @property
    def position(self):
        return "middle"


class SeniorWorker(Worker):
    _access_level = "senior"
    _hours_amount = 6

    def _debugging(self, hours):
        if hours >= 2:
            hours -= 2
        else:
            hours = 0
        super()._debugging(hours)

    def _resolve_middle_part(self, task):
        self._resolver(task, "middle", 0.75)

    def _resolve_junior_part(self, task):
        self._resolver(task, "junior", 0.5)

    @property
    def position(self):
        return "senior"
#

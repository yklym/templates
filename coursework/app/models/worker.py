from abc import ABC, abstractmethod
from custom_exceptions import *

class Worker(ABC):
    _experience = 0
    _salary = 0
    _hours_left = 8
    _efficiency = 1

    def __init__(self, name: str, photo: str):
        self.name = name
        self.photo = photo

    @abstractmethod
    def operation(self) -> str:
        pass
    @property
    def _hours_left(self):
        return self._hours_left
    @_hours_left.setter
    def _hours_left(self):


    def resolve_task(self, task):
        self._resolve_junior_part(task)  # base op
        self._debugging(1)  # Hook
        self._resolve_middle_part(task)  # base op
        self._debugging(2)  # Hook
        self._resolve_senior_part(task) # base op
        self._debugging(3)  # Hook
        self._rest() # base operation

        def _rest(self):
            self._hours_left -= 1



class JuniorWorker(Worker):
    def __init__(self, name, photo):
        self._hours_left = 10
        self._salary = 3
        super().__init__(name, photo)

    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class MiddleWorker(Worker):
    def __init__(self, name, photo):
        self._salary = 5
        super().__init__(name, photo)

    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


class SeniorWorker(Worker):
    def __init__(self, name, photo):
        self._salary = 7
        super().__init__(name, photo)

    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


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
# class Recruiter:
#     def __init__(self, name):

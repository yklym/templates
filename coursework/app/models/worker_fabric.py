from abc import ABC

from models.worker import JuniorWorker, MiddleWorker, SeniorWorker


class WorkerCreator(ABC):
    @staticmethod
    def create_worker(name):
        pass


class JuniorWorkerCreator(WorkerCreator):
    @staticmethod
    def create_worker(name) -> JuniorWorker:
        return JuniorWorker(name)


class MiddleWorkerCreator(WorkerCreator):
    @staticmethod
    def create_worker(name) -> MiddleWorker:
        return MiddleWorker(name)


class SeniorWorkerCreator(WorkerCreator):
    @staticmethod
    def create_worker(name) -> SeniorWorker:
        return SeniorWorker(name)
# OR

class WorkersFabric:
    def create_junior(self, name):
        return JuniorWorker(name)


# Obdumoi, yarek. Ty shze hochesh sozdat tyanochku?
# class Recruiter:
#     def __init__(self, name):

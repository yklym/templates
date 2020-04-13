from abc import ABC

from models.worker import JuniorWorker, MiddleWorker, SeniorWorker


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

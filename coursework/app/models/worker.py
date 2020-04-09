from abc import ABC, abstractmethod


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




# def client_code(creator: Worker) -> None:
#     """
#     Клиентский код работает с экземпляром конкретного создателя, хотя и через
#     его базовый интерфейс. Пока клиент продолжает работать с создателем через
#     базовый интерфейс, вы можете передать ему любой подкласс создателя.
#     """
#
#     print(f"Client: I'm not aware of the creator's class, but it still works.\n"
#           f"{creator.some_operation()}", end="")
#
#
# if __name__ == "__main__":
#     print("App: Launched with the ConcreteCreator1.")
#     client_code(ConcreteCreator1())
#     print("\n")
#
#     print("App: Launched with the ConcreteCreator2.")
#     client_code(ConcreteCreator2())

from abc import ABC, abstractmethod

from models.custom_exceptions import WorkerResolvingTaskException, CantBeResolvedByTeamException


class Command(ABC):
    @abstractmethod
    def execute(self, task) -> None:
        pass


class ChainedCommand(Command):
    def __init__(self, receiver) -> None:
        self._receiver = receiver
        self._next_handler = None

    def set_next(self, next_handler):
        self._next_handler = next_handler
        return next_handler

    def execute(self, task) -> None:
        try:
            self._receiver.resolve_task(task)
        except WorkerResolvingTaskException:
            if self._next_handler:
                print(task.estimate_list)
                self._next_handler.execute(task)
            else:
                raise CantBeResolvedByTeamException(f'in ChainedCommand with worker {self._receiver.name}')

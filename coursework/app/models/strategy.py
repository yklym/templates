from abc import ABC, abstractmethod
from typing import List

from models.custom_exceptions import *
from models.team_decorator import IterableTeamDecorator


class Strategy(ABC):

    def __init__(self, team):
        self._team = IterableTeamDecorator(team)
        self._employers_list = []

    # this method is similar to all the classes
    def resolve_task(self, task):
        self._find_employees(task)
        first_command = None
        prev_command = None
        # Links all the commands into responsibility chain
        for employer in self._employers_list:
            new_command = ChainedCommand(employer)
            if prev_command:
                prev_command.set_next(new_command)
            else:
                first_command = new_command
            prev_command = new_command

        first_command.execute(task)

    @abstractmethod
    def _find_employees(self):
        pass


class CheapStrategy(Strategy):
    def _find_employees(self) -> List:
        self._employers_list
        # Using iterator
        for employee in self._team.cheaper_workers_iterator():
            self._employers_list.append(employee)


class OptimalStrategy(Strategy):
    def _find_employees(self) -> List:
        for employee in self._team.optimal_workers_iterator():
            self._employers_list.append(employee)


class FastStrategy(Strategy):
    def _find_employees(self) -> List:
        for employee in self._team.faster_workers_iterator():
            self._employers_list.append(employee)


class EvenStrategy(Strategy):
    def _find_employees(self):
        for employee in self._team.tired_workers_iterator():
            self._employers_list.append(employee)


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
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
                self._next_handler.execute(task)
            else:
                raise CantBeResolvedByTeamException(f'in ChainedCommand with worker {self._receiver.name}')

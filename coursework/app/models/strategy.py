from abc import ABC, abstractmethod
from typing import List

from models.custom_exceptions import *


class Strategy(ABC):

    def __init__(self, team):
        self._team = team
        self._employers_list = []

    # this method is similar to all the classes
    def resolve_task(self, task):
        self._find_employers(task)
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


class CheapStrategy(Strategy):
    def _find_employers(self) -> List:
        # Some algo of returning employers
        pass


class OptimalStrategy(Strategy):
    def _find_employers(self) -> List:
        # Some algo of returning employers
        pass


class FastStrategy(Strategy):
    def _find_employers(self) -> List:
        # Some algo of returning employers
        pass


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
        except WorkerHasNoTimeException:
            if self._next_handler:
                self._next_handler.execute(task)
            else:
                raise CantBeResolvedByTeamException(f'in ChainedCommand with worker {self._receiver.name}')

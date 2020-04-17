from abc import ABC, abstractmethod
from typing import List

from models.command import ChainedCommand
from models.team_decorator import IterableTeamDecorator


class Strategy(ABC):

    def __init__(self, team):
        print("Created Strategy")
        self._team = IterableTeamDecorator(team)
        self._employers_list = []

    # this method is the same in all the classes
    def resolve_task(self, task):
        try:
            self._find_employees()
        except Exception:
            print("find employees exception")
        print("STRATEGY-----------")
        print(self._employers_list)
        first_command = None
        prev_command = None
        # Links all the commands into responsibility chain
        for employer in self._employers_list:
            print(employer.name)
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


class TiredWorkersStrategy(Strategy):
    def _find_employees(self):
        for employee in self._team.tired_workers_iterator():
            self._employers_list.append(employee)


class FavouriteStrategy(Strategy):
    def _find_employees(self):
        for employee in self._team.more_experienced_workers_iterator():
            self._employers_list.append(employee)


class EqualityStrategy(Strategy):
    def _find_employees(self):
        for employee in self._team.less_experienced_workers_iterator():
            self._employers_list.append(employee)



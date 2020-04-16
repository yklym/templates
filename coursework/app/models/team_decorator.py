from abc import ABC
from collections.abc import Iterable

from models.team_iterators import OptimalWorkersIterator, FasterWorkersIterator, CheaperWorkersIterator, \
    ExperiencedWorkersIterator


class TeamDecorator(ABC, Iterable):
    """
    Abstract decorator is created for easier creating of different decorators in future
    """

    def __init__(self, team):
        self._team = team

    @property
    def workers(self):
        return self._team.workers

    def add(self, position, worker):
        self._team.add(position, worker)


class IterableTeamDecorator(TeamDecorator):
    """
    DECORATOR

    We use this decorator to avoid adding too much code to the base
    class, so that we extend it with a decorator. As a plus, we also know
    that code we are hiding will be used only in one specific place. That means that
    we can briefly wrap basic class to provide client code with required functionality
    and don't use these methods without need
    """

    # Standard python way to provide non-iterable class with a decorator
    def optimal_workers_iterator(self):
        return OptimalWorkersIterator(self._team.workers)

    def tired_workers_iterator(self):
        return OptimalWorkersIterator(self._team.workers, reverse=False)

    def faster_workers_iterator(self):
        return FasterWorkersIterator(self._team.workers)

    def cheaper_workers_iterator(self):
        return CheaperWorkersIterator(self._team.workers)

    def more_experienced_workers_iterator(self):
        return ExperiencedWorkersIterator(self._team.workers)

    def less_experienced_workers_iterator(self):
        return ExperiencedWorkersIterator(self._team.workers, reverse=True)

    # Default iterator for iterable classes or ones inherited from standard "Iterable" class
    def __iter__(self):
        return OptimalWorkersIterator(self._team.workers)

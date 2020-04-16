from __future__ import annotations

from collections.abc import Iterator

"""
    ITERATOR
    
    Iterators can't influence important code. They only allow us
    to work with collection's data in proper order. Even though 
    the class, we created iterator for, isn't a collection at all    
"""


class AbstractWorkersIterator(Iterator):
    _position: int = None
    """
    Abstract iterator. 
    we don't need a constructor as far as all the inherited classes override it.
    """

    def __next__(self):
        try:
            value = self._employers_list[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()
        return value


class FasterWorkersIterator(AbstractWorkersIterator):

    def __init__(self, team_collection):
        self._employers_list = []
        if isinstance(team_collection["senior"], list):
            self._employers_list.extend(team_collection["senior"])
        if isinstance(team_collection["middle"], list):
            self._employers_list.extend(team_collection["middle"])
        if isinstance(team_collection["junior"], list):
            self._employers_list.extend(team_collection["junior"])

        self._position = 0


class CheaperWorkersIterator(AbstractWorkersIterator):

    def __init__(self, team_collection):
        self._employers_list = []
        if isinstance(team_collection["junior"], list):
            self._employers_list.extend(team_collection["junior"])
        if isinstance(team_collection["middle"], list):
            self._employers_list.extend(team_collection["middle"])
        if isinstance(team_collection["senior"], list):
            self._employers_list.extend(team_collection["senior"])

        self._position = 0


class OptimalWorkersIterator(AbstractWorkersIterator):

    def __init__(self, team_collection, reverse=False):
        self._employers_list = []
        juniors_list = team_collection["junior"]
        middles_list = team_collection["middle"]
        seniors_list = team_collection["senior"]

        if isinstance(juniors_list, list):
            juniors_list.sort(key=lambda worker: worker.hours_left, reverse=reverse)
            self._employers_list.extend(juniors_list)

        if isinstance(middles_list, list):
            middles_list.sort(key=lambda worker: worker.hours_left, reverse=reverse)
            self._employers_list.extend(middles_list)

        if isinstance(seniors_list, list):
            seniors_list.sort(key=lambda worker: worker.hours_left, reverse=reverse)
            self._employers_list.extend(seniors_list)

        self._position = 0


class ExperiencedWorkersIterator(AbstractWorkersIterator):

    def __init__(self, team_collection, reverse=False):
        self._employers_list = []
        juniors_list = team_collection["junior"]
        middles_list = team_collection["middle"]
        seniors_list = team_collection["senior"]

        if isinstance(juniors_list, list):
            juniors_list.sort(key=lambda worker: worker.experience, reverse=reverse)
            self._employers_list.extend(juniors_list)

        if isinstance(middles_list, list):
            middles_list.sort(key=lambda worker: worker.experience, reverse=reverse)
            self._employers_list.extend(middles_list)

        if isinstance(seniors_list, list):
            seniors_list.sort(key=lambda worker: worker.experience, reverse=reverse)
            self._employers_list.extend(seniors_list)

        self._position = 0

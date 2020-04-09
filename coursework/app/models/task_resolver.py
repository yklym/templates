from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class TaskResolver:

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def resolve(self, task) -> None:

        print(f'Task {task.estimate_list}')
        # print("Context: Sorting data using the strategy (not sure how it'll do it)")
        # result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        # print(",".join(result))

class Strategy(ABC):

    @abstractmethod
    def find_employers(self, task):
        pass


class CheapStrategy(Strategy):
    def find_employers(self, task, team) -> List:
        # Some algo of returning employers
        pass

class OptimalStrategy(Strategy):
    def find_employers(self, task, team) -> List:
        # Some algo of returning employers
        pass

class FastStrategy(Strategy):
    def find_employers(self, task, team) -> List:
        # Some algo of returning employers
        pass


# if __name__ == "__main__":
#     # Клиентский код выбирает конкретную стратегию и передаёт её в контекст.
#     # Клиент должен знать о различиях между стратегиями, чтобы сделать
#     # правильный выбор.
#
#     context = Context(ConcreteStrategyA())
#     print("Client: Strategy is set to normal sorting.")
#     context.do_some_business_logic()
#     print()
#
#     print("Client: Strategy is set to reverse sorting.")
#     context.strategy = ConcreteStrategyB()
#     context.do_some_business_logic()
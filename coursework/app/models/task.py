from abc import ABC, abstractmethod, abstractproperty


class AbstractTaskBuilder(ABC):
    """
    Интерфейс Строителя объявляет создающие методы для различных частей объектов
    Продуктов.
    """

    @property
    def product(self) -> None:
        pass

    @abstractmethod
    def set_junior_est(self) -> None:
        pass

    @abstractmethod
    def set_middle_est(self) -> None:
        pass

    @abstractmethod
    def set_senior_est(self) -> None:
        pass


class Task:

    def __init__(self) -> None:
        self._estimate_list = []
        self.estimate = 0

    @property
    def estimate_list(self):
        return self._estimate_list

    def add_estimate(self, key, value) -> None:
        self._estimate_list[key] = value;


class TaskBuilder(AbstractTaskBuilder):

    def __init__(self) -> None:
        self._task = None
        self.reset()

    def reset(self) -> None:
        self._task = Task()

    @property
    def product(self) -> Task:
        task = self._task
        self.reset()
        return task

    def set_junior_est(self, val: int) -> None:
        self._task.add_estimate("junior", val)

    def set_middle_est(self, val: int) -> None:
        self._task.add_estimate("middle", val)

    def set_senior_est(self, val: int) -> None:
        self._task.add_estimate("senior", val)

# class Director:
#     def __init__(self) -> None:
#         self._builder = None
#
#     @property
#     def builder(self) -> Builder:
#         return self._builder
#
#     @builder.setter
#     def builder(self, builder: Builder) -> None:
#         self._builder = builder
#
#     def build_minimal_viable_product(self) -> None:
#         self.builder.produce_part_a()
#
#     def build_full_featured_product(self) -> None:
#         self.builder.produce_part_a()
#         self.builder.produce_part_b()
#         self.builder.produce_part_c()

#
# if __name__ == "__main__":
#     director = Director()
#     builder = ConcreteBuilder1()
#     director.builder = builder
#
#     print("Standard basic product: ")
#     director.build_minimal_viable_product()
#     builder.product.list_parts()
#
#     print("\n")
#
#     print("Standard full featured product: ")
#     director.build_full_featured_product()
#     builder.product.list_parts()
#
#     print("\n")
#
#     # Помните, что паттерн Строитель можно использовать без класса Директор.
#     print("Custom product: ")
#     builder.produce_part_a()
#     builder.produce_part_b()
#     builder.product.list_parts()

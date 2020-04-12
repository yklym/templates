from abc import ABC, abstractmethod

from models.custom_exceptions import IncompleteTaskBuiltException


class Task:
    """
    the class we are building in builder below
    """

    def __init__(self) -> None:
        self._estimate_list = []
        self.estimate = 0

    # read-only property
    @property
    def estimate_list(self):
        return self._estimate_list

    def add_estimate(self, key, value) -> None:
        self._estimate_list[key] = value;


class AbstractTaskBuilder(ABC):
    """
    BUILDER
    We are using builder because the class we create has a lot of fields and
    could have even more in the future. What is more, the storage inside the class
    is a standard dictionary with some rules which are used in other classes. If user could access
    storage by himself it would possibly cause some problems while working with strings and etc.
    Event though we grant access to the dictionary by method, we control the creation of 3 main fields and
    that provides successful interaction with other classes which also incapsulate their behaviour
    with these main fields.
    """

    @property
    def built_task(self) -> None:
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


class TaskBuilder(AbstractTaskBuilder):

    def __init__(self) -> None:
        self._task = None
        self._jun_est = 0
        self._middle_est = 0
        self._senior_est = 0
        self.reset()

    def reset(self) -> None:
        self._task = Task()

    @property
    def built_task(self) -> Task:
        """
        We control the creation of at lest one required field and also provide others
        with default values
        """
        if not (self._jun_est or self._middle_est or self._senior_est):
            raise IncompleteTaskBuiltException("Task builder")

        self._task.add_estimate("junior", self._jun_est)
        self._task.add_estimate("middle", self._middle_est)
        self._task.add_estimate("senior", self._senior_est)

        task = self._task

        self.reset()
        return task

    def set_junior_est(self, val: int) -> None:
        self._jun_est = val

    def set_middle_est(self, val: int) -> None:
        self._middle_est = val

    def set_senior_est(self, val: int) -> None:
        self._senior_est = val


"""
    Creating a director class might help in future with creating tasks
    with pre-sets hidden in the director.
    This code isn't used at the moment but can greatly help in future 
    """
# class Director:
#
#     def __init__(self, builder):
#         self._builder = builder
#
#     def create_junior_test(self):
#         self._builder.set_junior_est(15)
#         return self._builder.built_task

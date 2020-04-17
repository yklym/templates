from models.strategy import *
from models.custom_exceptions import *


class SingletonMeta(type):
    """
    provides taskresolver's singleton functionality
    """
    _instance = None

    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class TaskResolver(metaclass=SingletonMeta):
    """
    SINGLETON
    FACADE

    The class wasn't meant to be used as a facade but still it is.
    By it we hide a lot of difficult code with using strategies. As it happens, some facades
    doesn't need more than one class object. That's why we will use python metaclass to
    provide the class with singleton's properties. What is more this perfectly suits for our
    single-thread upp

    What is more, it works good with chosen framework Flask, 'cause there some global variables
    we use already and our facade will be one of them
    """

    _strategy = None

    def _run_strategy(self, task):
        ret_dict = {
            "err": ""
        }
        try:
            if not self._strategy:
                raise Exception("task resolver")
            print("In task Resolver _run")
            self._strategy.resolve_task(task)
        except CantBeResolvedByTeamException:
            # TODO catch exceptions
            print("err in task resolver")
            ret_dict["err"] = f'Task cant be resolved by team'
            pass
        except Exception as e:
            ret_dict["err"] = e
            raise e

        return ret_dict

    def resolve(self, task, team, mode="fast"):
        mode = mode.lower()

        if mode == "fast":
            self._strategy = FastStrategy(team)
        elif mode == "cheap":
            self._strategy = CheapStrategy(team)
        elif mode == "optimal":
            self._strategy = OptimalStrategy(team)
        elif mode == "favourite":
            self._strategy = FavouriteStrategy(team)
        elif mode == "tired":
            self._strategy = TiredWorkersStrategy(team)
        elif mode == "equal":
            self._strategy = EqualityStrategy(team)
        else:
            self._strategy = None

        return self._run_strategy(task)

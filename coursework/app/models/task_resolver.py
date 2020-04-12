from models.strategy import Strategy


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

    def __init__(self) -> None:
        self._strategy = None

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    # As far as we use singleton, the strategies can be changed through the work
    @strategy.setter
    def strategy(self, strategy: Strategy, team=None):
        if not isinstance(strategy, Strategy):
            # do smth, idk
            pass

        if not team:
            self._strategy = strategy

        self._strategy = strategy(team)

    def resolve(self, task) -> None:
        # Check task
        if not self._strategy:
            raise Exception("task resolver")
        self._strategy.resolve_task(task)

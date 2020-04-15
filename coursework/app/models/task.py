

class Task:
    """
    the class we are building in builder below
    """

    def __init__(self) -> None:
        self._access_level = ["junior"]
        self._estimate_dict = {}
        self.estimate = 0

    @property
    def access_level(self):
        return self._access_level

    def set_access_level(self, access_level):
        self._access_level = access_level

    @property
    def estimate_list(self):
        return self._estimate_dict

    def add_estimate(self, key, value) -> None:
        self._estimate_dict[key] = value

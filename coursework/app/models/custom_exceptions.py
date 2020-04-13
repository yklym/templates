"""Exceptions. And that's it"""


class CustomException(Exception):
    """
    Standard Python Exception class provide us with all the required functionality
    so that we don't need to ad any odd behaviour to custom exceptions

    This abstract class helps to handle all the custom exceptions in one handle
    """
    pass


class WorkerResolvingTaskException(CustomException):
    pass


class WorkerHasNoTimeException(WorkerResolvingTaskException):
    pass


class WorkerCantAccessTaskException(WorkerResolvingTaskException):
    pass


class CantBeResolvedByTeamException(CustomException):
    pass


class IncompleteTaskBuiltException(CustomException):
    pass

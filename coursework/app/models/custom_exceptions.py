class CustomException(Exception):
    pass


class WorkerHasNoTimeException(CustomException):
    pass


if __name__ == "__main__":
    print("hello")

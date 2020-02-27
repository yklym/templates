class Worker:
    _max_working_hours = 10

    """
    Worker Class
    """

    def __init__(self, salaryPerHour: int = 10):
        self._salary_per_hour = salaryPerHour
        self._checked_today = False
        self._bank = 0
        self._worked_hours = 0

    def get_max_working_hours(self):
        return self._max_working_hours

    def check_presence(self):
        return self._checked_today

    def set_presence(self, presence: "Boolean" = True) -> "rets presence":
        self._checked_today = presence
        return self._checked_today

    def get_bank(self):
        self._bank = self._worked_hours * self._salary_per_hour
        return self._bank

    def rest_hours(self):
        return self._max_working_hours - self._worked_hours

    def add_worked_hours(self, worked_hours: int = 0):
        self._worked_hours += worked_hours
        return self._worked_hours

    def reset_working_hours(self):
        self._worked_hours = 0
        return self._worked_hours


class WorkerHolidayDecorator(Worker):
    """
    Decorator for working with holidays
    """

    def __init__(self, component: Worker, holiday_hours_discount: int = 0, salary_bonus: int = 0) -> "Decorator for working with holidays":
        self._component = component
        self._salary_bonus = salary_bonus
        self._holiday_hours_discount = holiday_hours_discount

    def rest_hours(self):
        rest_hours = self._component.restHours() - self._holiday_hours_discount
        if rest_hours < 0:
            rest_hours = 0
        return rest_hours

    def getMaxWorkingHours(self):
        max_working_hours = self._component.get_max_working_hours() - \
            self._holiday_hours_discount
        if max_working_hours < 0:
            max_working_hours = 0
        return max_working_hours

    def get_bank(self):
        bank_without_bonus = self._component.get_bank()
        return bank_without_bonus + bank_without_bonus * self._salary_bonus

print("Usual worker\n------------")
USUAL_WORKER = Worker(15)
print(USUAL_WORKER.get_bank())
USUAL_WORKER.add_worked_hours(4)
print(USUAL_WORKER.get_bank())
USUAL_WORKER.reset_working_hours()
print(USUAL_WORKER.get_bank())


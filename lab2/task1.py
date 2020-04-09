from abc import ABC, abstractmethod

# Розробити модуль до програмного забезпечення, що
# використовується у приймальній комісії вузу, який буде автоматично
# створювати папку з бланками електронних документів абітурієнта (анкета,
# оцінки на іспитах тощо) тільки у разі, якщо останній набрав прохідний бал.


class Student():
    def __init__(self, mark, age, fullname):
        self.mark = mark
        self.age = age
        self.fullname = fullname


class System(ABC):

    @abstractmethod
    def save_student_data(self, student: Student) -> None:
        pass


class BaseSystem(System):

    def save_student_data(self, student: Student) -> None:
        print(f"Creating student's [{student.fullname}] data ")


class Module(System):
    required_mark = 85

    def __init__(self, real_subject: BaseSystem) -> None:
        self._real_subject = real_subject

    def save_student_data(self, student: Student) -> None:
        if self.check_mark(student):
            self._real_subject.save_student_data(student)
        else:
            print(f"Student [{student.fullname}] has bad mark")

    def check_mark(self, student) -> bool:
        return student.mark > self.required_mark


if __name__ == "__main__":
    base = BaseSystem()
    proxy = Module(base)
    student1 = Student(86, 18, "Goood student")
    student2 = Student(80, 18, "Bad Student")

    proxy.save_student_data(student1)
    proxy.save_student_data(student2)
# За допомогою шаблона «Абстрактна фабрика» організувати
# виробництво пластикових читацьких квитків до бібліотеки. Читацькі
# квитки можуть бути студентські, шкільні, наукові, особливі (для
# академіків тощо). Різні апарати можуть виготовляти пластикові картки з
# фото або без фото, з голограмою або без. В залежності від складності
# виробництва змінюється і вартість продукції. Забезпечити у програмі вибір
# апарата з виготовлення квитків у залежності від наявної суми грошей.

from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractCard(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def append_book(self):
        pass


class AbstractFactory(ABC):
    @abstractmethod
    def create_student_card(self, name) -> AbstractStudentCard:
        pass

    @abstractmethod
    def create_scientist_card(self, name) -> AbstractScientistCard:
        pass

#  Concrete Factories


class PhotoFactory(AbstractFactory):

    def create_student_card(self, name, photo) -> StudentCardPhoto:
        return StudentCardPhoto(name, photo)

    def create_scientist_card(self, name, photo) -> StudentCardPhoto:
        return ScientistCardPhoto(name, photo)


class WatermarkFactory(AbstractFactory):
    """
    Каждая Конкретная Фабрика имеет соответствующую вариацию продукта.
    """

    def create_student_card(self, name, watermark) -> StudentCardWatermark:
        return StudentCardWatermark(name, watermark)

    def create_scientist_card(self, name, watermark) -> ScientistCardWatermark:
        return ScientistCardWatermark(name, watermark)

# Student


class AbstractStudentCard(AbstractCard):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def append_book(self, book: Book):
        if book.type != "student":
            print(
                f"Student {self._name} can't use book {book.name} with type {book.type}")
        else:
            print(
                f"Student {self._name} use {book.name} with type {book.type}")


class StudentCardPhoto(AbstractStudentCard):
    def __init__(self, name, photo):
        self._photo = photo
        super().__init__(name)

    def get_photo(self):
        print(f"Students [{self._name}] photo [{self._photo}]")


class StudentCardWatermark(AbstractStudentCard):
    def __init__(self, name, watermark):
        self._watermark = watermark
        super().__init__(name)

    def get_watermark(self):
        print(f"Students [{self._name}] watermark [{self._watermark}]")

# Scientist


class AbstractScientistCard(AbstractCard):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def append_book(self, book: Book):
        if book.type != "scientist":
            print(
                f"Scientist {self._name} can't use book {book.name} with type {book.type}")
        else:
            print(
                f"Student {self._name} use {book.name} with type {book.type}")


class ScientistCardPhoto(AbstractScientistCard):
    def __init__(self, name, photo):
        self._photo = photo
        super().__init__(name)

    def get_photo(self):
        print(f"Scientist's [{self._name}] photo [{self._photo}]")


class ScientistCardWatermark(AbstractScientistCard):
    def __init__(self, name, watermark):
        self._watermark = watermark
        super().__init__(name)

    def get_watermark(self):
        print(f"Scientist's [{self._name}] watermark [{self._watermark}]")


class Book():
    def __init__(self, name, _type):
        self.name = name
        self.type = _type


if __name__ == "__main__":
    factory = PhotoFactory()
    
    stud1 = factory.create_student_card("Kebin", "Phhhh")
    print(stud1.get_name())
    stud1.get_photo()

    stud_book = Book("Hello,", "student")
    sci_book = Book("Greetings", "scientist")

    stud1.append_book(sci_book)
    stud1.append_book(stud_book)

    print("--------------------")
    factory2 = WatermarkFactory()
    stud2 = factory2.create_scientist_card("Kate", "watermark")
    print(stud2.get_name())
    stud2.get_watermark()

    stud_book = Book("Hello,", "student")
    sci_book = Book("Greetings", "scientist")

    stud2.append_book(sci_book)
    stud2.append_book(stud_book)
    print("--------------------")


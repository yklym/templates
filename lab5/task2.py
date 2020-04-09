"""User Component містить текстове поле для введення тексту та три
кнопки для його збереження до файлу. У відповідність кожній кнопці
поставлений окремий спосіб збереження тексту. Перший спосіб –
звичайний: зберігаємо текст без внесення жодних змін. Другий спосіб –
видаляємо всі зайві пробіли з тексту перед збереженням. Третій спосіб –
застосовуємо кодування тексту (або архівацію). За допомогою шаблону
проектування реалізувати описаний User Component, якщо відомо, що
метод «Зберегти у файл» у нього один (немає жодних override варіантів
методу)."""

from abc import ABC, abstractmethod
import base64


class AbstractCommand(ABC):
    @abstractmethod
    def execute(self, text) -> None:
        pass


class Command(AbstractCommand):

    def __init__(self, writer, filename, text: str) -> None:
        self._writer = writer
        self._filename = filename
        self._text = text

    def execute(self) -> None:
        self._writer.write_to_file(self._filename, self._text)


class AbstractFileWriter(ABC):
    @abstractmethod
    def write_to_file(self, filename, text):
        print(f"Abstract filewriter writes [{text}] to [{filename}]")


class UsualFileWriter(AbstractFileWriter):
    def write_to_file(self, filename, text):
        print(f"Usual filewriter writes [{text}] to [{filename}]")


class TrimFileWriter(AbstractFileWriter):
    def write_to_file(self, filename, text):
        print(f"Usual filewriter writes [{text.strip()}] to [{filename}]")


class EncodeFileWriter(AbstractFileWriter):
    def write_to_file(self, filename, text):
        text = text.encode('ascii')
        base64_bytes = base64.b64encode(text)
        print(
            f"Usual filewriter writes [{base64_bytes}] to {filename}")


class UserComponent:
    def __init__(self):
        self._filename = "result.txt"
        pass

    def write_to_file(self, command: Command):
        print("User component perfoms saving using one of three commands")
        command.execute()
        print("--------------------")

    def button1(self, text):
        self.write_to_file(Command(UsualFileWriter(), self._filename, text))

    def button2(self, text):
        self.write_to_file(Command(TrimFileWriter(), self._filename, text))

    def button3(self, text):
        self.write_to_file(Command(EncodeFileWriter(), self._filename, text))

if __name__ == "__main__":
    snp_str = input()
    cmp = UserComponent()
    cmp.button1(snp_str)
    cmp.button2(snp_str)
    cmp.button3(snp_str)

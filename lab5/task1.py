# Деякий галузевий концерн об’єднує декілька фабрик з виробництва
# устаткування для підприємств важкої промисловості. Замовлення на
# виготовлення продукції надходять з вказівкою, яка саме фабрика
# бажано повинна його виконати. У разі, якщо вказаній фабриці не
# вистачає ресурсів для виконання замовлення, вона передає замовлення
# іншій фабриці концерну. У випадку, якщо знайдено фабрику, яка може
# виконати замовлення, у клієнта перепитують, чи погоджується він
# спрямувати замовлення іншій фабриці. У випадку, якщо жодна фабрика
# не має ресурсів для виконання замовлення, про це сповіщається клієнт.
# За допомогою шаблону проектування змоделювати обробку замовлення
# концерном

from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def produce(self, employers_count):
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def produce(self, employers_count):
        print("Choosen fabric can't provide you with employers. Wouldn't you mind taking another one?")
        if(not input().upper().startswith("NO")):
            return None
        if self._next_handler:
            return self._next_handler.produce(employers_count)
        return None


class Fabric1(AbstractHandler):
    _employers = 60

    def produce(self, employers_count: int):
        if employers_count <= self._employers:
            return f"Product was created by {self.__class__.__name__} with required amount of employers [{employers_count}]"
        else:
            return super().produce(employers_count)


class Fabric2(AbstractHandler):
    _employers = 120

    def produce(self, employers_count: int):
        if employers_count <= self._employers:
            return f"Product was created by {self.__class__.__name__} with required amount of employers [{employers_count}]"
        else:
            return super().produce(employers_count)


class Fabric3(AbstractHandler):
    _employers = 250

    def produce(self, employers_count: int):
        if employers_count <= self._employers:
            return f"Product was created by {self.__class__.__name__} with required amount of employers [{employers_count}]"
        else:
            return super().produce(employers_count)


def client_code(handler, employers) -> None:
    result = handler.produce(employers)
    if result:
        print(f"{result}")
    else:
        print(f"{employers} employers can't be found in your way.", end="")


if __name__ == "__main__":
    fabric1 = Fabric1()
    fabric2 = Fabric2()
    fabric3 = Fabric3()

    fabric1.set_next(fabric2).set_next(fabric3)
    fabrics = [fabric1, fabric2, fabric3]
    while True:
        print("Choose fabric 1-3, 0 - exit")
        fabr_num = int(input())
        if fabr_num == 0 or not isinstance(fabr_num, int):
            print("Exit perfomed")
            break
        print("Insert required employers count:")
        client_code(fabrics[fabr_num - 1], int(input()))

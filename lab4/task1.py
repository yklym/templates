"""
За допомогою шаблону проектування відтворити процес вивчення
студентом певного предмету та здачі ним екзамену. За кожне
самостійне заняття студент опановує 5% матеріалу. При опануванні
студентом більше 60% матеріалу, він переходить у категорію
потенційних «трійочників», при опануванні більше 80% - у категорію
студентів, що претендують на «четвірку», та при опануванні більше
95% матеріалу – стає потенційним відмінником.
"""

from abc import ABC, abstractmethod


class Context(ABC):
    _state = None

    def __init__(self) -> None:
        self.transition_to(FMarkState())

    def transition_to(self, state):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def prepare(self):
        self._state.prepare()

    def try_exam(self):
        self._state.try_exam()


class State(ABC):
    _max_mark = None
    _req_mark = None
    _next_state = None

    def __init__(self):
        self._curr_mark = 0
        self._first_state = FMarkState


    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    def prepare(self) -> None:
        self._curr_mark += 5
        print(f"Student is preparing to {self._curr_mark}")
        if(self._curr_mark >= self._req_mark):
            if self._next_state:
                self.context.transition_to(self._next_state())
            else:
                self.context.transition_to(self._first_state())

    def try_exam(self) -> None:
        print(f"Student got mark {self._max_mark}")
        if self._first_state:
            self.context.transition_to(self._first_state())


class AMarkState(State):
    _max_mark = 5
    _req_mark = 100
    _next_state = None

    def __init__(self):
        self._curr_mark = 90
        self._first_state = FMarkState



class BMarkState(State):
    _max_mark = 4
    _req_mark = 90
    _next_state = AMarkState

    def __init__(self):
        self._curr_mark = 80
        self._first_state = FMarkState


class EMarkState(State):
    _max_mark = 3
    _req_mark = 80
    _next_state = BMarkState

    def __init__(self):
        self._curr_mark = 60
        self._first_state = FMarkState

class FMarkState(State):
    _max_mark = 2
    _req_mark = 60
    _next_state = EMarkState

    def __init__(self):
        self._curr_mark = 0
    def try_exam(self) -> None:
        print(f"Student failed")
        self._curr_mark = 0

if __name__ == "__main__":
    # Клиентский код.
    stud1 = Context()
    stud1.prepare()
    for i in range(10):
        stud1.prepare()
    stud1.try_exam()
    stud1.prepare()

    for i in range(18):
        stud1.prepare()
    stud1.try_exam()


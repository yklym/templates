import copy
from abc import ABC
from typing import Optional

# Гра у шахи. За допомогою шаблона проектування забезпечити
# заповнення шахової дошки. Для цього використати відповідні прототипи
# шахових фігур. У випадку консольної реалізації програми інформацію про
# фігури виводити на екран у форматі: «позиція фігури» (наприклад, Е2),
# «колір фігури» та «назва фігури»

alphabetics = "abcdefgh"


class SingletonMeta(type):

    _instance = None

    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class chessDeck(metaclass=SingletonMeta):

    def __init__(self):
        self._board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append("#")
            self._board.append(row)

    def get_cords(self, code):
        code[0] = code[0].lower()
        code[0] = alphabetics.index(code[0])
        return code

    def get_pos(self, code):
        code[0] = alphabetics[code[0]]
        return code

    def set_paws(self, white_prototype, black_prototype):
        for i in range(8):
            new_paw = copy.copy(white_prototype)
            new_paw.position = self.get_pos([1, i])
            self._board[1][i] =  new_paw

        for i in range(8):
            new_paw = copy.copy(black_prototype)
            new_paw.position = self.get_pos([6, i])
            self._board[6][i] =  new_paw
    
    def print_figures(self):
        for row in self._board:
            for fig in row:
                if isinstance(fig,ChessFigure):
                    print(f"Figure [{fig.color};{fig.position};{fig.name}]")
    def __str__(self):
        string = "--------\n"
        for row in self._board:
            for char in row:
                if isinstance(char, ChessFigure):
                    # string += char.symb()
                    string += char.name[0].upper()
                else: 
                    string += "#"
            string += "\n"
        string += "--------"
        return string


class ChessFigure(ABC):

    def __init__(self, position, color):
        self.position = position
        self.color = color
        self.name = self.__class__.__name__

    def __copy__(self):
        new = self.__class__(self.position, self.color)
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo={}):
        new = self.__class__(self.position, self.color)
        new.__dict__.update(self.__dict__)
        return new


class Pawn(ChessFigure):
    def symb(self):
        return "|"
    pass


if __name__ == "__main__":
    game = chessDeck()
    game.set_paws(Pawn("P1", "white"), Pawn("P1", "black"))
    print(game)
    game.print_figures()
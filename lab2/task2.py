# Кухонний комбайн має функції кавниці, сокодавильниці,
# м’ясорубки, вимішувальника тіста тощо. За допомогою шаблона
# проектування реалізувати функціональність кожного побутового пристрою
# окремо (у вигляді окремих класів), а потім організувати новий клас, який
# дозволить об’єднати функції цих пристроїв разом.


class Combine:

    def __init__(self, doughMixerClass, MincerClass) -> None:
        self._dough_mixer = doughMixerClass()
        self._mincer = MincerClass()

    def create_meat_and_fish_pie(self) -> str:
        self._dough_mixer.set_temperature_mode(1)
        self._dough_mixer.prepare_dough()

        self._mincer.turn_on()
        chopped_meat = self._mincer.chop("meat")
        self._mincer.turn_on()
        chopped_fish = self._mincer.chop("fish")

        if (not chopped_meat) or (not chopped_fish):
            print("Error while creating pie")
            return False
        self._dough_mixer.set_temperature_mode(2)
        print("----------------------\n")
        self._dough_mixer.create_pie_base(chopped_meat + " " +chopped_fish)

class DoughMixer:
    def __init__(self):
        self._temperature_mode = 0

    def set_temperature_mode(self, tmp: int) -> str:
        self._temperature_mode = tmp
        print(f"DoughMixer set temperature mode to {tmp}")
        return tmp

    def prepare_dough(self):
        if self._temperature_mode != 1:
            print("DoughMixer failed to prepare dough")
            return False
        else:
            print("DoughMixer prepared dough")
            return True

    def create_pie_base(self, filling):
        if self._temperature_mode != 2:
            print("DoughMixer couldnt create pie base")
        else:
            print(f"DoughMixer created pie base with {filling}")


class Mincer:
    def __init__(self):
        self._is_turned_on = False

    def turn_on(self):
        self._is_turned_on = True

    def chop(self, product):
        if self._is_turned_on:
            print(f"mincer chopped {product}")
            self._is_turned_on = False
            return f"chopped {product}"
        else:
            print("Mincer is turned off")
            return False


if __name__ == "__main__":
    combine = Combine(DoughMixer, Mincer)

    combine.create_meat_and_fish_pie()

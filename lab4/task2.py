"""
В залежності від тканини, з якої пошито одяг, його можна прати та
прасувати за певних умов або чистити у хімчистці. За допомогою
шаблону проектування реалізувати різні алгоритми чистки одягу:
прання при різних температурах + прасування в різних режимах праски,
а також хімічна чистка одягу.
"""
from abc import ABC, abstractmethod


class AbstractDress(ABC):

    def clean(self) -> None:
        self.take_off()
        self.transport()
        # Mutable
        self.pre_action()
        self.set_temperature_mode()
        if self.action():
            print("Clothe washed successfully")
        self.post_action()
        # -----------
        self.transport()


    def take_off(self) -> None:
        print("All the classes require taking clothes off")

    def transport(self) -> None:
        print("All the classes require transporting clothes")
    
    def set_temperature_mode(self):
        print("Set temperature mode to 65dg")

    @abstractmethod
    def pre_action(self) -> None:
        pass

    @abstractmethod
    def post_action(self) -> None:
        pass
    
    @abstractmethod
    def action(self) -> None:
        pass


class SilkDress(AbstractDress):

    def pre_action(self):
        print("silk dress needs good soap")
    def action(self):
        print("Silk dress is cleaned in laundry")
    def post_action(self):
        print("Silk dress is squeezed in laundry")

class CottonDress(AbstractDress):

    def pre_action(self):
        print("Cotton dress doesnt need soap")
    def action(self):
        print("Cotton dress is cleaned by hand in cold water")
    def post_action(self):
        print("Cotton dress is hanged on the yard")

    def set_temperature_mode(self):
        print("Cotton dress set temperature mode to 65dg")

if __name__ == "__main__":
    silk = SilkDress()
    silk.clean()
    print("_-__--_-_-_-__")

    cotton = CottonDress()
    cotton.clean()
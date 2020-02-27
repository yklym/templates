from abc import ABC, abstractmethod

# Bridge -----------------------------

class CatNameImplementation(ABC):
    pass

class NamedCat(CatNameImplementation):
    def __init__(self, name):
        self.name = name

class UnnamedCat(CatNameImplementation):
    def __init__(self):
        self.name = "Unnamed Cat"


# Base-----------------------------------

class AbstractCat(ABC):
    """
    Abstract Cat interface
    """
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

class Cat(AbstractCat):
    """
    Base abstract Cat interface realization
    """

    def __init__(self, name_implementation: "helloo" = None):
        self._name_implementation = name_implementation

    def eat(self):
        print("Cat [{0}] is eating".format(self.get_name()))

    def sleep(self):
        print("Cat [{0}] ZZZZZZzzzzzZZZZZzzzz".format(self.get_name()))

    def get_name(self):
        return self._name_implementation.name

# Decorators ---------------------------

class CatDecorator(Cat):
    """
    Abstract decorator
    """
    _component = None

    def __init__(self, component: Cat):
        self._component = component

    def get_name(self):
        return self._component.get_name()

class DomesticCatDecorator(CatDecorator):
    def play(self):
        print("Domestic Cat [{}] is playing!".format(self.get_name()))

class KittenDecorator(DomesticCatDecorator):
    def play(self):
        print("The kitten [{}] is playing!".format(self.get_name()))

    def play_cute(self):
        print("The kitten [{}] playing so cute!".format(self.get_name()))

class WildCatDecorator(CatDecorator):
    def hunt(self):
        print("Wild Cat [{}] is hunting!".format(self.get_name()))

class LynxDecorator(WildCatDecorator):
    def hunt(self):
        print("Lynx [{}] is hunting!".format(self.get_name()))

    def hunt_sneaky(self):
        print("Lynx [{}] is hunting sneaky!".format(self.get_name()))


cat_name = input()
new_cat = None

# Bridge example

if cat_name:
    implementation = NamedCat(cat_name)
    new_cat = Cat(implementation)
    new_cat.sleep()
else:
    implementation = UnnamedCat()
    new_cat = Cat(implementation)
    new_cat.sleep()


# Domestic cat --------------------
dom_cat = DomesticCatDecorator(new_cat)
dom_cat.play()
print("\n")

# kitten --------------------------
kitten_dec = KittenDecorator(new_cat)
kitten_dec.play()
kitten_dec.play_cute()
print("\n")

# Wild cat -----------------------
wild_cat = WildCatDecorator(new_cat)
wild_cat.hunt()
print("\n")

# lynx ---------------------------
lynx_dec = LynxDecorator(new_cat)
lynx_dec.hunt()
lynx_dec.hunt_sneaky()
print("\n")

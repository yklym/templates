from abc import ABC, abstractmethod


class Component(ABC):

    def __init__(self, name):
        self.name = name
    
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def add(self, component) -> None:
        pass

    def remove(self, component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def inform(self) -> str:
        pass


class Employer(Component):
    def ___init__(self, name):
        self.name = name

    def inform(self) -> str:
        return "Employer [{}] was informed".format(self.name)


class Director(Component):

    def __init__(self, name="unnamed director") -> None:
        # List of leaves
        self.name = name
        self._children = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def inform(self) -> str:
        results = []
        for child in self._children:
            results.append(child.inform())
        results.append("Director [{}] was informed".format(self.name))
        return "\n".join(results)


def inform(component):
    print(f"{component.inform()}")


if __name__ == "__main__":
    simple = Employer("kate")
    inform(simple)

    tree = Director("Main Dir Den")

    branch1 = Director("Vlad")
    branch1.add(simple)
    branch1.add(Employer("Veva"))

    branch2 = Director("Vlad 2")
    branch2.add(simple)

    tree.add(branch1)
    tree.add(branch2)

    inform(tree)
from typing import TypeAlias, Callable, Literal, Self

# OptionalStr:TypeAlias = str|None
#
# Mode: TypeAlias = Literal["a","r","z"]
# Printer: TypeAlias = Callable[[str], str]
FruitType: TypeAlias = "Fruit"


class Fruit:
    def __init__(self, name:str)-> None:
        self.name = name

def fruit_method(self) ->FruitType:
    return self
from typing import Protocol

class Printer(Protocol):

    def print(self, magazine: str) -> None:
        ...

    def copy(self, magazine: str, copies:int) -> None:
        ...

class LazerPrinter:
    def __init__(self, name: str, version: int) -> None:
        self.name = name
        self.version = version

    def print(self, magazine: str) -> None:
        print(f"{self.name} ({self.version}) is printing: {magazine}.")


    def copy(self, magazine: str, copies: int) -> None:
        print(f"{self.name} ({self.version}) is making {copies} copies of: {magazine}")


lp: Printer = LazerPrinter("LazerPrinter", 1)

def print_magazine(printer: Printer, magazine: str) -> None:
    printer.print(magazine)
    print("Performing extra logic...")
    printer.copy(magazine, 5)
    print("Shutting down printer...")

print_magazine(lp, "Python and Javascript Times")

class InkJetPrinter:
    def __init__(self, name: str, version: int) -> None:
        self.name = name
        self.version = version

    def print(self, magazine: str) -> None:
        print(f"{self.name} ({self.version}) is printing: {magazine}.")


    def copy(self, magazine: str, copies: int) -> None:
        print(f"{self.name} ({self.version}) is making {copies} copies of: {magazine}")

    def extra_func(self):
        ...


ijp:Printer = InkJetPrinter("InkJetPrinter", 10)
print_magazine(ijp,"Geeks of Python and Javascript")


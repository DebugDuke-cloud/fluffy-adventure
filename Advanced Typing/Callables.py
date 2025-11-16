from typing import Callable
# from datetime import datetime
#
# def get_time() -> str:
#     return f"{datetime.now():%H:M}"
#
# # print(get_time())
#
# def repeat(func: Callable, amount: int) -> None:
#     for i in range(amount):
#         print(f"{i + 1}: {func()}")
#
#
# repeat("hello", 3)

from typing import Callable
def print_it(text: str, print_func: Callable[[str], None]) -> None:
    print_func(text)

def loud_print(text: str) -> None:
    print(f"{text.upper()}!")

def silent_print(text: str) -> None:
    print(f"{text.lower()}!")


def get_letters(text: str) -> list[str]:
    return list(text)

print_it("Hello", loud_print)
print_it("Hello", silent_print)
print_it("Hello", get_letters)




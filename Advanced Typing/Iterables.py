from typing import Iterable

def list_elements(elements: Iterable) -> None:
    for i, element in enumerate(elements, start=1):
        print(i, element, sep=":")


people: list[str] = ["Mario", "Luigi",234]
list_elements(people)



def list_elements(elements: Iterable[str]) -> None:
    for i, element in enumerate(elements, start=1):
        print(i, element, sep=":")


people: list[str] = ["Mario", "Luigi","James"]
list_elements(people)
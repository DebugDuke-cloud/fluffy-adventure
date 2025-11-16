from typing import Generator, Iterator

def generate() -> Iterator[int]:
    for i in range(3):
           yield i


numbers: Iterator[int] = generate()
print(next(numbers))
print(next(numbers))
print(next(numbers))

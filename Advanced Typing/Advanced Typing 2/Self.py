from typing import Self


class File:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath


    @classmethod
    def create_file(cls,name:str, ext: str)-> "File":
        return cls(f"{name}.{ext}")


    file: File = File.create("cat","jpg")
    print(file.filepath)

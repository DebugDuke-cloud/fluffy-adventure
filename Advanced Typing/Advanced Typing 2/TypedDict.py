from typing import TypedDict, NotRequired,Required


# class Coordinate(TypedDict):
#     x: float
#     y: float
#     label:str
#     category: NotRequired[str]
#
#
#
# coordinate: Coordinate = {"x": 20, "y":10,  "label": "Profit","category": "Finance"}

Vote = TypedDict(name= "Vote", fields={"for": int, "against": int, "topic": Required[str]}, total=False)
vote: Vote = {"for": 100, "Topic": "More money for everyone"}

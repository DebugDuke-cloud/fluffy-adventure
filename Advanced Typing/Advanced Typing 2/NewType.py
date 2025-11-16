from typing import TypeAlias, NewType

UserId: TypeAlias = int


def get_user(userid: UserId) -> str| None:
    users: dict ={0:"Mario",1:"James", 2:"Luigi"}
    return users.get(userid)

print(get_user(0))
print(get_user(False))
print(get_user(UserId(0)))


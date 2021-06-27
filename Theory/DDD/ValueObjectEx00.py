import dataclasses


@dataclasses.dataclass(frozen=True)
class UserId:
    id: int


@dataclasses.dataclass(frozen=True)
class UserName:
    name: str


class User:
    def __init__(self, user_id: UserId, user_name: UserName):
        self.user_id = user_id
        self.user_name = user_name


user_id = UserId(1)
user_name = UserName("kota")

user_valid = User(user_id, user_name)
# user_invalid = User(user_name, user_id)

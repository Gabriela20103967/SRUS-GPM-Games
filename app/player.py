class Player:
    def __init__(self, uid: str, name: str) -> None:
        self.__uid = uid
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @property
    def name(self) -> str:
        return self.__name

    def __str__(self):
        return f"Player(uid={self.__uid}, name={self.__name})"

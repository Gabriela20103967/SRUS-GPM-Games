from argon2 import PasswordHasher


class Player:
    """
    A class which represent a player

    Attributes:
        uid (str): The unique identifier for the player.
        name (str): The name of the player.
    """
    def __init__(self, uid: str, name: str) -> None:
        """
        Initializes a player instance

        Args:
            uid (str): The unique identifier for the player.
            name (str): The name of the player.
        """
        self.__uid = uid
        self.__name = name

    @property
    def uid(self) -> str:
        """
        Gets the uid of the player.

        :return:
        str: The unique identifier of the player
        """
        return self.__uid

    @property
    def name(self) -> str:
        """
        Gets the name of the player

        :return:
        str: The name of the player
        """
        return self.__name

    def add_password(self, password: str):
        """
        Hashes and store the player's password.

        Args:
            password (str): The password to be hashed and store.
        """
        ph = PasswordHasher()
        self.__hashed_password = ph.hash(password)

    def verify_password(self, password: str):
        """
        Verify the provide password against the stored hashed password.

        Args:
            password (str): The password to verify

        :return:
        bool: True if the password match with the store hash, and false otherwise.

        """
        ph = PasswordHasher()
        try:
            return ph.verify(self.__hashed_password, password)
        except:
            return False

    def __str__(self):
        """
        Return a string representation of the player.

        :return:
        str: a string that describe the player
        """
        return f"Player(uid={self.__uid}, name={self.__name})"



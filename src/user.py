from abc import ABC, abstractmethod


class IUser(ABC):
    
    @abstractmethod
    def user_move():
        """user move"""


class Bot(IUser):

    def __init__(self) -> None:
        self.user_index: int = -1

    def user_move(self, board: list):
        pass


class Player(IUser):

    def __init__(self) -> None:
        self.user_index: int = -1

    def user_move(self, board: list):
        pass
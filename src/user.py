from abc import ABC, abstractmethod
import numpy as np


class IUser(ABC):
    @abstractmethod
    def pre_user_move():
        """user move"""


class Bot(IUser):

    def __init__(self) -> None:
        self.first_move: bool = False
        self.user_figures: list = []

    def __repr__(self) -> str:
        return "Bot"

    def pre_user_move(self, game) -> int:
        self.first_move = True
        return -1 # correct move

class Player(IUser):

    def __init__(self) -> None:
        self.first_move: bool = False
        self.user_figures: list = []
        self.picked_figure = None
        self.picked_place = None

    def __repr__(self) -> str:
        return "Player"
    
    def pre_user_move(self, game) -> int:
        if self.picked_figure is None:
            clicked, col, row = game.place_clicked
            if clicked is False: return -3
            piece = game.game_board[row][col]
            if piece is None: return -3
            if piece.figure_owner != self: return -3
            self.picked_figure = piece
            return -3
        
        if self.picked_place is None:
            clicked, row, col = game.place_clicked
            if clicked is False: return -3
            if self.picked_figure.is_figure_move_correct((row, col), game) is False: 
                self.picked_figure = None
                self.picked_place = None
                return -2
            
            self.picked_place = (row, col)
            return -3

        game.make_move(self.picked_figure, self.picked_place) # make move
        self.first_move = True
        self.picked_figure = None
        self.picked_place = None
        return -1 # correct move
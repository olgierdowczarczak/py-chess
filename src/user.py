from abc import ABC, abstractmethod
from figure import *


class IUser(ABC):
    @abstractmethod
    def user_move():
        """user move"""


class Bot(IUser):

    def __init__(self) -> None:
        self.first_move: bool = False
        self.user_figures: list = []

    def __repr__(self) -> str:
        return "Bot"

    def user_move(self, game) -> int:
        best_figure_move: tuple = (0, 0, 0, 0) # point, move, direction, object
        
        for figure in self.user_figures:
            best_move_in_figure: tuple = (0, 0, 0) # point, move, direction

            for direction in figure.figures_directions:
                best_move_in_direction: tuple = (0, 0) # point, move

                move_touch: bool = False
                move_point: int = 0
                for move in range(1, figure.figure_move + 1):
                    move_point: int = figure.check_figure_move(direction, move, game)
                    # print(direction, move, move_point)
                    if move_point == 0:
                        continue

                    if move_touch is True:
                        continue

                    if move_point == -1:
                        move_touch = True
                        continue
                    
                    if move_point > best_move_in_direction[0]:
                        best_move_in_direction = (move_point, move)

                if best_move_in_direction[0] > best_move_in_figure[0]:
                    best_move_in_figure = (best_move_in_direction[0], best_move_in_direction[1], direction)

            print(figure, figure.figure_position, best_move_in_figure)

        self.first_move = True
        return -1


class Player(IUser):

    def __init__(self) -> None:
        self.first_move: bool = False
        self.user_figures: list = []

    def __repr__(self) -> str:
        return "Player"
    
    def user_move(self, game) -> int:
        self.first_move = True
        return -1
from abc import ABC, abstractmethod


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
        best_move: tuple = (0, 0, 0, 0) # point, move, direction, figure

        for figure in self.user_figures:
            move_in_figure: tuple = (0, 0, 0) # point, move, direction

            for direction in figure.figures_directions:
                move_in_direction: tuple = (0, 0) # point, move
                move_point: int = 0

                for move in range(figure.figure_move):
                    move_point: int = figure.check_figure_move(direction, move, game)
                    if move_point == -1: break # own figure in path
                    if move_point == 0: continue # blocked move
                    if move_point > move_in_direction[0]: move_in_direction = (move_point, move)
                if move_in_direction[0] > move_in_figure[0]: move_in_figure = (move_in_direction[0], move_in_direction[1], direction)
            if move_in_figure[0] > best_move[0]: best_move = (move_in_figure[0], move_in_figure[1], move_in_figure[2], figure)

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
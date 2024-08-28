from abc import ABC, abstractmethod


class IUser(ABC):
    @abstractmethod
    def pre_user_move():
        """user move"""

    @abstractmethod
    def post_user_move():
        """user make move"""


class Bot(IUser):

    def __init__(self) -> None:
        self.first_move: bool = False
        self.user_figures: list = []

    def __repr__(self) -> str:
        return "Bot"

    def pre_user_move(self, game) -> int:
        figure = self.user_figures[1]
        direction = figure.figures_directions["NE"]
        move = 1

        row, col = figure.figure_position
        for _ in range(move):
            row += direction[0]
            col += direction[1]

        print(game.check_move((row, col)))

        self.first_move = True
        return 1
    
    def post_user_move(self, move: tuple, game) -> int: # point, move, direction, figure
        return 1

class Player(IUser):

    def __init__(self) -> None:
        self.first_move: bool = False
        self.user_figures: list = []
        self.made_move: bool = False
        self.figure_selected = None
        self.place_selected = None

    def __repr__(self) -> str:
        return "Player"
    
    def pre_user_move(self, game) -> int:
        cliecked, row, col = game.place_clicked
        if cliecked is False: return -1

        if self.figure_selected:
            if self.place_selected is None:
                # select place to put selected figure
                return -1
            else:
                ret: tuple = (self.place_selected, game)
                self.figure_selected = None
                self.place_selected = None
                if self.made_move: self.first_move = True
                return self.post_user_move(ret)
        else:
            selected_figure = game.game_board[col][row]
            if selected_figure is None: return -1
            if selected_figure.figure_owner != self: return -1
            self.figure_selected = selected_figure
            return -2
    
    def post_user_move(self, move: tuple, game) -> int: # x, y
        return 1
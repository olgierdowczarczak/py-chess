from abc import ABC, abstractmethod


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
        # to do
        figure = self.user_figures[1]
        direction = figure.figures_directions["NE"]
        move = 1

        row, col = figure.figure_position
        for _ in range(move):
            row += direction[0] * (-1 if figure.figure_owner == game.users_list[1] else 1)
            col += direction[1] * (-1 if figure.figure_owner == game.users_list[1] else 1)

        if figure.is_figure_move_correct((row, col), game) is False:
            return -2 # wrong move
        
        game.make_move(figure, (row, col)) # make move

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
            cliecked, row, col = game.place_clicked
            if cliecked is False: return -3
            
            item = game.game_board[col][row]
            if item is None: return -3
            if item.figure_owner != self: return -3
            self.picked_figure = item
            return -3
        
        if self.picked_place is None:
            cliecked, row, col = game.place_clicked
            if cliecked is False: return -3
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
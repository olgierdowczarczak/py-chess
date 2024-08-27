from abc import ABC, abstractmethod


class IUser(ABC):
    @abstractmethod
    def user_move():
        """user move"""

    @abstractmethod
    def make_move():
        """user make move"""


class Bot(IUser):

    def __init__(self) -> None:
        self.first_move: bool = False
        self.user_figures: list = []

    def __repr__(self) -> str:
        return "Bot"

    def user_move(self, game) -> int:
        best_move: tuple = (-1, 0, 0, 0)  # point, move, direction, figure

        for figure in self.user_figures:
            move_in_figure: tuple = (-1, 0, 0)  # point, move, direction

            for direction in figure.figures_directions:
                move_in_direction: tuple = (-1, 0)  # point, move
                move_point: int = 0
                blocked: bool = False

                for move in range(figure.figure_move + 1):
                    if blocked is True:
                        continue

                    move_point: int = figure.check_figure_move(direction, move, game)       

                    if move_point == -1:  # own figure in path 
                        blocked = True
                        continue

                    if move_point == 0: continue  # blocked move
                    if move_point > move_in_direction[0]: move_in_direction = (move_point, move)

                if blocked is True:
                    blocked = False
                    continue

                if move_in_direction[0] > move_in_figure[0]: 
                    move_in_figure = (move_in_direction[0], move_in_direction[1], direction)

            if move_in_figure[0] > best_move[0]: 
                best_move = (move_in_figure[0], move_in_figure[1], move_in_figure[2], figure)
        
        self.first_move = True
        return self.make_move(best_move, game)
    
    def make_move(self, move: tuple, game) -> int: # point, move, direction, figure
        row, col = move[3].figure_position
        game.game_board[col][row] = None

        for _ in range(move[1]+1):
            row += move[3].figures_directions[move[2]][0]
            col += move[3].figures_directions[move[2]][1]

        move[3].figure_position = (row, col)
        game.game_board[col][row] = move[3]
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
    
    def user_move(self, game) -> int:
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
                return self.make_move(ret)
        else:
            selected_figure = game.game_board[col][row]
            if selected_figure is None: return -1
            if selected_figure.figure_owner != self: return -1
            self.figure_selected = selected_figure
            return -2
    
    def make_move(self, move: tuple, game) -> int: # x, y
        return 1
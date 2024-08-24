from abc import ABC, abstractmethod


class IFigure(ABC):

    @abstractmethod
    def move_figure():
        """move figure"""


class Pawn(IFigure):
    # possible figure moves
    figure_moves: dict = {
        "N" : [0, 1],
        "NE" : [1, 1],
        "NW" : [-1, 1],
    }
    
    # figure field move
    figure_move: int = 1

    def __init__(self, user_index: int, figure_position: tuple) -> None:
        self.user_index: int = user_index
        self.figure_position: tuple = figure_position

    def __repr__(self) -> str:
        return "P"

    def move_figure(self, direction: str):
        ...

    
class Rook(IFigure):
    # possible figure moves
    figure_moves: dict = {
        "N" : [0, 1],
        "NE" : [1, 1],
        "E" : [1, 0],
        "SE" : [1, -1],
        "S" : [0, -1],
        "SW" : [-1, -1],
        "W" : [-1, 0],
        "NW" : [-1, 1],
    }
    
    # figure field move
    figure_move: int = 8

    def __init__(self, user_index: int, figure_position: tuple) -> None:
        self.user_index: int = user_index
        self.figure_position: tuple = figure_position

    def __repr__(self) -> str:
        return "R"

    def move_figure(self, direction: str):
        ...


class Knight(IFigure):
    # possible figure moves
    figure_moves: dict = {
        "NE" : [1, 2],
        "SE" : [2, -1],
        "SW" : [-2, -1],
        "NW" : [-2, 1],
    }
    
    # figure field move
    figure_move: int = 1

    def __init__(self, user_index: int, figure_position: tuple) -> None:
        self.user_index: int = user_index
        self.figure_position: tuple = figure_position

    def __repr__(self) -> str:
        return "K"

    def move_figure(self, direction: str):
        ...


class Bishop(IFigure):
    # possible figure moves
    figure_moves: dict = {
        "NE" : [1, 1],
        "SE" : [1, -1],
        "SW" : [-1, -1],
        "NW" : [-1, 1],
    }
    
    # figure field move
    figure_move: int = 8

    def __init__(self, user_index: int, figure_position: tuple) -> None:
        self.user_index: int = user_index
        self.figure_position: tuple = figure_position

    def __repr__(self) -> str:
        return "B"

    def move_figure(self, direction: str):
        ...


class Queen(IFigure):

    # possible figure moves
    figure_moves: dict = {
        "N" : [0, 1],
        "NE" : [1, 1],
        "E" : [1, 0],
        "SE" : [1, -1],
        "S" : [0, -1],
        "SW" : [-1, -1],
        "W" : [-1, 0],
        "NW" : [-1, 1],
    }
    
    # figure field move
    figure_move: int = 8

    def __init__(self, user_index: int, figure_position: tuple) -> None:
        self.user_index: int = user_index
        self.figure_position: tuple = figure_position

    def __repr__(self) -> str:
        return "Q"

    def move_figure(self, direction: str):
        ...


class King(IFigure):

    # possible figure moves
    figure_moves: dict = {
        "N" : [0, 1],
        "NE" : [1, 1],
        "E" : [1, 0],
        "SE" : [1, -1],
        "S" : [0, -1],
        "SW" : [-1, -1],
        "W" : [-1, 0],
        "NW" : [-1, 1],
    }
    
    # figure field move
    figure_move: int = 1

    def __init__(self, user_index: int, figure_position: tuple) -> None:
        self.user_index: int = user_index
        self.figure_position: tuple = figure_position

    def __repr__(self) -> str:
        return "F"

    def move_figure(self, direction: str):
        ...


class FigureFactory:

    @staticmethod
    def build_figure(figure_type: str):
        match figure_type:
            case "Pawn": return Pawn
            case "Rook": return Rook
            case "Knight": return Knight
            case "Bishop": return Bishop
            case "Queen": return Queen
            case "King": return King
            case _: raise TypeError(f"{figure_type} is not allowed figure type!")
from abc import ABC, abstractmethod


class IFigure(ABC):

    @abstractmethod
    def check_figure_move():
        """move figure"""


class Pawn(IFigure):

    # possible figure moves

    figures_directions: dict = {
        "N" : [0, 1],
        "NE" : [1, 1],
        "NW" : [-1, 1],
    }
    
    figure_point: int = 1
    figure_move: int = 2

    def __init__(self, figure_owner, figure_position: tuple) -> None:
        self.figure_owner = figure_owner
        self.figure_position: tuple = figure_position

    def __repr__(self) -> str:
        return "P"

    def check_figure_move(self, direction: str, move: int, game) -> int:
        position_object = game.check_move(self.figure_position, self.figures_directions[direction], move)
        if position_object == 0:
            return 0
        
        if game.mover.first_move == True and game > 1:
            return 0
        
        if position_object is None:
            if direction == "NE" or direction == "NW":
                return 0 
                
            return 1
        
        if position_object.figure_owner == game.mover:
            return -1

        return position_object.figure_point
    

class Rook(IFigure):
    
    # possible figure moves
    figures_directions: dict = {
        "N" : [0, 1],
        "E" : [1, 0],
        "S" : [0, -1],
        "W" : [-1, 0],
    }
    
    figure_point: int = 2
    figure_move: int = 8

    def __init__(self, figure_owner, figure_position: tuple) -> None:
        self.figure_owner = figure_owner
        self.figure_position: tuple = figure_position

    def __repr__(self) -> str:
        return "R"

    def check_figure_move(self, direction: str, move: int, game) -> int:
        position_object = game.check_move(self.figure_position, self.figures_directions[direction], move)
        if position_object == 0:
            return 0
        
        if position_object is None:
            return 1
        
        if position_object.figure_owner == game.mover:
            return -1

        return position_object.figure_point


class Knight(IFigure):

    # possible figure moves
    figures_directions: dict = {
        "NE" : [1, 2],
        "SE" : [2, -1],
        "SW" : [-2, -1],
        "NW" : [-2, 1],
    }
    # !TO UPDATE DIRECTION
    
    figure_point: int = 3
    figure_move: int = 1

    def __init__(self, figure_owner, figure_position: tuple) -> None:
        self.figure_owner = figure_owner
        self.figure_position: tuple = figure_position

    def __repr__(self) -> str:
        return "K"

    def check_figure_move(self, direction: str, move: int, game) -> int:
        position_object = game.check_move(self.figure_position, self.figures_directions[direction], move)
        if position_object == 0:
            return 0
        
        if position_object is None:
            return 1
        
        if position_object.figure_owner == game.mover:
            return -1

        return position_object.figure_point


class Bishop(IFigure):

    # possible figure moves
    figures_directions: dict = {
        "NE" : [1, 1],
        "SE" : [1, -1],
        "SW" : [-1, -1],
        "NW" : [-1, 1],
    }
    
    figure_point: int = 4
    figure_move: int = 8

    def __init__(self, figure_owner, figure_position: tuple) -> None:
        self.figure_owner = figure_owner
        self.figure_position: tuple = figure_position

    def __repr__(self) -> str:
        return "B"

    def check_figure_move(self, direction: str, move: int, game) -> int:
        position_object = game.check_move(self.figure_position, self.figures_directions[direction], move)
        if position_object == 0:
            return 0
        
        if position_object is None:
            return 1
        
        if position_object.figure_owner == game.mover:
            return -1

        return position_object.figure_point


class Queen(IFigure):

    # possible figure moves
    figures_directions: dict = {
        "N" : [0, 1],
        "NE" : [1, 1],
        "E" : [1, 0],
        "SE" : [1, -1],
        "S" : [0, -1],
        "SW" : [-1, -1],
        "W" : [-1, 0],
        "NW" : [-1, 1],
    }
    
    figure_point: int = 5
    figure_move: int = 8

    def __init__(self, figure_owner, figure_position: tuple) -> None:
        self.figure_owner = figure_owner
        self.figure_position: tuple = figure_position

    def __repr__(self) -> str:
        return "Q"

    def check_figure_move(self, direction: str, move: int, game) -> int:
        position_object = game.check_move(self.figure_position, self.figures_directions[direction], move)
        if position_object == 0:
            return 0
        
        if position_object is None:
            return 1
        
        if position_object.figure_owner == game.mover:
            return -1

        return position_object.figure_point


class King(IFigure):

    # possible figure moves
    figures_directions: dict = {
        "N" : [0, 1],
        "NE" : [1, 1],
        "E" : [1, 0],
        "SE" : [1, -1],
        "S" : [0, -1],
        "SW" : [-1, -1],
        "W" : [-1, 0],
        "NW" : [-1, 1],
    }
    
    figure_point: int = 6
    figure_move: int = 1

    def __init__(self, figure_owner, figure_position: tuple) -> None:
        self.figure_owner = figure_owner
        self.figure_position: tuple = figure_position

    def __repr__(self) -> str:
        return "H"

    def check_figure_move(self, direction: str, move: int, game) -> int:
        position_object = game.check_move(self.figure_position, self.figures_directions[direction], move)
        if position_object == 0:
            return 0
        
        if position_object is None:
            return 1
        
        if position_object.figure_owner == game.mover:
            return -1

        return position_object.figure_point


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
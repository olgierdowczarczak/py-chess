from abc import ABC, abstractmethod


class IFigure(ABC):

    @abstractmethod
    def is_figure_move_correct():
        """move figure"""
    

class FigureLogic:
    def check_direction(self, new_position: tuple, game) -> bool:
        for direction in self.figures_directions:
            start_position: tuple = self.figure_position
            row, col = start_position

            for _ in range(self.figure_move):
                row += self.figures_directions[direction][0] * (-1 if self.figure_owner == game.users_list[1] else 1)
                col += self.figures_directions[direction][1] * (-1 if self.figure_owner == game.users_list[1] else 1)

                try: item = game.game_board[col][row]
                except IndexError: break

                if not item is None:
                    if item.figure_owner == self.figure_owner: break # if own figure on path
                    elif item and ((row, col) != new_position): break # if enemy figure on path

                if ((row, col) == new_position):
                    return direction

        return None

    def check_figure_move(self, new_position: tuple, game) -> bool:
        if game.is_place_out_of_board(new_position) is True: return False # Move out of board 
        item = game.game_board[new_position[1]][new_position[0]]
        if item is None: return True # No object
        if item.figure_owner == self.figure_owner: return False # Own figure
        
        return True # Move correct


class Pawn(IFigure, FigureLogic):

    figures_directions: dict = {
        "N" : [0, 1],
        "NE" : [1, 1],
        "NW" : [-1, 1],
    }
    
    figure_point: int = 1
    figure_move: int = 2
    figure_files: list = ["images/w_pawn.png", "images/b_pawn.png"]

    def __init__(self, figure_owner, figure_position: tuple, figure_image) -> None:
        self.figure_owner = figure_owner
        self.figure_position: tuple = figure_position
        self.figure_image = figure_image

    def __repr__(self) -> str:
        return "P"

    def is_figure_move_correct(self, new_position: tuple, game) -> bool:
        if self.check_figure_move(new_position, game) is False: return False
        
        direction = self.check_direction(new_position, game)
        if not direction == "N":
            item = game.game_board[new_position[1]][new_position[0]]
            if item == None: return False # Block move
            elif item.figure_owner == self.figure_owner: return False # Own figure
        
        if direction is None: return False
        return True
    

class Rook(IFigure, FigureLogic):
    
    figures_directions: dict = {
        "N" : [0, 1],
        "E" : [1, 0],
        "S" : [0, -1],
        "W" : [-1, 0],
    }
    
    figure_point: int = 2
    figure_move: int = 8
    figure_files: list = ["images/w_rook.png", "images/b_rook.png"]

    def __init__(self, figure_owner, figure_position: tuple, figure_image) -> None:
        self.figure_owner = figure_owner
        self.figure_position: tuple = figure_position
        self.figure_image = figure_image

    def __repr__(self) -> str:
        return "R"

    def is_figure_move_correct(self, new_position: tuple, game) -> bool:
        if self.check_figure_move(new_position, game) is False: return False
        if self.check_direction(new_position, game) is None: return False
        return True


class Knight(IFigure, FigureLogic):

    figures_directions: dict = {
        "NE" : [1, 2],
        "E"  : [2, 1],
        "SE" : [2, -1],
        "S"  : [1, -2],
        "SW" : [-1, -2],
        "W"  : [-2, -1],
        "NW" : [-2, 1],
        "N"  : [-1, 2],
    }
    
    figure_point: int = 3
    figure_move: int = 1
    figure_files: list = ["images/w_knight.png", "images/b_knight.png"]

    def __init__(self, figure_owner, figure_position: tuple, figure_image) -> None:
        self.figure_owner = figure_owner
        self.figure_position: tuple = figure_position
        self.figure_image = figure_image

    def __repr__(self) -> str:
        return "K"

    def is_figure_move_correct(self, new_position: tuple, game) -> bool:
        if self.check_figure_move(new_position, game) is False: return False
        if self.check_direction(new_position, game) is None: return False
        return True


class Bishop(IFigure, FigureLogic):

    figures_directions: dict = {
        "NE" : [1, 1],
        "SE" : [1, -1],
        "SW" : [-1, -1],
        "NW" : [-1, 1],
    }
    
    figure_point: int = 4
    figure_move: int = 8
    figure_files: list = ["images/w_bishop.png", "images/b_bishop.png"]

    def __init__(self, figure_owner, figure_position: tuple, figure_image) -> None:
        self.figure_owner = figure_owner
        self.figure_position: tuple = figure_position
        self.figure_image = figure_image

    def __repr__(self) -> str:
        return "B"

    def is_figure_move_correct(self, new_position: tuple, game) -> bool:
        if self.check_figure_move(new_position, game) is False: return False
        if self.check_direction(new_position, game) is None: return False
        return True


class Queen(IFigure, FigureLogic):

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
    figure_files: list = ["images/w_queen.png", "images/b_queen.png"]

    def __init__(self, figure_owner, figure_position: tuple, figure_image) -> None:
        self.figure_owner = figure_owner
        self.figure_position: tuple = figure_position
        self.figure_image = figure_image

    def __repr__(self) -> str:
        return "Q"

    def is_figure_move_correct(self, new_position: tuple, game) -> bool:
        if self.check_figure_move(new_position, game) is False: return False
        if self.check_direction(new_position, game) is None: return False
        return True


class King(IFigure, FigureLogic):

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
    figure_files: list = ["images/w_king.png", "images/b_king.png"]

    def __init__(self, figure_owner, figure_position: tuple, figure_image) -> None:
        self.figure_owner = figure_owner
        self.figure_position: tuple = figure_position
        self.figure_image = figure_image

    def __repr__(self) -> str:
        return "H"

    def is_figure_move_correct(self, new_position: tuple, game) -> bool:
        if self.check_figure_move(new_position, game) is False: return False
        if self.check_direction(new_position, game) is None: return False
        return True


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
from user import Bot, Player
from figure import FigureFactory


class Game:

    def __init__(self) -> None:
        # init board
        self.game_board: list = [[_ for _ in range(8)] for _ in range(8)]
        self.game_board[0] = [
            FigureFactory.build_figure("Rook")(0, (0, 0)),
            FigureFactory.build_figure("Knight")(0, (1, 0)),
            FigureFactory.build_figure("Bishop")(0, (2, 0)),
            FigureFactory.build_figure("Queen")(0, (3, 0)),
            FigureFactory.build_figure("King")(0, (4, 0)),
            FigureFactory.build_figure("Bishop")(0, (5, 0)),
            FigureFactory.build_figure("Knight")(0, (6, 0)),
            FigureFactory.build_figure("Rook")(0, (7, 0)),
        ]
        self.game_board[1] = [
            FigureFactory.build_figure("Rook")(0, (0, 1)),
            FigureFactory.build_figure("Rook")(0, (1, 1)),
            FigureFactory.build_figure("Rook")(0, (2, 1)),
            FigureFactory.build_figure("Rook")(0, (3, 1)),
            FigureFactory.build_figure("Rook")(0, (4, 1)),
            FigureFactory.build_figure("Rook")(0, (5, 1)),
            FigureFactory.build_figure("Rook")(0, (6, 1)),
            FigureFactory.build_figure("Rook")(0, (7, 1)),
        ]
        self.game_board[6] = [
            FigureFactory.build_figure("Rook")(1, (0, 6)),
            FigureFactory.build_figure("Rook")(1, (1, 6)),
            FigureFactory.build_figure("Rook")(1, (2, 6)),
            FigureFactory.build_figure("Rook")(1, (3, 6)),
            FigureFactory.build_figure("Rook")(1, (4, 6)),
            FigureFactory.build_figure("Rook")(1, (5, 6)),
            FigureFactory.build_figure("Rook")(1, (6, 6)),
            FigureFactory.build_figure("Rook")(1, (7, 6)),
        ]
        self.game_board[7] = [
            FigureFactory.build_figure("Rook")(1, (0, 7)),
            FigureFactory.build_figure("Knight")(1, (1, 7)),
            FigureFactory.build_figure("Bishop")(1, (2, 7)),
            FigureFactory.build_figure("Queen")(1, (3, 7)),
            FigureFactory.build_figure("King")(1, (4, 7)),
            FigureFactory.build_figure("Bishop")(1, (5, 7)),
            FigureFactory.build_figure("Knight")(1, (6, 7)),
            FigureFactory.build_figure("Rook")(1, (7, 7)),
        ]

        # init bot, player
        self.bot = Bot()
        self.player = Player()
        self.players = [self.bot, self.player]
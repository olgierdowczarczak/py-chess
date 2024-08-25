from user import Bot, Player
from figure import FigureFactory
from random import shuffle


class Game:

    def __init__(self) -> None:
        # init bot, player, mover
        self.bot = Bot()
        self.player = Player()
        self.mover = self.bot
        #users: list = [self.bot, self.player]
        #shuffle(users)
        #self.mover = users[0]

        # init board
        self.game_board: list = [[None for _ in range(8)] for _ in range(8)]
        self.game_board[0] = [
            FigureFactory.build_figure("Rook")(self.bot, (0, 0)),
            FigureFactory.build_figure("Knight")(self.bot, (1, 0)),
            FigureFactory.build_figure("Bishop")(self.bot, (2, 0)),
            FigureFactory.build_figure("Queen")(self.bot, (3, 0)),
            FigureFactory.build_figure("King")(self.bot, (4, 0)),
            FigureFactory.build_figure("Bishop")(self.bot, (5, 0)),
            FigureFactory.build_figure("Knight")(self.bot, (6, 0)),
            FigureFactory.build_figure("Rook")(self.bot, (7, 0)),
        ]
        self.game_board[1] = [
            FigureFactory.build_figure("Pawn")(self.bot, (0, 1)),
            FigureFactory.build_figure("Pawn")(self.bot, (1, 1)),
            FigureFactory.build_figure("Pawn")(self.bot, (2, 1)),
            FigureFactory.build_figure("Pawn")(self.bot, (3, 1)),
            FigureFactory.build_figure("Pawn")(self.bot, (4, 1)),
            FigureFactory.build_figure("Pawn")(self.bot, (5, 1)),
            FigureFactory.build_figure("Pawn")(self.bot, (6, 1)),
            FigureFactory.build_figure("Pawn")(self.bot, (7, 1)),
        ]
        self.game_board[6] = [
            FigureFactory.build_figure("Pawn")(self.player, (0, 6)),
            FigureFactory.build_figure("Pawn")(self.player, (1, 6)),
            FigureFactory.build_figure("Pawn")(self.player, (2, 6)),
            FigureFactory.build_figure("Pawn")(self.player, (3, 6)),
            FigureFactory.build_figure("Pawn")(self.player, (4, 6)),
            FigureFactory.build_figure("Pawn")(self.player, (5, 6)),
            FigureFactory.build_figure("Pawn")(self.player, (6, 6)),
            FigureFactory.build_figure("Pawn")(self.player, (7, 6)),
        ]
        self.game_board[7] = [
            FigureFactory.build_figure("Rook")(self.player, (0, 7)),
            FigureFactory.build_figure("Knight")(self.player, (1, 7)),
            FigureFactory.build_figure("Bishop")(self.player, (2, 7)),
            FigureFactory.build_figure("Queen")(self.player, (3, 7)),
            FigureFactory.build_figure("King")(self.player, (4, 7)),
            FigureFactory.build_figure("Bishop")(self.player, (5, 7)),
            FigureFactory.build_figure("Knight")(self.player, (6, 7)),
            FigureFactory.build_figure("Rook")(self.player, (7, 7)),
        ]

        # sign figures to users
        self.bot.user_figures = self.game_board[0] + self.game_board[1]
        self.player.user_figures = self.game_board[6] + self.game_board[7]

        # game loop
        self.game_status: int = -1
        while self.game_status == -1:
            self.game_status = self.check_game()
            self.mover = self.bot if self.mover == self.player else self.player
            break
    
        if self.game_status == 2: 
            print("Draw")
        else: 
            print(f"{self.player if self.game_status else self.bot} wins!")

    def check_game(self) -> int:
        game_result: int = self.check_board()
        if not game_result == -1:
            return game_result

        return (self.bot if self.mover == self.bot else self.player).user_move(self)

    def check_board(self) -> int:
        return -1
    
    def check_move(self, figure_position: tuple, direction_position: list, move: int):
        row, col = figure_position[0], figure_position[1]
        for _ in range(move + 1):
            row += direction_position[0]
            col += direction_position[1]
        
        if row < 0 or row > 7 or col < 0 or col > 7:
            return 0
        
        position_object = self.game_board[row][col]
        return position_object
    
    def show_board(self) -> None:
        for row in self.game_board:
            print(row)
from user import Bot, Player
from figure import FigureFactory
from random import shuffle


class Game:

    def __init__(self) -> None:
        # init bot, player, mover
        self.bot = Bot()
        self.player = Player()
        self.mover = self.bot
        users_list: list = [self.bot, self.player]
        shuffle(users_list)
        #self.mover = users[0]

        # init board
        self.game_board: list = [[None for _ in range(8)] for _ in range(8)]
        self.game_board[0] = [
            FigureFactory.build_figure("Rook")(users_list[0], (0, 0)),
            FigureFactory.build_figure("Knight")(users_list[0], (1, 0)),
            FigureFactory.build_figure("Bishop")(users_list[0], (2, 0)),
            FigureFactory.build_figure("Queen")(users_list[0], (3, 0)),
            FigureFactory.build_figure("King")(users_list[0], (4, 0)),
            FigureFactory.build_figure("Bishop")(users_list[0], (5, 0)),
            FigureFactory.build_figure("Knight")(users_list[0], (6, 0)),
            FigureFactory.build_figure("Rook")(users_list[0], (7, 0)),
        ]
        self.game_board[1] = [
            FigureFactory.build_figure("Pawn")(users_list[0], (0, 1)),
            FigureFactory.build_figure("Pawn")(users_list[0], (1, 1)),
            FigureFactory.build_figure("Pawn")(users_list[0], (2, 1)),
            FigureFactory.build_figure("Pawn")(users_list[0], (3, 1)),
            FigureFactory.build_figure("Pawn")(users_list[0], (4, 1)),
            FigureFactory.build_figure("Pawn")(users_list[0], (5, 1)),
            FigureFactory.build_figure("Pawn")(users_list[0], (6, 1)),
            FigureFactory.build_figure("Pawn")(users_list[0], (7, 1)),
        ]
        self.game_board[6] = [
            FigureFactory.build_figure("Pawn")(users_list[1], (0, 6)),
            FigureFactory.build_figure("Pawn")(users_list[1], (1, 6)),
            FigureFactory.build_figure("Pawn")(users_list[1], (2, 6)),
            FigureFactory.build_figure("Pawn")(users_list[1], (3, 6)),
            FigureFactory.build_figure("Pawn")(users_list[1], (4, 6)),
            FigureFactory.build_figure("Pawn")(users_list[1], (5, 6)),
            FigureFactory.build_figure("Pawn")(users_list[1], (6, 6)),
            FigureFactory.build_figure("Pawn")(users_list[1], (7, 6)),
        ]
        self.game_board[7] = [
            FigureFactory.build_figure("Rook")(users_list[1], (0, 7)),
            FigureFactory.build_figure("Knight")(users_list[1], (1, 7)),
            FigureFactory.build_figure("Bishop")(users_list[1], (2, 7)),
            FigureFactory.build_figure("Queen")(users_list[1], (3, 7)),
            FigureFactory.build_figure("King")(users_list[1], (4, 7)),
            FigureFactory.build_figure("Bishop")(users_list[1], (5, 7)),
            FigureFactory.build_figure("Knight")(users_list[1], (6, 7)),
            FigureFactory.build_figure("Rook")(users_list[1], (7, 7)),
        ]

        # sign figures to users
        users_list[0].user_figures = self.game_board[0] + self.game_board[1]
        users_list[1].user_figures = self.game_board[6] + self.game_board[7]

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
        for _ in range(move+1):
            row += direction_position[0]
            col += direction_position[1]
        
        if row < 0 or row > 7 or col < 0 or col > 7:
            return 0
        
        return self.game_board[col][row]
    
    def show_board(self) -> None:
        for row in self.game_board:
            print(row)
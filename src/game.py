import pygame
from user import Bot, Player
from figure import *
from random import shuffle


class Game:

    def __init__(self) -> None:
        # init pygame
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Chess")
        self.square_size: int = 600 // 8
        self.place_clicked: tuple = (False, 0, 0)

        # init bot, player, mover
        self.bot = Bot()
        self.player = Player()
        self.mover = self.bot
        users_list: list = [self.bot, self.player]
        #shuffle(users_list)
        #self.mover = users[0]

        # init board
        self.game_board: list = [[None for _ in range(8)] for _ in range(8)]
        self.game_board[0] = [
            FigureFactory.build_figure("Rook")(users_list[0], (0, 0), pygame.transform.scale(pygame.image.load(Rook.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Knight")(users_list[0], (1, 0), pygame.transform.scale(pygame.image.load(Knight.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Bishop")(users_list[0], (2, 0), pygame.transform.scale(pygame.image.load(Bishop.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Queen")(users_list[0], (3, 0), pygame.transform.scale(pygame.image.load(Queen.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("King")(users_list[0], (4, 0), pygame.transform.scale(pygame.image.load(King.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Bishop")(users_list[0], (5, 0), pygame.transform.scale(pygame.image.load(Bishop.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Knight")(users_list[0], (6, 0), pygame.transform.scale(pygame.image.load(Knight.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Rook")(users_list[0], (7, 0), pygame.transform.scale(pygame.image.load(Rook.figure_files[0]), (self.square_size, self.square_size))),
        ]
        self.game_board[1] = [
            FigureFactory.build_figure("Pawn")(users_list[0], (0, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[0], (1, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[0], (2, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[0], (3, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[0], (4, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[0], (5, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[0], (6, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[0], (7, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
        ]
        self.game_board[6] = [
            FigureFactory.build_figure("Pawn")(users_list[1], (0, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[1], (1, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[1], (2, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[1], (3, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[1], (4, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[1], (5, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[1], (6, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(users_list[1], (7, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
        ]
        self.game_board[7] = [
            FigureFactory.build_figure("Rook")(users_list[1], (0, 7), pygame.transform.scale(pygame.image.load(Rook.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Knight")(users_list[1], (1, 7), pygame.transform.scale(pygame.image.load(Knight.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Bishop")(users_list[1], (2, 7), pygame.transform.scale(pygame.image.load(Bishop.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Queen")(users_list[1], (3, 7), pygame.transform.scale(pygame.image.load(Queen.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("King")(users_list[1], (4, 7), pygame.transform.scale(pygame.image.load(King.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Bishop")(users_list[1], (5, 7), pygame.transform.scale(pygame.image.load(Bishop.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Knight")(users_list[1], (6, 7), pygame.transform.scale(pygame.image.load(Knight.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Rook")(users_list[1], (7, 7), pygame.transform.scale(pygame.image.load(Rook.figure_files[1]), (self.square_size, self.square_size))),
        ]

        # sign figures to users
        users_list[0].user_figures = self.game_board[0] + self.game_board[1]
        users_list[1].user_figures = self.game_board[7] + self.game_board[6]

        # draw board
        self.draw_board()
        self.update_board()
        pygame.display.flip()

        # game loop
        self.game_status: int = -1
        while self.game_status:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_status = 0
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row = x // self.square_size
                    col = y // self.square_size
                    self.place_clicked = (True, row, col)

            # refresh screen
            self.draw_board()

            self.game_status = self.check_game()
            if self.game_status == -2: continue # show place to set figure
            if self.game_status == -1: continue

            self.mover = self.bot if self.mover == self.player else self.player
            self.place_clicked = (False, 0, 0)

            # refresh screen
            self.update_board()
            pygame.display.flip()

        if self.game_status == 0: print("None Result")
        elif self.game_status == -1: print("Draw")
        else: print(f"{self.player if self.game_status else self.bot} wins!")

        pygame.quit()

    def check_game(self) -> int:
        # game_result: int = self.check_board()
        # if not game_result == -1:
        #     return game_result

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

    def draw_board(self) -> None:
        # draw board
        color: tuple = ()
        for row in range(8):
            for col in range(8):
                if (row + col) % 2: color = (0, 0, 0)
                else: color = (255, 255, 255)
                pygame.draw.rect(self.screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

    def update_board(self) -> None:
        # update board
        for row in self.game_board:
            for place in row:
                if place is None: continue
                self.screen.blit(place.figure_image, (place.figure_position[0] * self.square_size, place.figure_position[1] * self.square_size))

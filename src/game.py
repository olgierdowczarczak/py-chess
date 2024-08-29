import pygame
from user import *
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
        self.users_list: list = [self.bot, self.player]
        shuffle(self.users_list)
        self.mover = self.users_list[0]

        # init board
        self.game_board: list = [[None for _ in range(8)] for _ in range(8)]
        self.game_board[0] = [
            FigureFactory.build_figure("Rook")(self.users_list[0], (0, 0), pygame.transform.scale(pygame.image.load(Rook.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Knight")(self.users_list[0], (1, 0), pygame.transform.scale(pygame.image.load(Knight.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Bishop")(self.users_list[0], (2, 0), pygame.transform.scale(pygame.image.load(Bishop.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Queen")(self.users_list[0], (3, 0), pygame.transform.scale(pygame.image.load(Queen.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("King")(self.users_list[0], (4, 0), pygame.transform.scale(pygame.image.load(King.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Bishop")(self.users_list[0], (5, 0), pygame.transform.scale(pygame.image.load(Bishop.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Knight")(self.users_list[0], (6, 0), pygame.transform.scale(pygame.image.load(Knight.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Rook")(self.users_list[0], (7, 0), pygame.transform.scale(pygame.image.load(Rook.figure_files[0]), (self.square_size, self.square_size))),
        ]
        self.game_board[1] = [
            FigureFactory.build_figure("Pawn")(self.users_list[0], (0, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[0], (1, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[0], (2, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[0], (3, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[0], (4, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[0], (5, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[0], (6, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[0], (7, 1), pygame.transform.scale(pygame.image.load(Pawn.figure_files[0]), (self.square_size, self.square_size))),
        ]
        self.game_board[6] = [
            FigureFactory.build_figure("Pawn")(self.users_list[1], (0, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[1], (1, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[1], (2, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[1], (3, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[1], (4, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[1], (5, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[1], (6, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Pawn")(self.users_list[1], (7, 6), pygame.transform.scale(pygame.image.load(Pawn.figure_files[1]), (self.square_size, self.square_size))),
        ]
        self.game_board[7] = [
            FigureFactory.build_figure("Rook")(self.users_list[1], (0, 7), pygame.transform.scale(pygame.image.load(Rook.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Knight")(self.users_list[1], (1, 7), pygame.transform.scale(pygame.image.load(Knight.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Bishop")(self.users_list[1], (2, 7), pygame.transform.scale(pygame.image.load(Bishop.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Queen")(self.users_list[1], (3, 7), pygame.transform.scale(pygame.image.load(Queen.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("King")(self.users_list[1], (4, 7), pygame.transform.scale(pygame.image.load(King.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Bishop")(self.users_list[1], (5, 7), pygame.transform.scale(pygame.image.load(Bishop.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Knight")(self.users_list[1], (6, 7), pygame.transform.scale(pygame.image.load(Knight.figure_files[1]), (self.square_size, self.square_size))),
            FigureFactory.build_figure("Rook")(self.users_list[1], (7, 7), pygame.transform.scale(pygame.image.load(Rook.figure_files[1]), (self.square_size, self.square_size))),
        ]

        # sign figures to users
        self.users_list[0].user_figures = self.game_board[0] + self.game_board[1]
        self.users_list[1].user_figures = self.game_board[7] + self.game_board[6]

        self.draw_board() # draw board
        self.update_figures() # draw figures
        pygame.display.flip() # refresh screen

        # game loop
        self.game_loop: bool = True
        self.game_status: int = -1

        while self.game_loop:
            # self.check_game()

            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # press quit
                    self.game_status = 2
                    self.game_loop = False
                    break

                if event.type == pygame.MOUSEBUTTONDOWN: # press button
                    x, y = pygame.mouse.get_pos()
                    self.place_clicked = (True, x // self.square_size, y // self.square_size)

            if self.game_loop is False: break

            self.draw_board() # draw board

            # pre move
            self.game_status = (self.bot if self.mover == self.bot else self.player).pre_user_move(self) # make move
            if self.game_status == -2: continue # wrong move, try again
            elif self.game_status == -3:
                self.place_clicked = (False, 0, 0) # reset clicked place
                continue # wait for move
            
            # post move
            self.mover = self.bot if self.mover == self.player else self.player # change mover
            self.place_clicked = (False, 0, 0) # reset clicked place
            
            # update pawn moves
            if self.bot.first_move is True and self.player.first_move is True:
                Pawn.figure_move = 1

            # update board
            self.update_figures() # draw figures
            pygame.display.flip() # refresh screen

        if self.game_status == 2: print("None Result")
        elif self.game_status == 3: print("Draw")
        else: print(f"{self.player if self.game_status else self.bot} wins!")
        pygame.quit()

    def check_board(self) -> int:
        return -1
    
    def is_place_out_of_board(self, position: tuple) -> bool:
        return True if position[0] < 0 or position[0] > 7 or position[1] < 0 or position[1] > 7 else False
    
    def make_move(self, figure, new_position: tuple) -> None:
        start_position: tuple = figure.figure_position
        self.game_board[start_position[1]][start_position[0]] = None
        figure.figure_position = new_position
        self.game_board[new_position[1]][new_position[0]] = figure

    def draw_board(self) -> None:
        # draw board
        color: tuple = ()
        for row in range(8):
            for col in range(8):
                if (row + col) % 2: color = (0, 0, 0)
                else: color = (255, 255, 255)
                pygame.draw.rect(self.screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

    def update_figures(self) -> None:
        # update board
        for row in self.game_board:
            for figure in row:
                if figure is None: continue
                self.screen.blit(figure.figure_image, (figure.figure_position[0] * self.square_size, figure.figure_position[1] * self.square_size))
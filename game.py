import os
import random
import sys

from board import Board
from config import EXIT, MOVES
from exceptions import ValidMoveNotExists, GameOver, NotValidMove
from figures import Line, LFigure, JFigure, Lightning, Square
from utils import get_char


class Game:
    AVAILABLE_FIGURES = [Line, LFigure, JFigure, Lightning, Square]
    figure = None
    correct_move = False
    user_move = None
    message = None
    new_figure_needed = False
    keyboard_instruction = """
    (a) - left
    (d) - right
    (w) - rotate right
    (s) - rotate left
    (e)xit"""

    def __init__(self):
        self.board = Board()
        self.init_game()

    def init_game(self):
        self.clear_screen()
        self.set_figure()
        self.board.add(self.figure.fields)
        self.board.draw()

    def get_figure(self):
        return random.choice(self.AVAILABLE_FIGURES)()

    def set_figure(self):
        self.check_move_possibility()

        self.figure = self.get_figure()
        self.new_figure_needed = False

    def check_touching_edge(self):
        fields = self.figure.fields
        board = self.board.board

        for field in fields:
            check = board[field['y'] + 1][field['x']]

            exists_in_fields = False
            for now in fields:
                if now['x'] == field['x'] and now['y'] == field['y'] + 1:
                    exists_in_fields = True
            if check == '*' and not exists_in_fields:
                raise ValidMoveNotExists

    def check_move_possibility(self):
        move_possible = self.board.is_available

        if not move_possible:
            raise GameOver

    def check_board(self, new_figure=False):
        current_board = self.board.board

        if new_figure:
            fields_to_check = self.figure.fields

            valid_move = not any(current_board[field['y']][field['x']] == '*' for field in fields_to_check)
            if not valid_move:
                raise GameOver

        if not new_figure:
            above_fields = self.figure.new_fields_before_down
            fields_to_check = [self.figure.new_fields, above_fields]

            for fields in fields_to_check:
                for new_field in fields:
                    try:
                        field_to_check = current_board[new_field['y']][new_field['x']]
                    except IndexError:
                        raise NotValidMove

                    exists_in_previous_move = False
                    for old_field in self.figure.fields:
                        if old_field['x'] == new_field['x'] and old_field['y'] == new_field['y']:
                            exists_in_previous_move = True
                    if field_to_check == '*' and not exists_in_previous_move:
                        raise NotValidMove

    def check_other_moves(self):
        exists_valid_move = False
        # we want to check if the other user possible moves are valid
        moves = MOVES.copy()
        moves.remove(self.user_move)
        for move in moves:
            self.figure.set_fields(move)
            try:
                self.check_board()
            except NotValidMove as ex:
                self.message = ex.message
            else:
                exists_valid_move = True

        if not exists_valid_move:
            raise ValidMoveNotExists

    def print_info(self):
        print(self.keyboard_instruction)
        if self.message:
            print(self.message)
            self.message = None

    def prepare_next_move(self):
        self.board.delete(self.figure.fields)
        self.figure.update()
        self.board.add(self.figure.fields)

    def set_no_valid_move_state(self):
        self.new_figure_needed = True
        self.message = None

    def get_board_state(self):
        self.display()
        self.check_touching_edge()

    @staticmethod
    def clear_screen():
        os.system('cls')

    def reset_move_state(self):
        self.user_move = None
        self.correct_move = False

    def display(self):
        self.clear_screen()
        self.board.draw()

    def exit(self):
        self.display()
        print(self.message)
        sys.exit()

    def start(self):

        while True:

            while not self.new_figure_needed:
                self.reset_move_state()

                while not self.correct_move:
                    self.print_info()
                    self.user_move = get_char()

                    if self.user_move == EXIT:
                        sys.exit()

                    try:
                        if self.user_move in MOVES:
                            self.correct_move = True

                            self.figure.set_fields(self.user_move)

                            try:
                                self.check_board()
                                self.prepare_next_move()
                            except NotValidMove as nvm:
                                self.message = nvm.message
                                self.check_other_moves()

                        self.get_board_state()

                    except ValidMoveNotExists:
                        self.set_no_valid_move_state()

            try:
                self.set_figure()
                self.check_board(new_figure=True)
                self.board.add(self.figure.fields)
                self.get_board_state()

            except ValidMoveNotExists:
                self.new_figure_needed = True
                self.message = None

            except GameOver as go:
                self.message = go.message
                self.board.add(self.figure.fields)
                self.exit()
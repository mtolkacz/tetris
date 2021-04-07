import random

from config import ROTATE_RIGHT, ROTATE_LEFT, RIGHT, LEFT


class Figure:
    scope = None
    fields = []
    previous_fields = []
    new_fields = []
    new_fields_before_down = []

    @staticmethod
    def get_starting_position(x):
        pass

    def get_new_fields_before_down(self):
        above_fields = []
        for field in self.new_fields:
            above_fields.append({
                'x': field['x'],
                'y': field['y'] - 1 if field['y'] > 0 else 0,
            })
        return above_fields

    def get_starting_x(self):
        x = random.randrange(self.scope['left'], self.scope['right'] + 1)
        return x

    def rotate_right(self):
        pass

    def rotate_left(self):
        pass

    def left(self):
        self.new_fields.append(
            {
                'x': self.fields[0]['x'] - 1,
                'y': self.fields[0]['y'] + 1
            })
        self.new_fields.append(
            {
                'x': self.fields[1]['x'] - 1,
                'y': self.fields[1]['y'] + 1
            })
        self.new_fields.append(
            {
                'x': self.fields[2]['x'] - 1,
                'y': self.fields[2]['y'] + 1
            })
        self.new_fields.append(
            {
                'x': self.fields[3]['x'] - 1,
                'y': self.fields[3]['y'] + 1
            })

    def right(self):
        # fields = []
        self.new_fields.append(
            {
                'x': self.fields[0]['x'] + 1,
                'y': self.fields[0]['y'] + 1
            })
        self.new_fields.append(
            {
                'x': self.fields[1]['x'] + 1,
                'y': self.fields[1]['y'] + 1
            })
        self.new_fields.append(
            {
                'x': self.fields[2]['x'] + 1,
                'y': self.fields[2]['y'] + 1
            })
        self.new_fields.append(
            {
                'x': self.fields[3]['x'] + 1,
                'y': self.fields[3]['y'] + 1
            })
        # return fields

    def set_fields(self, move):

        self.new_fields = []

        if move == ROTATE_RIGHT:
            self.rotate_right()

        if move == ROTATE_LEFT:
            self.rotate_left()

        if move == RIGHT:
            self.right()

        if move == LEFT:
            self.left()

        self.new_fields_before_down = self.get_new_fields_before_down()

    def update(self):
        if self.new_fields:
            self.previous_fields = self.fields
            self.fields = self.new_fields
            self.new_fields = []


class VariantFigure(Figure):
    # Variants of the figure
    NORMAL = 1
    RIGHT = 2
    LEFT = 3
    UP_DOWN = 4

    variant = NORMAL


class Line(Figure):
    scope = {'left': 1, 'right': 15}
    vertically = True

    def __init__(self):
        x = self.get_starting_x()
        self.fields = self.get_starting_position(x)

    @staticmethod
    def get_starting_position(x):
        return [{'x': x, 'y': 0, }, {'x': x, 'y': 1, }, {'x': x, 'y': 2, }, {'x': x, 'y': 3, }]

    def rotate_right(self):
        if self.vertically:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] - 1,
                    'y': self.fields[0]['y'] + 4
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 3
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] + 1,
                    'y': self.fields[2]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] + 2,
                    'y': self.fields[3]['y'] + 1
                })

        else:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] + 2,
                    'y': self.fields[0]['y'] - 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'] + 1,
                    'y': self.fields[1]['y'] - 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'],
                    'y': self.fields[2]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] - 1,
                    'y': self.fields[3]['y'] + 1
                })

        self.vertically = not self.vertically

    def rotate_left(self):
        if self.vertically:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] - 2,
                    'y': self.fields[0]['y'] + 4
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'] - 1,
                    'y': self.fields[1]['y'] + 3
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'],
                    'y': self.fields[2]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] + 1,
                    'y': self.fields[3]['y'] + 1
                })
        else:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] + 1,
                    'y': self.fields[0]['y'] - 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] - 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] - 1,
                    'y': self.fields[2]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] - 2,
                    'y': self.fields[3]['y'] + 1
                })

        self.vertically = not self.vertically


class LFigure(VariantFigure):
    scope = {'left': 1, 'right': 17}

    def __init__(self):
        x = self.get_starting_x()
        self.fields = self.get_starting_position(x)

    @staticmethod
    def get_starting_position(x):
        return [{'x': x, 'y': 0, }, {'x': x, 'y': 1, }, {'x': x, 'y': 2, }, {'x': x + 1, 'y': 2, }]

    def rotate_right(self):
        if self.variant == LFigure.NORMAL:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] + 2,
                    'y': self.fields[0]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'] + 1,
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'],
                    'y': self.fields[2]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] - 1,
                    'y': self.fields[3]['y'] + 1
                })
            self.variant = LFigure.RIGHT

        elif self.variant == LFigure.RIGHT:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] - 1,
                    'y': self.fields[0]['y'] + 3
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] - 1,
                    'y': self.fields[2]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'],
                    'y': self.fields[3]['y']
                })
            self.variant = LFigure.UP_DOWN

        elif self.variant == LFigure.LEFT:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] + 1,
                    'y': self.fields[0]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] - 1,
                    'y': self.fields[2]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'],
                    'y': self.fields[3]['y'] + 3
                })
            self.variant = LFigure.NORMAL

        elif self.variant == LFigure.UP_DOWN:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] - 1,
                    'y': self.fields[0]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] + 1,
                    'y': self.fields[2]['y'] + 3
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] + 2,
                    'y': self.fields[3]['y'] + 2
                })
            self.variant = LFigure.LEFT

    def rotate_left(self):
        if self.variant == LFigure.NORMAL:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] - 1,
                    'y': self.fields[0]['y'] + 3
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] + 1,
                    'y': self.fields[2]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'],
                    'y': self.fields[3]['y']
                })
            self.variant = LFigure.LEFT

        elif self.variant == LFigure.RIGHT:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] - 2,
                    'y': self.fields[0]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'] - 1,
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'],
                    'y': self.fields[2]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] + 1,
                    'y': self.fields[3]['y'] + 1
                })
            self.variant = LFigure.NORMAL

        elif self.variant == LFigure.LEFT:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] + 2,
                    'y': self.fields[0]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'] + 1,
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'],
                    'y': self.fields[2]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] - 1,
                    'y': self.fields[3]['y'] + 1
                })
            self.variant = LFigure.UP_DOWN

        elif self.variant == LFigure.UP_DOWN:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] + 1,
                    'y': self.fields[0]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] - 1,
                    'y': self.fields[2]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'],
                    'y': self.fields[3]['y'] + 3
                })
            self.variant = LFigure.RIGHT


class JFigure(VariantFigure):
    scope = {'left': 2, 'right': 18}

    def __init__(self):
        x = self.get_starting_x()
        self.fields = self.get_starting_position(x)

    @staticmethod
    def get_starting_position(x):
        return [{'x': x, 'y': 0, }, {'x': x, 'y': 1, }, {'x': x, 'y': 2, }, {'x': x - 1, 'y': 2, }]

    def rotate_right(self):
        if self.variant == JFigure.NORMAL:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] + 1,
                    'y': self.fields[0]['y'] + 3
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] - 1,
                    'y': self.fields[2]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'],
                    'y': self.fields[3]['y']
                })
            self.variant = JFigure.RIGHT

        elif self.variant == JFigure.RIGHT:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] - 2,
                    'y': self.fields[0]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'] - 1,
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'],
                    'y': self.fields[2]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] + 1,
                    'y': self.fields[3]['y'] + 1
                })
            self.variant = JFigure.UP_DOWN

        elif self.variant == JFigure.LEFT:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] + 2,
                    'y': self.fields[0]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'] + 1,
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'],
                    'y': self.fields[2]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] - 1,
                    'y': self.fields[3]['y'] + 1
                })
            self.variant = JFigure.NORMAL

        elif self.variant == JFigure.UP_DOWN:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] - 1,
                    'y': self.fields[0]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] + 1,
                    'y': self.fields[2]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'],
                    'y': self.fields[3]['y'] + 3
                })
            self.variant = JFigure.LEFT

    def rotate_left(self):
        if self.variant == JFigure.NORMAL:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] - 1,
                    'y': self.fields[0]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] + 1,
                    'y': self.fields[2]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] + 2,
                    'y': self.fields[3]['y'] + 1
                })
            self.variant = JFigure.LEFT

        elif self.variant == JFigure.RIGHT:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] - 1,
                    'y': self.fields[0]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] + 1,
                    'y': self.fields[2]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'],
                    'y': self.fields[3]['y'] + 3
                })
            self.variant = JFigure.NORMAL

        elif self.variant == JFigure.LEFT:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] + 1,
                    'y': self.fields[0]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] - 1,
                    'y': self.fields[2]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'],
                    'y': self.fields[3]['y'] - 1
                })
            self.variant = JFigure.UP_DOWN

        elif self.variant == JFigure.UP_DOWN:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] + 1,
                    'y': self.fields[0]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] - 1,
                    'y': self.fields[2]['y'] + 3
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] - 2,
                    'y': self.fields[3]['y'] + 2
                })
            self.variant = JFigure.RIGHT


class Lightning(VariantFigure):
    scope = {'left': 2, 'right': 17}

    def __init__(self):
        x = self.get_starting_x()
        self.fields = self.get_starting_position(x)

    @staticmethod
    def get_starting_position(x):
        return [{'x': x, 'y': 0, }, {'x': x, 'y': 1, }, {'x': x - 1, 'y': 1, }, {'x': x - 1, 'y': 2, }]

    def rotate(self):
        if self.variant == Lightning.NORMAL:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] - 1,
                    'y': self.fields[0]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'],
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'] + 1,
                    'y': self.fields[2]['y'] + 2
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] + 2,
                    'y': self.fields[3]['y'] + 1
                })
            self.variant = Lightning.LEFT

        elif self.variant == Lightning.LEFT:
            self.new_fields.append(
                {
                    'x': self.fields[0]['x'] + 2,
                    'y': self.fields[0]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[1]['x'] + 1,
                    'y': self.fields[1]['y'] + 1
                })
            self.new_fields.append(
                {
                    'x': self.fields[2]['x'],
                    'y': self.fields[2]['y']
                })
            self.new_fields.append(
                {
                    'x': self.fields[3]['x'] - 1,
                    'y': self.fields[3]['y'] + 1
                })
            self.variant = Lightning.NORMAL

    def rotate_left(self):
        self.rotate()

    def rotate_right(self):
        self.rotate()


class Square(VariantFigure):
    scope = {'left': 2, 'right': 18}

    def __init__(self):
        x = self.get_starting_x()
        self.fields = self.get_starting_position(x)

    @staticmethod
    def get_starting_position(x):
        return [{'x': x, 'y': 0, }, {'x': x + 1, 'y': 0, }, {'x': x, 'y': 1, }, {'x': x + 1, 'y': 1, }]

    def rotate(self):
        self.new_fields.append(
            {
                'x': self.fields[0]['x'],
                'y': self.fields[0]['y'] + 1
            })
        self.new_fields.append(
            {
                'x': self.fields[1]['x'],
                'y': self.fields[1]['y'] + 1
            })
        self.new_fields.append(
            {
                'x': self.fields[2]['x'],
                'y': self.fields[2]['y'] + 1
            })
        self.new_fields.append(
            {
                'x': self.fields[3]['x'],
                'y': self.fields[3]['y'] + 1
            })

    def rotate_right(self):
        self.rotate()

    def rotate_left(self):
        self.rotate()
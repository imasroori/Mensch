# 1st Project on MaktabSharif,Maktab42, Code by Iman Masroori
""" In this Module logic of game are designed"""
import random


class Piece:
    def __init__(self):
        pass

    def move(self, start, end, length):
        pass


class Gbox():
    green_step = [7, 21, 20, 19, 12, 5, 4, 3, 10, 17, 16, 15, 22, 29, 30, 31, 38, 45, 46, 47, 40, 33, 34, 35, 28, 27]
    counter_all_piece = 0

    def __init__(self, id=green_step[0], step=None, state=None):
        self.counter_all_piece += 1
        self.id = id
        self.step = step
        self.state = state
        self.counter_all_piece += 1
        if self.counter_all_piece > 4:
            raise Exception("no extra")

    def at_home(self):
        if self.id == self.green_step[-1]:
            return True
        else:
            return False

    def in_game(self):
        if self.id != self.green_step[0] and self.id != self.green_step[-1]:
            return True
        else:
            return False

    def out_game(self):
        if self.id == self.green_step[0]:
            return True
        else:
            return False

    def __del__(self):
        del self


class Ybox():
    yellow_step = [49, 47, 40, 33, 34, 35, 28, 21, 20, 19, 12, 5, 4, 3, 10, 17, 16, 15, 22, 29, 30, 31, 38, 45, 46, 39]

    counter_all_piece = 0

    def __init__(self, idd=yellow_step[0], step=None, state=None):
        # self.counter_all_piece += 1
        self.idd = idd
        self.step = step
        self.state = state
        self.counter_all_piece += 1
        print("num blues", self.counter_all_piece)
        if self.counter_all_piece > 4:
            raise Exception("no extra")

    def at_home(self):
        if self.idd == self.yellow_step[-1]:
            return True
        else:
            return False

    def in_game(self):
        if self.idd != self.yellow_step[0] and self.idd != self.yellow_step[-1]:
            return True
        else:
            return False

    def out_game(self):
        if self.idd == self.yellow_step[0]:
            return True
        else:
            return False

    def move(self):

        return self.yellow_step[self.yellow_step.index(self.idd) + self.step]

    def __del__(self):
        del self


class Bbox():
    blue_step = [1, 3, 10, 17, 16, 15, 22, 29, 30, 31, 38, 45, 46, 47, 40, 33, 34, 35, 28, 21, 20, 19, 12, 5, 4, 11]
    counter_all_piece = 0

    def __init__(self, idd=blue_step[0], step=None, state=None):
        # self.counter_all_piece += 1
        self.idd = idd
        self.step = step
        self.state = state
        self.counter_all_piece += 1
        print("num blues", self.counter_all_piece)
        if self.counter_all_piece > 4:
            raise Exception("no extra")

    def at_home(self):
        if self.idd == self.blue_step[-1]:
            return True
        else:
            return False

    def in_game(self):
        if self.idd != self.blue_step[0] and self.idd != self.blue_step[-1]:
            return True
        else:
            return False

    def out_game(self):
        if self.idd == self.blue_step[0]:
            return True
        else:
            return False

    def move(self):

        return self.blue_step[self.blue_step.index(self.idd) + self.step]

    def __del__(self):
        del self


class Rbox():
    red_step = [43, 29, 30, 31, 38, 45, 46, 47, 40, 33, 34, 35, 28, 21, 20, 19, 12, 5, 4, 3, 10, 17, 16, 15, 22, 23]
    counter_all_piece = 0

    def __init__(self, idd=red_step[0], step=None, state=None):
        self.idd = idd
        self.step = step
        self.state = state
        self.counter_all_piece += 1
        print("num blues", Bbox.counter_all_piece)
        if self.counter_all_piece > 4:
            raise Exception("no extra")

    def at_home(self):
        if self.idd == self.red_step[-1]:
            return True
        else:
            return False

    def in_game(self):
        if self.idd != self.red_step[0] and self.idd != self.red_step[-1]:
            return True
        else:
            return False

    def out_game(self):
        if self.idd == self.red_step[0]:
            return True
        else:
            return False

    def move(self):

        return self.red_step[self.red_step.index(self.idd) + self.step]

    def __del__(self):
        del self


def turn():
    turn_list = iter([1, 2, 3, 4])
    return next(turn_list)


if __name__ == '__main__':
    print("ddd", turn())

    print(len(Bbox.blue_step), len(Rbox.red_step), len(Ybox.yellow_step), len(Gbox.green_step))
    list_circle_board = [0]
    print(Bbox(17, 1).move())

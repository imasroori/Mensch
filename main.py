# Mensch Game with Tkinter Module in Python, Code by Iman Masroori
import random


class Piece:
    def __init__(self):
        pass

    def move(self, start, end, length):
        pass


class gBox():
    all_count = 4

    def __init__(self):
        pass

    def at_home(self):
        pass

    def in_game(self):
        pass

    def out_game(self):
        pass


class yBox():
    def __init__(self):
        pass


class bBox():
    def __init__(self):
        pass


class rBox():
    def __init__(self):
        pass


def roll():
    return random.randint(1, 6)


def turn():
    turn_list = iter([1, 2, 3, 4])
    return next(turn_list)
print("ddd",turn())


list_circle_board = [0]
print(roll())

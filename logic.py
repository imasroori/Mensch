# 1st Project on MaktabSharif,Maktab42, Code by Iman Masroori
""" In this Module logic of game are designed"""
import random
import gui
import logging
from tkinter import *

AppLogger = logging.getLogger()
logging.basicConfig(
    format='[%(asctime)s] (%(filename)s:%(lineno)d) %(levelname)s: %(message)s', filename='info_ranking.log',
    level=logging.DEBUG)


def roll_dice(turn_player):
    if not AddPlayer.turn_player_list_logic:
        info_rank = Tk()
        App_Rank = gui.RankInfo(info_rank)
        info_rank.mainloop()
        return None
    else:
        x = turn_player % len(AddPlayer.turn_player_list_logic)
        roll_num_out = random.randint(1, 6)

        return roll_num_out


class AddPlayer:
    counter_player = 0
    turn_player = 0
    turn_player_list_logic = []
    blues_piece = []
    reds_piece = []
    yellows_piece = []
    greens_piece = []
    ranking = []

    def __init__(self, user, color):
        AddPlayer.counter_player += 1
        print('self.counter_player in AddPlayer is: ', self.counter_player, "AddPlayer.counter_player in AddPlayer is:",
              AddPlayer.counter_player)
        self.user = user
        self.color = color
        self.turn_player = 0
        self.turn_player_list_logic.append((self.user, self.color))
        print(f'(user,color) are ==> {self.turn_player_list_logic}')
        self.init_instance()

    def init_instance(self):
        if self.color == 'BLUE':
            AddPlayer.blues_piece = [Bbox() for _ in range(4)]
            print("BLUE Pieces Created!")

        if self.color == 'RED':
            AddPlayer.reds_piece = [Rbox() for _ in range(4)]
            print("RED Pieces Created!")

        if self.color == 'GREEN':
            AddPlayer.greens_piece = [Gbox() for _ in range(4)]
            print("GREEN Pieces Created!")

        if self.color == 'YELLOW':
            AddPlayer.yellows_piece = [Ybox() for _ in range(4)]
            print("YELLOW Pieces Created!")

        print(f"Counter of users is: {AddPlayer.counter_player}")


class Gbox:
    green_step = [7, 21, 20, 19, 12, 5, 4, 3, 10, 17, 16, 15, 22, 29, 30, 31, 38, 45, 46, 47, 40, 33, 34, 35, 28, 27]
    counter_all_piece = 0

    def __init__(self, idd=green_step[0]):
        self.idd = idd
        self.counter_all_piece += 1
        if self.counter_all_piece > 4:
            raise Exception("no extra")

    @staticmethod
    def at_home(greens_piece):
        flag_at_home = True
        for i in greens_piece:
            if i.idd != Gbox.green_step[-1]:
                flag_at_home = False
                return flag_at_home
            else:
                continue
        else:
            return flag_at_home

    @staticmethod
    def out_game(greens_piece):
        for i in greens_piece:
            if (i.idd != Gbox.green_step[0]) and (i.idd != Gbox.green_step[-1]):
                return False
            else:
                continue
        else:
            return True

    @staticmethod
    def move_check(piece):
        return piece in Gbox.green_step[1:len(Gbox.green_step) - 1]

    @staticmethod
    def overlap(lis=None):
        if lis is None:
            lis = AddPlayer.greens_piece
        c_lap = 1
        for i in range(1, len(lis)):
            if AddPlayer.greens_piece[i].idd == AddPlayer.greens_piece[i - 1].idd:
                c_lap += 1
        return c_lap


class Ybox:
    yellow_step = [49, 47, 40, 33, 34, 35, 28, 21, 20, 19, 12, 5, 4, 3, 10, 17, 16, 15, 22, 29, 30, 31, 38, 45, 46, 39]

    counter_all_piece = 0

    def __init__(self, idd=yellow_step[0]):
        self.idd = idd
        self.counter_all_piece += 1
        if self.counter_all_piece > 4:
            raise Exception("no extra")

    @staticmethod
    def at_home(yellows_piece):
        flag_at_home = True
        for i in yellows_piece:
            if i.idd != Ybox.yellow_step[-1]:
                flag_at_home = False
                return flag_at_home
            else:
                continue
        else:
            return flag_at_home

    @staticmethod
    def out_game(yellows_piece):
        for i in yellows_piece:
            if (i.idd != Ybox.yellow_step[0]) and (i.idd != Ybox.yellow_step[-1]):
                return False
            else:
                continue
        else:
            return True

    @staticmethod
    def move_check(piece):
        return piece in Ybox.yellow_step[1:len(Ybox.yellow_step) - 1]


class Bbox:
    blue_step = [1, 3, 10, 17, 16, 15, 22, 29, 30, 31, 38, 45, 46, 47, 40, 33, 34, 35, 28, 21, 20, 19, 12, 5, 4, 11]
    counter_all_piece = 0

    def __init__(self, idd=blue_step[0]):
        self.idd = idd
        self.counter_all_piece += 1
        if self.counter_all_piece > 4:
            raise Exception("no extra")

    @staticmethod
    def at_home(blues_piece):
        flag_at_home = True
        for i in blues_piece:
            if i.idd != Bbox.blue_step[-1]:
                flag_at_home = False
                return flag_at_home
            else:
                continue
        else:
            return flag_at_home

    @staticmethod
    def out_game(blues_piece):
        for i in blues_piece:
            if (i.idd != Bbox.blue_step[0]) and (i.idd != Bbox.blue_step[-1]):
                return False
            else:
                continue
        else:
            return True

    @staticmethod
    def move_check(piece):
        return piece in Bbox.blue_step[1:len(Bbox.blue_step) - 1]


class Rbox():
    red_step = [43, 29, 30, 31, 38, 45, 46, 47, 40, 33, 34, 35, 28, 21, 20, 19, 12, 5, 4, 3, 10, 17, 16, 15, 22, 23]
    counter_all_piece = 0

    def __init__(self, idd=red_step[0]):
        self.idd = idd
        self.counter_all_piece += 1
        if self.counter_all_piece > 4:
            raise Exception("no extra")

    @staticmethod
    def at_home(reds_piece):
        flag_at_home = True
        for i in reds_piece:
            if i.idd != Rbox.red_step[-1]:
                flag_at_home = False
                return flag_at_home
            else:
                continue
        else:
            return flag_at_home

    @staticmethod
    def out_game(reds_piece):
        for i in reds_piece:
            if (i.idd != Rbox.red_step[0]) and (i.idd != Rbox.red_step[-1]):
                return False
            else:
                continue
        else:
            return True

    @staticmethod
    def move_check(piece):
        return piece in Rbox.red_step[1:len(Rbox.red_step) - 1]


def win():
    if not AddPlayer.turn_player_list_logic:
        logging.info(str(AddPlayer.ranking))

        info_rank = Tk()
        App_Rank = gui.RankInfo(info_rank)
        info_rank.mainloop()


def killer_piece(id_logic, color):
    copy_list_player = AddPlayer.turn_player_list_logic.copy()
    for item in copy_list_player:
        if item[1] == color:
            copy_list_player.remove(item)
    killed_pieces = []
    for i in copy_list_player:
        if i[1] == 'BLUE':
            for j in AddPlayer.blues_piece:
                if j.idd == id_logic:
                    killed_pieces.append((AddPlayer.blues_piece.index(j), 'BLUE'))

        elif i[1] == 'RED':
            for j in AddPlayer.reds_piece:
                if j.idd == id_logic:
                    killed_pieces.append((AddPlayer.reds_piece.index(j), 'RED'))

        elif i[1] == 'YELLOW':
            for j in AddPlayer.yellows_piece:
                if j.idd == id_logic:
                    killed_pieces.append((AddPlayer.yellows_piece.index(j), 'YELLOW'))

        elif i[1] == 'GREEN':
            for j in AddPlayer.greens_piece:
                if j.idd == id_logic:
                    killed_pieces.append((AddPlayer.greens_piece.index(j), 'GREEN'))

    print("===>> killed_pieces", killed_pieces)
    return killed_pieces


def logic(id_gui, color, roll_num, p):
    try:
        if color == "BLUE":

            if (Bbox.move_check(id_gui)) and (id_gui == AddPlayer.blues_piece[p].idd):
                strt = AddPlayer.blues_piece[p].idd
                id_logic = Bbox.blue_step[Bbox.blue_step.index(strt) + roll_num]

                kill_id_color = killer_piece(id_logic, color)

                AddPlayer.blues_piece[p].idd = id_logic

                if Bbox.at_home(AddPlayer.blues_piece):
                    for item in AddPlayer.turn_player_list_logic:
                        if item[1] == 'BLUE':
                            AddPlayer.turn_player_list_logic.remove(item)
                            AddPlayer.ranking.append(item)

                return id_logic, 'BLUE', kill_id_color

            elif (not Bbox.move_check(id_gui)) and (id_gui == Bbox.blue_step[0]) and (
                    id_gui == AddPlayer.blues_piece[p].idd) and (roll_num == 6):
                id_logic = Bbox.blue_step[1]

                kill_id_color = killer_piece(id_logic, color)

                AddPlayer.blues_piece[p].idd = id_logic

                return id_logic, 'BLUE', kill_id_color

        elif color == "RED":

            if (Rbox.move_check(id_gui)) and (id_gui == AddPlayer.reds_piece[p].idd):
                strt = AddPlayer.reds_piece[p].idd
                id_logic = Rbox.red_step[Rbox.red_step.index(strt) + roll_num]

                kill_id_color = killer_piece(id_logic, color)

                AddPlayer.reds_piece[p].idd = id_logic

                if Rbox.at_home(AddPlayer.reds_piece):
                    for item in AddPlayer.turn_player_list_logic:
                        if item[1] == 'RED':
                            AddPlayer.turn_player_list_logic.remove(item)
                            AddPlayer.ranking.append(item)

                return id_logic, 'RED', kill_id_color

            elif (not Rbox.move_check(id_gui)) and (id_gui == Rbox.red_step[0]) and (
                    id_gui == AddPlayer.reds_piece[p].idd) and (roll_num == 6):
                id_logic = Rbox.red_step[1]

                kill_id_color = killer_piece(id_logic, color)

                AddPlayer.reds_piece[p].idd = id_logic

                return id_logic, 'RED', kill_id_color

        elif color == "GREEN":

            if (Gbox.move_check(id_gui)) and (id_gui == AddPlayer.greens_piece[p].idd):
                strt = AddPlayer.greens_piece[p].idd
                id_logic = Gbox.green_step[Gbox.green_step.index(strt) + roll_num]

                kill_id_color = killer_piece(id_logic, color)

                AddPlayer.greens_piece[p].idd = id_logic

                if Gbox.at_home(AddPlayer.greens_piece):
                    for item in AddPlayer.turn_player_list_logic:
                        if item[1] == 'GREEN':
                            AddPlayer.turn_player_list_logic.remove(item)
                            AddPlayer.ranking.append(item)

                return id_logic, 'GREEN', kill_id_color

            elif (not Gbox.move_check(id_gui)) and (id_gui == Gbox.green_step[0]) and (
                    id_gui == AddPlayer.greens_piece[p].idd) and (roll_num == 6):
                id_logic = Gbox.green_step[1]

                kill_id_color = killer_piece(id_logic, color)

                AddPlayer.greens_piece[p].idd = id_logic

                return id_logic, 'GREEN', kill_id_color

        elif color == "YELLOW":

            if (Ybox.move_check(id_gui)) and (id_gui == AddPlayer.yellows_piece[p].idd):
                strt = AddPlayer.yellows_piece[p].idd
                id_logic = Ybox.yellow_step[Ybox.yellow_step.index(strt) + roll_num]

                kill_id_color = killer_piece(id_logic, color)

                AddPlayer.yellows_piece[p].idd = id_logic

                if Ybox.at_home(AddPlayer.yellows_piece):
                    for item in AddPlayer.turn_player_list_logic:
                        if item[1] == 'YELLOW':
                            AddPlayer.turn_player_list_logic.remove(item)
                            AddPlayer.ranking.append(item)

                return id_logic, 'YELLOW', kill_id_color

            elif (not Ybox.move_check(id_gui)) and (id_gui == Ybox.yellow_step[0]) and (
                    id_gui == AddPlayer.yellows_piece[p].idd) and (roll_num == 6):
                id_logic = Ybox.yellow_step[1]

                kill_id_color = killer_piece(id_logic, color)

                AddPlayer.yellows_piece[p].idd = id_logic

                return id_logic, 'YELLOW', kill_id_color

    except IndexError:
        print("---------- Not Permissiom For This Move! ----------")

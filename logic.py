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
        gui.Board.ranking()
        return None
    else:
        x = turn_player % len(AddPlayer.turn_player_list_logic)
        print(x, turn_player, AddPlayer.turn_player_list_logic)
        print("nooobat ineh --->>>", AddPlayer.turn_player_list_logic[x])
        temp_list_players = AddPlayer.turn_player_list_logic.copy()
        roll_num_out = random.randint(1, 6)
        if roll_num_out == 6:
            print("=======>>>>>> gui.Board.turn_player", gui.Board.turn_player)

            gui.Board.turn_player -= 1
            print("=======>>>>>> gui.Board.turn_player", gui.Board.turn_player)
            return roll_num_out
        else:
            return roll_num_out
        # for item in temp_list_players:
        #     if item[1] == "BLUE":
        #         if (not Bbox.out_game(AddPlayer.blues_piece)):
        #             counter = 0
        #             while counter <=2:
        #                 gui.Board.turn_player -=1
        #                 counter +=1
        #                 return random.randint(1,6)
        #     elif item[1] == "GREEN":
        #         pass
        #     elif item[1] == "YELLOW":
        #         pass
        #     elif item[1] == "RED":
        #         pass

        # print(Rbox.out_game(AddPlayer.reds_piece))
        # return random.randint(1, 6)


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
            print(f'{self.user} have 4 piece with color {self.color}')

        if self.color == 'RED':
            AddPlayer.reds_piece = [Rbox() for _ in range(4)]
            print(f'{self.user} have 4 piece with color {self.color}')
        if self.color == 'GREEN':
            AddPlayer.greens_piece = [Gbox() for _ in range(4)]
            print(f'{self.user} have 4 piece with color {self.color}')
        if self.color == 'YELLOW':
            AddPlayer.yellows_piece = [Ybox() for _ in range(4)]
            print(f'{self.user} have 4 piece with color {self.color}')

        print(f"Counter of users is: {AddPlayer.counter_player}")

    # @property
    # def show_users(self):
    #     # print((self.user, self.color))
    #     return (self.user, self.color)

    @property
    def num_players(self):
        return self.counter_player


class Piece:
    def __init__(self):
        pass

    def move(self, start, end, length):
        pass


class Gbox():
    green_step = [7, 21, 20, 19, 12, 5, 4, 3, 10, 17, 16, 15, 22, 29, 30, 31, 38, 45, 46, 47, 40, 33, 34, 35, 28, 27]
    counter_all_piece = 0

    def __init__(self, idd=green_step[0], step=None, state=None):
        self.idd = idd
        self.step = step
        self.state = state
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

    def in_game(self):

        if self.idd != self.green_step[0] and self.idd != self.green_step[-1]:
            return True
        else:
            return False

    @staticmethod
    def out_game(greens_piece):
        for i in greens_piece:
            if (i.idd != Gbox.green_step[0]) and (i.idd != Gbox.green_step[-1]):
                return False
            else:
                continue
        else:
            return True


class Ybox():
    yellow_step = [49, 47, 40, 33, 34, 35, 28, 21, 20, 19, 12, 5, 4, 3, 10, 17, 16, 15, 22, 29, 30, 31, 38, 45, 46, 39]

    counter_all_piece = 0

    def __init__(self, idd=yellow_step[0], step=None, state=None):

        self.idd = idd
        self.step = step
        self.state = state
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

    def in_game(self):
        if self.idd != self.yellow_step[0] and self.idd != self.yellow_step[-1]:
            return True
        else:
            return False

    @staticmethod
    def out_game(yellows_piece):
        for i in yellows_piece:
            if (i.idd != Ybox.yellow_step[0]) and (i.idd != Ybox.yellow_step[-1]):
                return False
            else:
                continue
        else:
            return True

    def move(self):

        return self.yellow_step[self.yellow_step.index(self.idd) + self.step]

    def __del__(self):
        del self


class Bbox():
    blue_step = [1, 3, 10, 17, 16, 15, 22, 29, 30, 31, 38, 45, 46, 47, 40, 33, 34, 35, 28, 21, 20, 19, 12, 5, 4, 11]
    counter_all_piece = 0

    def __init__(self, idd=blue_step[0], step=None, state=None):

        self.idd = idd
        self.step = step
        self.state = state
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

    def in_game(self):
        if self.idd != self.blue_step[0] and self.idd != self.blue_step[-1]:
            return True
        else:
            return False

    @staticmethod
    def out_game(blues_piece):
        for i in blues_piece:
            if (i.idd != Bbox.blue_step[0]) and (i.idd != Bbox.blue_step[-1]):
                return False
            else:
                continue
        else:
            return True

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

    def in_game(self):
        if self.idd != self.red_step[0] and self.idd != self.red_step[-1]:
            return True
        else:
            return False

    @staticmethod
    def out_game(reds_piece):
        for i in reds_piece:
            if (i.idd != Rbox.red_step[0]) and (i.idd != Rbox.red_step[-1]):
                return False
            else:
                continue
        else:
            return True

    def move(self):

        return self.red_step[self.red_step.index(self.idd) + self.step]

    def __del__(self):
        del self


def win():
    logging.info(str(AddPlayer.ranking))
    logging.debug(str(AddPlayer.ranking))
    logging.debug("hi deeeeeebuuuuug")
    logging.error("hi, gggggggggh AddPlayer.ranking")
    # if len(AddPlayer.turn_player_list_logic) == 0:
    #     gui.Board.destroy()
    # gui.Board.destroy()
    # win_rank = Tk()
    if not AddPlayer.turn_player_list_logic:
        gui.Board.ranking()


def logic(id_gui, color, roll_num, p):
    try:
        if color == "BLUE":

            if (not Bbox.out_game(AddPlayer.blues_piece)) and (id_gui != Bbox.blue_step[0]):
                strt = AddPlayer.blues_piece[p].idd
                id_logic = Bbox.blue_step[Bbox.blue_step.index(strt) + roll_num]
                print(type(id_logic))
                if id_gui == AddPlayer.blues_piece[p].idd:
                    AddPlayer.blues_piece[p].idd = id_logic

                    if Bbox.at_home(AddPlayer.blues_piece):
                        print("ok bopop6666666666666666666666666666")
                        for item in AddPlayer.turn_player_list_logic:
                            if item[1] == 'BLUE':
                                AddPlayer.turn_player_list_logic.remove(item)
                                AddPlayer.ranking.append(item)
                                print("lis_1)))))))))", AddPlayer.turn_player_list_logic)
                                print("lis_2)))))))))", AddPlayer.ranking)
                                win()

                    return id_logic, 'BLUE'
            else:
                if (roll_num == 6) and (id_gui == AddPlayer.blues_piece[p].idd):
                    id_logic = Bbox.blue_step[1]
                    AddPlayer.blues_piece[p].idd = id_logic
                    return id_logic, 'BLUE'

        elif color == "RED":
            if (not Rbox.out_game(AddPlayer.reds_piece)) and (id_gui != Rbox.red_step[0]):
                strt = AddPlayer.reds_piece[p].idd
                id_logic = Rbox.red_step[Rbox.red_step.index(strt) + roll_num]
                print(type(id_logic))
                if id_gui == AddPlayer.reds_piece[p].idd:
                    AddPlayer.reds_piece[p].idd = id_logic

                    if Rbox.at_home(AddPlayer.reds_piece):
                        print("ok bopop6666666666666666666666666666")
                        for item in AddPlayer.turn_player_list_logic:
                            if item[1] == 'RED':
                                AddPlayer.turn_player_list_logic.remove(item)
                                AddPlayer.ranking.append(item)
                                print("lis_1)))))))))", AddPlayer.turn_player_list_logic)
                                print("lis_2)))))))))", AddPlayer.ranking)
                                win()

                    return id_logic, 'RED'
            else:
                if (roll_num == 6) and (id_gui == AddPlayer.reds_piece[p].idd):
                    id_logic = Rbox.red_step[1]
                    AddPlayer.reds_piece[p].idd = id_logic

                    return id_logic, 'RED'

        elif color == "GREEN":
            if (not Gbox.out_game(AddPlayer.greens_piece)) and (id_gui != Gbox.green_step[0]):
                strt = AddPlayer.greens_piece[p].idd
                id_logic = Gbox.green_step[Gbox.green_step.index(strt) + roll_num]
                print(type(id_logic))
                if id_gui == AddPlayer.greens_piece[p].idd:
                    AddPlayer.greens_piece[p].idd = id_logic

                    if Gbox.at_home(AddPlayer.greens_piece):
                        print("ok bopop6666666666666666666666666666")
                        for item in AddPlayer.turn_player_list_logic:
                            if item[1] == 'GREEN':
                                AddPlayer.turn_player_list_logic.remove(item)
                                AddPlayer.ranking.append(item)
                                print("lis_1)))))))))", AddPlayer.turn_player_list_logic)
                                print("lis_2)))))))))", AddPlayer.ranking)
                                win()

                    return id_logic, 'GREEN'
            else:
                if (roll_num == 6) and (id_gui == AddPlayer.greens_piece[p].idd):
                    id_logic = Gbox.green_step[1]
                    AddPlayer.greens_piece[p].idd = id_logic

                    return id_logic, 'GREEN'

        elif color == "YELLOW":
            if (not Ybox.out_game(AddPlayer.yellows_piece)) and (id_gui != Ybox.yellow_step[0]):
                strt = AddPlayer.yellows_piece[p].idd
                id_logic = Ybox.yellow_step[Ybox.yellow_step.index(strt) + roll_num]
                print(type(id_logic))
                if id_gui == AddPlayer.yellows_piece[p].idd:
                    AddPlayer.yellows_piece[p].idd = id_logic

                    if Ybox.at_home(AddPlayer.yellows_piece):
                        print("ok bopop6666666666666666666666666666")
                        for item in AddPlayer.turn_player_list_logic:
                            if item[1] == 'YELLOW':
                                AddPlayer.turn_player_list_logic.remove(item)
                                AddPlayer.ranking.append(item)
                                print("lis_1)))))))))", AddPlayer.turn_player_list_logic)
                                print("lis_2)))))))))", AddPlayer.ranking)
                                win()

                    return id_logic, 'YELLOW'
            else:
                if (roll_num == 6) and (id_gui == AddPlayer.yellows_piece[p].idd):
                    id_logic = Ybox.yellow_step[1]
                    AddPlayer.yellows_piece[p].idd = id_logic

                    return id_logic, 'YELLOW'

    except IndexError:
        print("---------- Not Permissiom For This Move! ----------")

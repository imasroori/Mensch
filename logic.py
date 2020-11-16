# 1st Project on MaktabSharif,Maktab42, Code by Iman Masroori
""" In this Module logic of game are designed"""
import random
import gui


def roll_dice(turn_player):
    x = turn_player % len(AddPlayer.turn_player_list_logic)
    print(x,turn_player,AddPlayer.turn_player_list_logic)
    print("nooobat ineh --->>>", AddPlayer.turn_player_list_logic[x])
    # if AddPlayer.turn_player_list_logic[x][1] == 'GREEN':
    #     for i in AddPlayer.greens_piece:
    #         print(i.idd,"idididididididididid")
    #         # print(type(i))
    #         if i.idd == Gbox.green_step[0]:
    #             return [random.randint(1,6)]
    #         elif i.idd != Gbox.green_step[-1]:
    #             i = None
    #         else:
    #             return random.randint(1,6)
    # if AddPlayer.turn_player_list_logic[x][1] == 'BLUE':
    #     flag = [0,0,0,0]
    #     for i in range(4):
    #         if AddPlayer.blues_piece[i].in_game():
    #             flag[i] = 1
    #     if flag:
    #         roll = random.randint(1,6)
    #
    #         return random.randint(1,6)
    #
    #
    #             random.randint(1,6)
    #         elif i.idd != Bbox.blue_step[-1]:
    #             i = None
    #         else:
    #             return random.randint(1,6)
    #
    # if AddPlayer.greens_piece:
    #     print(*[AddPlayer.greens_piece[i].at_home() for i in range(4)])
    #     print(*[AddPlayer.greens_piece[i].out_game() for i in range(4)])
    #
    # if AddPlayer.yellows_piece:
    #     print("---------------------------")
    #     print([AddPlayer.yellows_piece[i] for i in range(4)])
    #
    # if AddPlayer.blues_piece:
    #     print("+++++++++++++++++++++++++++++++")
    #     print([AddPlayer.blues_piece[x].out_game() for i in range(4)])
    #
    # if AddPlayer.reds_piece:
    #     print('*************************')
    #     print(*[AddPlayer.reds_piece[i].idd for i in range(4)])

    return random.randint(1, 6)



class AddPlayer:
    counter_player = 0
    turn_player_list_logic = []
    blues_piece = []
    reds_piece = []
    yellows_piece = []
    greens_piece = []

    def __init__(self, user, color):
        # self.counter_player += 1
        AddPlayer.counter_player += 1
        print(self.counter_player, "jjjjjjj", AddPlayer.counter_player)
        self.user = user
        self.color = color
        self.turn_player_list_logic.append((self.user, self.color))
        # print((self.user, self.color))
        print(self.turn_player_list_logic)
        self.init_instance()

    def init_instance(self):
        if self.color == 'BLUE':
            AddPlayer.blues_piece = [Bbox() for _ in range(4)]
            print("Huuuuuuu", *[AddPlayer.blues_piece[i].idd for i in range(4)])

        if self.color == 'RED':
            AddPlayer.reds_piece = [Rbox() for _ in range(4)]
            print("Huuuuuuu", *[AddPlayer.reds_piece[i].idd for i in range(4)])
        if self.color == 'GREEN':
            AddPlayer.greens_piece = [Gbox() for _ in range(4)]
            print("Huuuuuuu", *[AddPlayer.greens_piece[i].idd for i in range(4)])
            print("bbbbbbbb", *[AddPlayer.greens_piece[i].state for i in range(4)])
            print("Hnnnnnnn", *[AddPlayer.greens_piece[i].at_home() for i in range(4)])
            print("typessss", [type(AddPlayer.greens_piece[i]) for i in range(4)])
            [print(AddPlayer.greens_piece[i]) for i in range(4)]
        if self.color == 'YELLOW':
            AddPlayer.yellows_piece = [Ybox() for _ in range(4)]
            print("Huuuuuuu", *[AddPlayer.yellows_piece[i].idd for i in range(4)])

        print(AddPlayer.counter_player)

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

    def at_home(self):
        if self.idd == self.green_step[-1]:
            return True
        else:
            return False

    def in_game(self):
        if self.idd != self.green_step[0] and self.idd != self.green_step[-1]:
            return True
        else:
            return False

    def out_game(self):
        if self.idd == self.green_step[0]:
            return True
        else:
            return False





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

        self.idd = idd
        self.step = step
        self.state = state
        self.counter_all_piece += 1
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




# cc = Bbox(2)
# print(type(cc))
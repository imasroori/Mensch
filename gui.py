import random
from tkinter import *
from tkinter import ttk
import logic


class Board:
    roll_num = 0
    turn_player = -1
    reds = []
    blues = []
    greens = []
    yellows = []
    dic_colors = {"YELLOW": 'yellow', "BLUE": 'blue', "GREEN": 'green', "RED": 'red'}
    flag = 1

    def __init__(self, master):
        self.master = master
        self.master.title('Mensch Game')
        self.master.geometry("950x650+200+20")  # 200+20
        self.master.resizable(0, 0)
        self.values_color = ['YELLOW', 'GREEN', 'BLUE', 'RED']

        self.reds = []
        self.blues = []
        self.greens = []
        self.yellows = []

        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.menu()

        self.add_player()

        self.photo_roll_dice = PhotoImage(file="content/images/roll_dice.png")
        self.photo_blue_player = PhotoImage(file="content/images/BLUE-PLYER.png")
        self.photo_green_player = PhotoImage(file="content/images/GREEN-PLAYER.png", width=30, height=45)
        self.photo_red_player = PhotoImage(file="content/images/RED-PLAYER.png", width=30, height=45)
        self.photo_yellow_player = PhotoImage(file="content/images/YELLOW-PLAYER.png", width=30, height=45)

        self.frame_left = Frame(self.master, width=200, height=650)
        self.frame_left.grid(row=0, column=0)

        self.frame_right = Frame(self.master, width=750, height=650)
        self.frame_right.grid(row=0, column=1)

        self.can_board = Canvas(self.frame_right, width=750, height=650)
        self.can_board.pack()

        self.frame_panel = Frame(self.frame_left, width=200, height=250)
        self.frame_roll = Frame(self.frame_left, width=200, height=400)
        self.lbl_turn = Label(self.frame_roll)
        self.label_roll = Label(self.frame_roll)
        self.lbl_roll = Label(self.frame_roll)
        self.btn_roll = Button(self.frame_roll)

        self.lbl_red = [Label(self.can_board, image=self.photo_red_player) for _ in range(4)]
        self.lbl_green = [Label(self.can_board, image=self.photo_green_player) for _ in range(4)]
        self.lbl_yellow = [Label(self.can_board, image=self.photo_yellow_player) for _ in range(4)]
        self.lbl_blue = [Label(self.can_board, image=self.photo_blue_player) for _ in range(4)]

        self.lbl_players = Label(self.frame_panel, text="Players", fg='#ee11ee', font="Nazli 23 bold")

        self.lbl_users = [Label(self.frame_panel, font="Nazli 18 bold") for _ in range(4)]

        self.widgets()

        self.master.bind("<Button-1>", self.callback)
        # self.master.mainloop()

    def menu(self):
        self.filemenu.add_command(label="Add Player", font="Nazli 20 bold", command=self.add_player)
        self.filemenu.add_command(label="Start Game", font="Nazli 20 bold", state=DISABLED, command=self.start_game)
        self.filemenu.add_command(label="New Game", font="Nazli 20 bold", command=self.new_game)
        self.filemenu.add_command(label="Exit", font="Nazli 20 bold", command=self.exit_game)
        self.menubar.add_cascade(label="Game", font="Nazli 14 bold", menu=self.filemenu)

        self.menubar.add_cascade(label="Help", font="Nazli 14 bold", menu=self.helpmenu)
        self.master.config(menu=self.menubar)

    def widgets(self):

        self.lbl_blue[0].bind("<Button-1>", self.func1)
        self.lbl_blue[1].bind("<Button-1>", self.func2)
        self.lbl_blue[2].bind("<Button-1>", self.func3)
        self.lbl_blue[3].bind("<Button-1>", self.func4)

        self.lbl_red[0].bind("<Button-1>", self.func1)
        self.lbl_red[1].bind("<Button-1>", self.func2)
        self.lbl_red[2].bind("<Button-1>", self.func3)
        self.lbl_red[3].bind("<Button-1>", self.func4)

        self.lbl_green[0].bind("<Button-1>", self.func1)
        self.lbl_green[1].bind("<Button-1>", self.func2)
        self.lbl_green[2].bind("<Button-1>", self.func3)
        self.lbl_green[3].bind("<Button-1>", self.func4)

        self.lbl_yellow[0].bind("<Button-1>", self.func1)
        self.lbl_yellow[1].bind("<Button-1>", self.func2)
        self.lbl_yellow[2].bind("<Button-1>", self.func3)
        self.lbl_yellow[3].bind("<Button-1>", self.func4)

        temp = 0
        for i in range(7):
            for j in range(7):
                temp += 1
                if temp in [2, 6, 8, 9, 13, 14, 18, 24, 25, 26, 32, 36, 37, 41, 42, 44, 48]:
                    continue
                else:
                    if temp in [1, 3, 11]:
                        self.can_board.create_oval(80 * i + 120, 80 * j + 50, 80 * i + 180, 80 * j + 110,
                                                   fill="#5050ff")

                    elif temp in [7, 21, 27]:
                        self.can_board.create_oval(80 * i + 120, 80 * j + 50, 80 * i + 180, 80 * j + 110,
                                                   fill="#50ff50")

                    elif temp in [39, 47, 49]:
                        self.can_board.create_oval(80 * i + 120, 80 * j + 50, 80 * i + 180, 80 * j + 110,
                                                   fill="#ffff50")

                    elif temp in [23, 29, 43]:
                        self.can_board.create_oval(80 * i + 120, 80 * j + 50, 80 * i + 180, 80 * j + 110,
                                                   fill="#ff5050")
                    else:
                        self.can_board.create_oval(80 * i + 120, 80 * j + 50, 80 * i + 180, 80 * j + 110,
                                                   fill="#ffffff")
        self.frame_panel.place(x=0, y=0)

    def enter(self):
        try:
            username = self.entry_user.get()
            password = self.entry_pass.get()
            color_selected = self.color_select.get()
            with open("docs/players_user_pass.txt", 'r') as file1:
                for line in file1:
                    key, val = line.strip().split()
                    if username == key and val == password:
                        if logic.AddPlayer.counter_player <= 3:
                            self.values_color.remove(color_selected)

                        self.lbl_players.pack(side=TOP)
                        if color_selected == "BLUE":
                            logic.AddPlayer(username, color_selected)

                            # self.blues = [logic.Bbox(idd=logic.Bbox.blue_step[0]) for _ in range(4)]

                            # x + 12  y+6
                            [self.lbl_blue[i].place(y=80 * ((logic.Bbox.blue_step[0] + 6) % 7) + 56,
                                                    x=80 * (((logic.Bbox.blue_step[0] + 6) // 7) - 1) + 132) for i in
                             range(4)]
                            self.counter_lbl(color_selected)
                            self.lbl_users[0].config(text=username, fg="blue")
                            self.lbl_users[0].pack(padx=50, pady=2)

                        if color_selected == "RED":
                            logic.AddPlayer(username, color_selected)

                            self.reds = [logic.Rbox(idd=logic.Rbox.red_step[0]) for _ in range(4)]

                            # x + 12  y+6
                            [self.lbl_red[i].place(y=80 * ((self.reds[0].idd + 6) % 7) + 56,
                                                   x=80 * (((self.reds[0].idd + 6) // 7) - 1) + 132) for i in range(4)]
                            self.counter_lbl(color_selected)
                            self.lbl_users[1].config(text=username, fg="red")
                            self.lbl_users[1].pack(padx=50, pady=2)

                        if color_selected == "GREEN":
                            logic.AddPlayer(username, color_selected)

                            self.greens = [logic.Gbox(idd=logic.Gbox.green_step[0]) for _ in range(4)]

                            [self.lbl_green[i].place(y=80 * ((self.greens[0].idd + 6) % 7) + 56,
                                                     x=80 * (((self.greens[0].idd + 6) // 7) - 1) + 132) for i in
                             range(4)]
                            self.counter_lbl(color_selected)
                            self.lbl_users[2].config(text=username, fg="green")
                            self.lbl_users[2].pack(padx=50, pady=2)

                        if color_selected == "YELLOW":
                            logic.AddPlayer(username, color_selected)

                            self.yellows = [logic.Ybox(idd=logic.Ybox.yellow_step[0]) for _ in range(4)]

                            # x + 12  y+6
                            [self.lbl_yellow[i].place(y=80 * ((self.yellows[0].idd + 6) % 7) + 56,
                                                      x=80 * (((self.yellows[0].idd + 6) // 7) - 1) + 132) for i in
                             range(4)]
                            self.counter_lbl(color_selected)
                            self.lbl_users[3].config(text=username, fg="yellow")
                            self.lbl_users[3].pack(padx=50, pady=2)

                        self.cancel()
                        self.filemenu.entryconfigure(0, state=NORMAL)
                        if logic.AddPlayer.counter_player < 2:
                            self.filemenu.entryconfigure(1, state=DISABLED)
                        if logic.AddPlayer.counter_player >= 2:
                            self.filemenu.entryconfigure(1, state=NORMAL)
                        if logic.AddPlayer.counter_player == 4:
                            self.filemenu.entryconfigure(0, state=DISABLED)
                        break
                else:
                    print("UserName Not Found or PassWord Incorrect!")
                    self.lbl_ok.configure(text="UserName Not Found or PassWord Incorrect!", fg="#ff0000",
                                          font="Nazli 15 bold")
                    self.lbl_ok.place(x=190, y=210)

        except ValueError:
            self.lbl_ok.configure(text="Error!", fg="#ff0000", font="Nazli 15 bold")
            self.lbl_ok.place(x=300, y=215)

    def register(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()
        if username and password:
            with open("docs/players_user_pass.txt", 'a') as f:
                f.write(username)
                f.write('\t')
                f.write(password)
                f.write('\n')
            print(f"{username} Registered!")

            self.lbl_ok.configure(text=f"You are Registered! username is {username} and password is {password}",
                                  fg="#00ff00",
                                  font="Nazli 15 bold")
            self.lbl_ok.place(x=150, y=212)
        else:
            self.lbl_ok.configure(text=f"Unvalid UserName or PassWord!",
                                  fg="#ff0000",
                                  font="Nazli 15 bold")
            self.lbl_ok.place(x=220, y=212)

    def cancel(self):
        self.filemenu.entryconfigure(0, state=NORMAL)
        if logic.AddPlayer.counter_player >= 2:
            self.filemenu.entryconfigure(1, state=NORMAL)
        self.login_form.transient(self.master)
        self.login_form.withdraw()

    def new_game(self):
        print("!=======   Restart Game   =======!")
        self.destroy()
        logic.AddPlayer.counter_player = 0
        logic.AddPlayer.turn_player_list_logic = []
        Board.turn_player = -1

        RankInfo.c_rank = 0
        logic.AddPlayer.ranking = []

        board = Tk()
        Board(board)

    def exit_game(self):
        print("!=======   Exit Game   =======!")
        self.destroy()

    def destroy(self):
        self.master.destroy()

    def add_player(self):
        self.login_form = Toplevel(self.master)
        self.login_form.title("Login-Mensch")
        self.login_form.geometry("700x400+300+120")
        self.login_form.resizable(0, 0)

        self.login_form.lift(self.master)

        self.filemenu.entryconfigure(1, state=DISABLED)
        self.filemenu.entryconfigure(0, state=DISABLED)

        self.label_user = Label(self.login_form, text="UserName", font="Nazli 15 bold").place(x=215, y=100)
        self.label_user = Label(self.login_form, text="Welcome to Mensch, Enjoy!", font="Nazli 30 bold",
                                fg='blue').place(x=155, y=10)

        self.entry_user = Entry(self.login_form, fg="blue", textvariable=StringVar(), selectforeground="red", width=23)
        self.entry_user.place(x=305, y=108)

        self.label_pass = Label(self.login_form, text="PassWord", font="Nazli 15 bold").place(x=215, y=140)
        self.entry_pass = Entry(self.login_form, show="*", fg="blue", selectforeground="red", width=23)
        self.entry_pass.place(x=305, y=148)
        self.lbl_ok = Label(self.login_form)
        self.color_selection = Label(self.login_form, text="ColorPiece", font="Nazli 15 bold").place(x=215,
                                                                                                     y=180)
        self.color_select = ttk.Combobox(self.login_form, textvariable=StringVar())
        self.color_select.config(values=self.values_color, state='readonly')
        self.color_select.place(x=305, y=188)
        self.btn_enter = Button(self.login_form, text="Enter", bg="#80ff00", font="Nazli 15 bold",
                                activebackground="#92ff92", bd=4,
                                command=self.enter).place(x=220, y=250)
        self.btn_register = Button(self.login_form, text="Register", bg="#0080ff", font="Nazli 15 bold",
                                   activebackground="#30b9ff", bd=4,
                                   command=self.register).place(x=300, y=250)
        self.btn_cancel = Button(self.login_form, text="Cancel", bg="#ff8000", font="Nazli 15 bold",
                                 activebackground="#ff8080", bd=4,
                                 command=self.cancel).place(x=400, y=250)

    def start_game(self):
        print("!=======   Start Game   =======!")
        print(logic.AddPlayer.turn_player_list_logic)

        self.frame_roll.place(x=0, y=250)
        self.filemenu.entryconfigure(0, state=DISABLED)
        self.filemenu.entryconfigure(1, state=DISABLED)

        text_inp = f"Let's Go {logic.AddPlayer.turn_player_list_logic[0][0]}"

        self.lbl_turn.configure(text=text_inp, font="Nazli 17 bold",
                                fg=Board.dic_colors[logic.AddPlayer.turn_player_list_logic[0][1]])
        self.lbl_turn.pack()

        self.label_roll = Label(self.frame_roll, image=self.photo_roll_dice, width=150, height=150)
        self.label_roll.pack(pady=10, padx=10)
        self.btn_roll = Button(self.frame_roll, text="Roll", bg="#c269c2", bd=5, font="Nazli 16 bold", width=8,
                               command=self.roll_dice)
        self.btn_roll.pack()
        self.lbl_roll = Label(self.frame_roll, font="Nazli 35 bold", fg="#333333")
        # self.lbl_roll.pack(pady=15)

    def roll_dice(self):
        if logic.AddPlayer.turn_player_list_logic:
            self.roll_num = random.randint(1, 6)
            self.lbl_roll.configure(text=self.roll_num)
            self.lbl_roll.pack()

            self.roll_turn()
            # self.turn()

        else:
            self.btn_roll.configure(state=DISABLED)

    def func1(self, event):
        # returns the x,y co-ordinates of the mouse pointer relative to the main board.
        cx = self.master.winfo_pointerx() - self.master.winfo_rootx()
        cy = self.master.winfo_pointery() - self.master.winfo_rooty()

        j = (cx - 320) // 80
        i = (cy - 50) // 80
        id_gui = 7 * j + i + 1
        roll_num = self.roll_num
        p = 0
        color_piece = \
            logic.AddPlayer.turn_player_list_logic[Board.turn_player % len(logic.AddPlayer.turn_player_list_logic)][1]
        try:
            out = logic.logic(id_gui, color_piece, roll_num, p)
            target_id = out[0]
            color = out[1]

            killed_id_color = out[2]

            if color == "BLUE":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_blue[0].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            elif color == "RED":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_red[0].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            elif color == "GREEN":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_green[0].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            elif color == "YELLOW":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_yellow[0].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            logic.win()

        except TypeError:
            print("------- Click on Proprite Label! -------")

        print(f"row is {i}  and col is {j}", "id in gui is: ", id_gui)

    def func2(self, event):
        cx = self.master.winfo_pointerx() - self.master.winfo_rootx()
        cy = self.master.winfo_pointery() - self.master.winfo_rooty()
        j = (cx - 320) // 80
        i = (cy - 50) // 80
        id_gui = 7 * j + i + 1
        p = 1
        roll_num = self.roll_num
        color_piece = \
            logic.AddPlayer.turn_player_list_logic[Board.turn_player % len(logic.AddPlayer.turn_player_list_logic)][1]

        try:
            out = logic.logic(id_gui, color_piece, roll_num, p)
            target_id = out[0]
            color = out[1]
            killed_id_color = out[2]

            if color == "BLUE":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_blue[1].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            elif color == "RED":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_red[1].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            elif color == "GREEN":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_green[1].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            elif color == "YELLOW":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_yellow[1].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            logic.win()
        except TypeError:
            print("------- Click on Proprite Label! -------")

        print(f"row is {i}  and col is {j}", "id in gui is: ", id_gui)

    def func3(self, event):
        cx = self.master.winfo_pointerx() - self.master.winfo_rootx()
        cy = self.master.winfo_pointery() - self.master.winfo_rooty()

        j = (cx - 320) // 80
        i = (cy - 50) // 80
        id_gui = 7 * j + i + 1
        p = 2
        roll_num = self.roll_num
        color_piece = \
            logic.AddPlayer.turn_player_list_logic[Board.turn_player % len(logic.AddPlayer.turn_player_list_logic)][1]

        try:
            out = logic.logic(id_gui, color_piece, roll_num, p)
            target_id = out[0]
            color = out[1]

            killed_id_color = out[2]

            if color == "BLUE":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_blue[2].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            elif color == "RED":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_red[2].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            elif color == "GREEN":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_green[2].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            elif color == "YELLOW":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_yellow[2].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            logic.win()
        except TypeError:
            print("------- Click on Proprite Label! -------")

        print(f"row is {i}  and col is {j}", "id in gui is: ", id_gui)

    def func4(self, event):
        try:
            cx = self.master.winfo_pointerx() - self.master.winfo_rootx()
            cy = self.master.winfo_pointery() - self.master.winfo_rooty()

            j = (cx - 320) // 80
            i = (cy - 50) // 80
            id_gui = 7 * j + i + 1

            p = 3
            roll_num = self.roll_num
            color_piece = \
                logic.AddPlayer.turn_player_list_logic[Board.turn_player % len(logic.AddPlayer.turn_player_list_logic)][
                    1]

            out = logic.logic(id_gui, color_piece, roll_num, p)
            target_id = out[0]
            color = out[1]
            killed_id_color = out[2]

            if color == "BLUE":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_blue[3].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            elif color == "RED":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_red[3].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            elif color == "GREEN":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])

                self.counter_lbl(color)
                self.lbl_green[3].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            elif color == "YELLOW":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                        self.counter_lbl(ii[1])
                self.counter_lbl(color)
                self.lbl_yellow[3].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
                self.roll_turn(roll_num)

            logic.win()
            print(f"row is {i}  and col is {j}", "id in gui is: ", id_gui)
        except TypeError:
            print("------- Click on Proprite Label! -------")
        except ZeroDivisionError:
            print("!=======  Game Ended!  =======!")

    def callback(self, event):
        # This formula returns the x,y co-ordinates of the mouse pointer relative to the board.
        cx = self.master.winfo_pointerx() - self.master.winfo_rootx()
        cy = self.master.winfo_pointery() - self.master.winfo_rooty()
        print("clicked on widget ", event.x, event.y)
        print("clicked on Board :", cx, cy)
        # return event.x, event.y

    def turn(self):
        color = Board.dic_colors[logic.AddPlayer.turn_player_list_logic[
            Board.turn_player % len(logic.AddPlayer.turn_player_list_logic)][1]]
        if logic.AddPlayer.turn_player_list_logic:
            self.lbl_turn.configure(
                text=f"TURN:{logic.AddPlayer.turn_player_list_logic[(Board.turn_player % len(logic.AddPlayer.turn_player_list_logic))][0]}",
                fg=color, font="Nazli 17 bold")

            self.lbl_turn.pack()

    def roll_turn(self, roll_n=None):

        if roll_n is not None:
            self.roll_num = 0
            if roll_n == 6:
                Board.turn_player -= 1

        elif roll_n is None:
            Board.turn_player += 1
            self.turn()
            usr = logic.AddPlayer.turn_player_list_logic[
                Board.turn_player % len(logic.AddPlayer.turn_player_list_logic)]
            if self.roll_num == 6:
                return None

            elif usr[1] == 'BLUE' and logic.Bbox.out_game(logic.AddPlayer.blues_piece):
                if self.roll_num != 6:
                    if Board.flag < 3:
                        Board.turn_player -= 1
                        Board.flag += 1
                        self.roll_num = 0
                    else:
                        Board.flag = 1
                else:
                    Board.turn_player -= 1
                # break
            elif usr[1] == 'GREEN' and logic.Gbox.out_game(logic.AddPlayer.greens_piece):
                if self.roll_num != 6:
                    if Board.flag < 3:
                        Board.turn_player -= 1
                        Board.flag += 1
                        self.roll_num = 0
                    else:
                        Board.flag = 1
                else:
                    Board.turn_player -= 1
                # break
            elif usr[1] == 'YELLOW' and logic.Ybox.out_game(logic.AddPlayer.yellows_piece):
                if self.roll_num != 6:
                    if Board.flag < 3:
                        Board.turn_player -= 1
                        Board.flag += 1
                        self.roll_num = 0
                    else:
                        Board.flag = 1
                else:
                    Board.turn_player -= 1
                # break
            elif usr[1] == 'RED' and logic.Rbox.out_game(logic.AddPlayer.reds_piece):
                if self.roll_num != 6:
                    if Board.flag < 3:
                        Board.turn_player -= 1
                        Board.flag += 1
                        self.roll_num = 0
                    else:
                        Board.flag = 1
                else:
                    Board.turn_player -= 1

    def killed(self, killed_piece, killed_color):

        if killed_color == 'BLUE':
            self.lbl_blue[killed_piece].place(x=80 * (((logic.Bbox.blue_step[0] + 6) // 7) - 1) + 132,
                                              y=80 * ((logic.Bbox.blue_step[0] + 6) % 7) + 56)
            logic.AddPlayer.blues_piece[killed_piece].idd = logic.Bbox.blue_step[0]
        if killed_color == 'RED':
            self.lbl_red[killed_piece].place(x=80 * (((logic.Rbox.red_step[0] + 6) // 7) - 1) + 132,
                                             y=80 * ((logic.Rbox.red_step[0] + 6) % 7) + 56)
            logic.AddPlayer.reds_piece[killed_piece].idd = logic.Rbox.red_step[0]
        if killed_color == 'GREEN':
            self.lbl_green[killed_piece].place(x=80 * (((logic.Gbox.green_step[0] + 6) // 7) - 1) + 132,
                                               y=80 * ((logic.Gbox.green_step[0] + 6) % 7) + 56)
            logic.AddPlayer.greens_piece[killed_piece].idd = logic.Gbox.green_step[0]
        if killed_color == 'YELLOW':
            self.lbl_yellow[killed_piece].place(x=80 * (((logic.Ybox.yellow_step[0] + 6) // 7) - 1) + 132,
                                                y=80 * ((logic.Ybox.yellow_step[0] + 6) % 7) + 56)
            logic.AddPlayer.yellows_piece[killed_piece].idd = logic.Ybox.yellow_step[0]

    def counter_lbl(self, color):
        if color == 'GREEN':
            tmp = logic.Gbox.overlap(lis=logic.AddPlayer.greens_piece)
            self.lbl_green[3].configure(text=tmp[3] if tmp[3] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                        fg='white')
            self.lbl_green[2].configure(text=tmp[2] if tmp[2] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                        fg='white')
            self.lbl_green[1].configure(text=tmp[1] if tmp[1] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                        fg='white')
            self.lbl_green[0].configure(text=tmp[0] if tmp[0] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                        fg='white')
        elif color == 'BLUE':
            tmp = logic.Bbox.overlap(lis=logic.AddPlayer.blues_piece)
            self.lbl_blue[3].configure(text=tmp[3] if tmp[3] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                       fg='white')
            self.lbl_blue[2].configure(text=tmp[2] if tmp[2] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                       fg='white')
            self.lbl_blue[1].configure(text=tmp[1] if tmp[1] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                       fg='white')
            self.lbl_blue[0].configure(text=tmp[0] if tmp[0] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                       fg='white')
        elif color == 'RED':
            tmp = logic.Rbox.overlap(lis=logic.AddPlayer.reds_piece)
            self.lbl_red[3].configure(text=tmp[3] if tmp[3] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                      fg='white')
            self.lbl_red[2].configure(text=tmp[2] if tmp[2] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                      fg='white')
            self.lbl_red[1].configure(text=tmp[1] if tmp[1] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                      fg='white')
            self.lbl_red[0].configure(text=tmp[0] if tmp[0] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                      fg='white')
        elif color == 'YELLOW':
            tmp = logic.Ybox.overlap(lis=logic.AddPlayer.yellows_piece)
            self.lbl_yellow[3].configure(text=tmp[3] if tmp[3] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                         fg='white')
            self.lbl_yellow[2].configure(text=tmp[2] if tmp[2] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                         fg='white')
            self.lbl_yellow[1].configure(text=tmp[1] if tmp[1] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                         fg='white')
            self.lbl_yellow[0].configure(text=tmp[0] if tmp[0] != 1 else ' ', compound=CENTER, font='Nazli 20 bold',
                                         fg='white')


class RankInfo:
    c_rank = 0
    dic_colors = {"YELLOW": 'yellow', "BLUE": 'blue', "GREEN": 'green', "RED": 'red'}

    def __init__(self, root):
        self.win_ranks = root
        self.win_ranks.title('Ranking')
        self.win_ranks.resizable(0, 0)
        self.win_ranks.geometry('450x400+300+200')

        c_rank = 0
        Label(self.win_ranks, text='Game Finished!', font='Nazli 18 bold').pack()
        for item in logic.AddPlayer.ranking:
            c_rank += 1
            Label(self.win_ranks, text=f'Rank {c_rank}: ' + str(item[0]), font='Nazli 25 bold',
                  fg=RankInfo.dic_colors[item[1]]).pack()
        btn_close = Button(self.win_ranks, text='Ok,Finished!', bg='#c390c3', font='Nazli 15 bold', command=self.exit)
        btn_close.pack()

    def exit(self):
        self.destroy()

    def destroy(self):
        self.win_ranks.destroy()

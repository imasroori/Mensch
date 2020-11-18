from tkinter import *
from tkinter import ttk
import logic


class Board:
    # turn_player_list = []
    # player_and_colors = []
    roll_num = 0
    turn_player = -1
    reds = []
    blues = []
    greens = []
    yellows = []

    def __init__(self, master):
        self.master = master
        self.master.title('Mensch Game')
        self.master.geometry("950x650+200+20")  # 200+20
        self.master.resizable(0, 0)
        self.values_color = ['YELLOW', 'GREEN', 'BLUE', 'RED']
        # self.turn_player_list = []
        # self.player_and_colors = []

        self.reds = []
        self.blues = []
        self.greens = []
        self.yellows = []

        # self.turn_player = -1

        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.menu()

        # self.counter_player = 0
        self.add_player()

        self.photo_roll_dice = PhotoImage(file="content/images/roll_dice.png")
        self.photo_blue_player = PhotoImage(file="content/images/BLUE-PLYER.png", width=30, height=45)
        self.photo_green_player = PhotoImage(file="content/images/GREEN-PLAYER.png", width=30, height=45)
        self.photo_red_player = PhotoImage(file="content/images/RED-PLAYER.png", width=30, height=45)
        self.photo_yellow_player = PhotoImage(file="content/images/YELLOW-PLAYER.png", width=30, height=45)

        self.frame_left = Frame(self.master, width=200, height=650)
        self.frame_left.grid(row=0, column=0)

        self.frame_right = Frame(self.master, width=750, height=650, bg="red")
        self.frame_right.grid(row=0, column=1)

        self.can_board = Canvas(self.frame_right, width=750, height=650)
        self.can_board.pack()

        self.frame_panel = Frame(self.frame_left, width=200, height=250)
        self.frame_roll = Frame(self.frame_left, width=200, height=400)
        self.lbl_turn = Label(self.frame_roll)

        self.lbl_red = [Label(self.can_board, image=self.photo_red_player) for _ in range(4)]
        self.lbl_green = [Label(self.can_board, image=self.photo_green_player) for _ in range(4)]
        self.lbl_yellow = [Label(self.can_board, image=self.photo_yellow_player) for _ in range(4)]
        self.lbl_blue = [Label(self.can_board, image=self.photo_blue_player) for _ in range(4)]

        self.lbl_players = Label(self.frame_panel, text="Players", font="Nazli 18 bold")

        self.lbl_users = [Label(self.frame_panel, font="Nazli 18 bold") for _ in range(4)]

        self.widgets()

        # self.lbl_over = Label(self.frame_right)
        # self.lbl_over.pack(fill=BOTH)
        # self.lbl_over.bind("<Button-1>", self.callback)
        self.master.bind("<Button-1>", self.callback)
        # self.master.mainloop()

    def menu(self):
        self.filemenu.add_command(label="Add Player", font="Nazli 14 bold", command=self.add_player)
        self.filemenu.add_command(label="Start Game", font="Nazli 14 bold", state=DISABLED, command=self.start_game)
        self.filemenu.add_command(label="New Game", font="Nazli 14 bold", command=self.new_game)
        self.filemenu.add_command(label="Exit", font="Nazli 14 bold", command=self.exit_game)
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
            with open("content/players_user_pass.txt", 'r') as file1:
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

                            self.lbl_users[0].config(text=username, fg="blue")
                            self.lbl_users[0].pack(padx=50, pady=2)

                        if color_selected == "RED":
                            logic.AddPlayer(username, color_selected)

                            self.reds = [logic.Rbox(idd=logic.Rbox.red_step[0]) for _ in range(4)]

                            # x + 12  y+6
                            [self.lbl_red[i].place(y=80 * ((self.reds[0].idd + 6) % 7) + 56,
                                                   x=80 * (((self.reds[0].idd + 6) // 7) - 1) + 132) for i in range(4)]

                            self.lbl_users[1].config(text=username, fg="red")
                            self.lbl_users[1].pack(padx=50, pady=2)

                        if color_selected == "GREEN":
                            logic.AddPlayer(username, color_selected)

                            self.greens = [logic.Gbox(idd=logic.Gbox.green_step[0]) for _ in range(4)]

                            # x + 12  y+6
                            [self.lbl_green[i].place(y=80 * ((self.greens[0].idd + 6) % 7) + 56,
                                                     x=80 * (((self.greens[0].idd + 6) // 7) - 1) + 132) for i in
                             range(4)]

                            self.lbl_users[2].config(text=username, fg="green")
                            self.lbl_users[2].pack(padx=50, pady=2)

                        if color_selected == "YELLOW":
                            logic.AddPlayer(username, color_selected)

                            self.yellows = [logic.Ybox(idd=logic.Ybox.yellow_step[0]) for _ in range(4)]

                            # x + 12  y+6
                            [self.lbl_yellow[i].place(y=80 * ((self.yellows[0].idd + 6) % 7) + 56,
                                                      x=80 * (((self.yellows[0].idd + 6) // 7) - 1) + 132) for i in
                             range(4)]

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
            self.lbl_ok.configure(text="Error!")
            self.lbl_ok.place(x=300, y=225)

    def register(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()
        if username and password:
            with open("content/players_user_pass.txt", 'a') as f:
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

        self.label_user = Label(self.login_form, text="UserName", font="Nazli 14 bold").place(x=220, y=100)

        self.entry_user = Entry(self.login_form, fg="blue", textvariable=StringVar(), selectforeground="red", width=23)
        self.entry_user.place(x=300, y=108)

        self.label_pass = Label(self.login_form, text="PassWord", font="Nazli 14 bold").place(x=220, y=140)
        self.entry_pass = Entry(self.login_form, show="*", fg="blue", selectforeground="red", width=23)
        self.entry_pass.place(x=300, y=148)
        self.lbl_ok = Label(self.login_form)
        self.color_selection = Label(self.login_form, text="ColorPiece", font="Nazli 14 bold").place(x=220,
                                                                                                     y=180)
        self.color_select = ttk.Combobox(self.login_form, textvariable=StringVar())
        self.color_select.config(values=self.values_color, state='readonly')
        self.color_select.place(x=300, y=188)
        self.btn_enter = Button(self.login_form, text="Enter", bg="#bbbbbb", font="Nazli 15 bold",
                                activebackground="skyblue",
                                activeforeground="blue", command=self.enter).place(x=220, y=250)
        self.btn_register = Button(self.login_form, text="Register", bg="#bbbbbb", font="Nazli 15 bold",
                                   activebackground="skyblue",
                                   activeforeground="blue", command=self.register).place(x=300, y=250)
        self.btn_cancel = Button(self.login_form, text="Cancel", bg="#bbbbbb", font="Nazli 15 bold",
                                 activebackground="skyblue",
                                 activeforeground="blue", command=self.cancel).place(x=400, y=250)

    def start_game(self):
        print("!=======   Start Game   =======!")
        print(logic.AddPlayer.turn_player_list_logic)
        # self.frame_roll = Frame(self.frame_left, width=200, height=400)

        self.frame_roll.place(x=0, y=250)
        self.filemenu.entryconfigure(0, state=DISABLED)
        self.filemenu.entryconfigure(1, state=DISABLED)

        self.turn()

        # self.lbl_turn.configure(text=f"Start {logic.AddPlayer.turn_player_list_logic[0][1]}")
        # self.lbl_turn.pack()

        self.label_roll = Label(self.frame_roll, image=self.photo_roll_dice, width=150, height=150)
        self.label_roll.pack(pady=10, padx=10)
        self.btn_roll = Button(self.frame_roll, text="Roll", bg="skyblue", bd=4, font="Nazli 14 bold", width=8,
                               command=self.roll_dice)
        self.btn_roll.pack()
        self.lbl_roll = Label(self.frame_roll, font="Nazli 35 bold", fg="blue")
        self.lbl_roll.pack(pady=15)

    def roll_dice(self):
        if logic.AddPlayer.turn_player_list_logic:
            self.roll_num = logic.roll_dice(Board.turn_player)
            Board.turn_player += 1
            self.lbl_roll.configure(text=self.roll_num)
            self.turn()
        else:
            self.btn_roll.configure(state=DISABLED)
        print(f'turn is :{Board.turn_player}')

    def func1(self, event):
        print("aaaaaaaaaaaaaaaaaaaaaa")
        # returns the x,y co-ordinates of the mouse pointer relative to the main board.
        cx = self.master.winfo_pointerx() - self.master.winfo_rootx()
        cy = self.master.winfo_pointery() - self.master.winfo_rooty()

        print("on widget cx,cy:", cx, cy)

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

            # killed_piece = out[2]
            # killed_color = out[3]
            killed_id_color = out[2]

            if color == "BLUE":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_blue[0].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)

            elif color == "RED":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_red[0].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)

            elif color == "GREEN":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_green[0].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)

            elif color == "YELLOW":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_yellow[0].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
            logic.win()
            # self.turn()
        except TypeError:
            print("------- Click on Proprite Label! -------")

        print(f"row is {i}  and col is {j}", "id in gui is: ", id_gui)

    def func2(self, event):
        print("bbbbbbbbbbbbbbbbbbbb")
        cx = self.master.winfo_pointerx() - self.master.winfo_rootx()
        cy = self.master.winfo_pointery() - self.master.winfo_rooty()
        print("on widget cx,cy:", cx, cy)
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
            # killed_piece = out[2]
            # killed_color = out[3]

            if color == "BLUE":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_blue[1].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)

            elif color == "RED":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_red[1].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)

            elif color == "GREEN":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_green[1].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)

            elif color == "YELLOW":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0],ii[1])
                self.lbl_yellow[1].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
            # self.turn()
            logic.win()
        except TypeError:
            print("------- Click on Proprite Label! -------")

        print(f"row is {i}  and col is {j}", "id in gui is: ", id_gui)

    def func3(self, event):
        print("ccccccccccccccccccccc")
        cx = self.master.winfo_pointerx() - self.master.winfo_rootx()
        cy = self.master.winfo_pointery() - self.master.winfo_rooty()
        # print("clicked on gggg ", event.x, event.y)
        print("on widget cx,cy:", cx, cy)
        # row, col = self.callback(event)
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
            # killed_piece
            # killed_color = out[3]

            if color == "BLUE":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_blue[2].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)

            elif color == "RED":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_red[2].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)

            elif color == "GREEN":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_green[2].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)

            elif color == "YELLOW":
                if killed_id_color:
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_yellow[2].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
            # self.turn()
            logic.win()
        except TypeError:
            print("------- Click on Proprite Label! -------")

        print(f"row is {i}  and col is {j}", "id in gui is: ", id_gui)

    def func4(self, event):
        try:
            print("dddddddddddddddddddddddddd")
            cx = self.master.winfo_pointerx() - self.master.winfo_rootx()
            cy = self.master.winfo_pointery() - self.master.winfo_rooty()
            print("on widget cx,cy:", cx, cy)
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
            # killed_piece = out[2]
            # killed_color = out[3]

            # color = logic.logic(id_gui, color_piece, roll_num, p)[1]
            if color == "BLUE":
                if killed_id_color:
                    print('<<<<<<<<<<<<<<<<<', killed_id_color)
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_blue[3].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)

            elif color == "RED":
                if killed_id_color:
                    print('<<<<<<<<<<<<<<<<<', killed_id_color)
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_red[3].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)

            elif color == "GREEN":
                if killed_id_color:
                    print('<<<<<<<<<<<<<<<<<', killed_id_color)
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_green[3].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)

            elif color == "YELLOW":
                if killed_id_color:
                    print('<<<<<<<<<<<<<<<<<', killed_id_color)
                    for ii in killed_id_color:
                        self.killed(ii[0], ii[1])
                self.lbl_yellow[3].place(x=80 * (((target_id + 6) // 7) - 1) + 132, y=80 * ((target_id + 6) % 7) + 56)
            # self.turn()
            logic.win()
        except TypeError:
            print("------- Click on Proprite Label! -------")
        except ZeroDivisionError:
            print("!=======  Game Ended!  =======!")

        print(f"row is {i}  and col is {j}", "id in gui is: ", id_gui)

    # @staticmethod
    def callback(self, event):
        cx = self.master.winfo_pointerx() - self.master.winfo_rootx()  # This formula returns the x,y co-ordinates of the mouse pointer relative to the board.
        cy = self.master.winfo_pointery() - self.master.winfo_rooty()
        print("clicked on ", event.x, event.y)
        print("cx,cy is:", cx, cy)
        # return event.x, event.y

    def turn(self):
        dic_colors = {"YELLOW": 'yellow', "BLUE": 'blue', "GREEN": 'green', "RED": 'red'}
        color = dic_colors[
            logic.AddPlayer.turn_player_list_logic[(Board.turn_player) % len(logic.AddPlayer.turn_player_list_logic)][
                1]]
        if Board.turn_player == -1:
            text_inp = f"Let's Go {logic.AddPlayer.turn_player_list_logic[0][0]}"

            self.lbl_turn.configure(text=text_inp, font="Nazli 17 bold",
                                    fg=dic_colors[logic.AddPlayer.turn_player_list_logic[0][1]])
            self.lbl_turn.pack()
        else:
            self.lbl_turn.configure(
                text=f"TURN:{logic.AddPlayer.turn_player_list_logic[(Board.turn_player % len(logic.AddPlayer.turn_player_list_logic))][0]}",
                fg=color, font="Nazli 17 bold")
            self.lbl_turn.pack()

    # def ranking(self):

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


class RankInfo:
    dic_colors = {"YELLOW": 'yellow', "BLUE": 'blue', "GREEN": 'green', "RED": 'red'}
    c_rank = 0

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
        btn_close = Button(self.win_ranks, text='Ok!', font='Nazli 15 bold', command=self.exit)
        btn_close.pack()

    def exit(self):
        self.destroy()

    def destroy(self):
        self.win_ranks.destroy()

from tkinter import *
import random
from tkinter import ttk
import logic
from tkinter import messagebox


class AddPlayer:
    counter_player = 0

    def __init__(self):
        AddPlayer.counter_player += 1

    @property
    def num_players(self):
        return self.counter_player


class Board:
    def __init__(self, master):
        self.master = master
        self.master.title('Mensch Game')
        self.master.geometry("950x650+200+20")
        self.master.resizable(0, 0)
        self.values_color = ['YELLOW', 'GREEN', 'BLUE', 'RED']
        self.turn_player_list = []
        self.player_and_colors = []

        self.reds = []
        self.blues = []
        self.greens = []
        self.yellows = []

        self.turn_player = 0
        self.menubar = Menu(self.master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.counter_player = 0
        self.add_player()
        self.filemenu.add_command(label="Add Player", font="Nazli 14 bold", command=self.add_player)
        self.filemenu.add_command(label="Start Game", font="Nazli 14 bold", state=DISABLED, command=self.start_game)
        self.filemenu.add_command(label="New Game", font="Nazli 14 bold", command=self.new_game)
        self.filemenu.add_command(label="Exit", font="Nazli 14 bold", command=self.exit_game)
        self.menubar.add_cascade(label="Game", font="Nazli 14 bold", menu=self.filemenu)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", font="Nazli 14 bold", menu=self.helpmenu)
        self.master.config(menu=self.menubar)

        self.photo_roll_dice = PhotoImage(file="content/images/roll_dice.png")
        self.photo_blue_player = PhotoImage(file="content/images/BLUE-PLYER.png", width=30, height=45)
        self.photo_green_player = PhotoImage(file="content/images/GREEN-PLAYER.png", width=30, height=45)
        self.photo_red_player = PhotoImage(file="content/images/RED-PLAYER.png", width=30, height=45)
        self.photo_yellow_player = PhotoImage(file="content/images/YELLOW-PLAYER.png", width=30, height=45)

        self.frame_left = Frame(self.master, width=200, height=650)
        self.frame_left.grid(row=0, column=0)

        self.frame_right = Frame(self.master, width=750, height=650, bg="red")
        self.frame_right.grid(row=0, column=1)

        self.can_board = Canvas(self.frame_right, width=750, height=660)
        self.can_board.pack()

        self.lbl_blue_1 = Label(self.can_board, image=self.photo_blue_player)
        self.lbl_blue_2 = Label(self.can_board, image=self.photo_blue_player)
        self.lbl_blue_3 = Label(self.can_board, image=self.photo_blue_player)
        self.lbl_blue_4 = Label(self.can_board, image=self.photo_blue_player)
        self.lbl_blue_1.bind("<Button-1>", self.func1)
        self.lbl_blue_2.bind("<Button-1>", self.func1)
        self.lbl_blue_3.bind("<Button-1>", self.func1)
        self.lbl_blue_4.bind("<Button-1>", self.func1)

        self.master.bind("<Button-1>", self.callback)
        self.lbl_red = Label(self.can_board, image=self.photo_red_player)

        self.lbl_green = Label(self.can_board, image=self.photo_green_player)

        self.lbl_yellow = Label(self.can_board, image=self.photo_yellow_player)

        c = 0
        for i in range(7):
            for j in range(7):
                c += 1
                if c in [2, 6, 8, 9, 13, 14, 18, 24, 25, 26, 32, 36, 37, 41, 42, 44, 48]:
                    continue
                else:
                    if c in [1, 3, 11]:
                        self.can_board.create_oval(80 * i + 120, 80 * j + 50, 80 * i + 180, 80 * j + 110,
                                                   fill="#5050ff")

                    elif c in [7, 21, 27]:
                        self.can_board.create_oval(80 * i + 120, 80 * j + 50, 80 * i + 180, 80 * j + 110,
                                                   fill="#50ff50")

                    elif c in [39, 47, 49]:
                        self.can_board.create_oval(80 * i + 120, 80 * j + 50, 80 * i + 180, 80 * j + 110,
                                                   fill="#ffff50")

                    elif c in [23, 29, 43]:
                        self.can_board.create_oval(80 * i + 120, 80 * j + 50, 80 * i + 180, 80 * j + 110,
                                                   fill="#ff5050")
                    else:
                        self.can_board.create_oval(80 * i + 120, 80 * j + 50, 80 * i + 180, 80 * j + 110,
                                                   fill="#ffffff")

        self.frame_panel = Frame(self.frame_left, width=200, height=250)
        self.frame_panel.place(x=0, y=0)
        self.lbl_players = Label(self.frame_panel, text="Players", font="Nazli 18 bold")
        self.lbl_user1 = Label(self.frame_panel, font="Nazli 18 bold")

        self.lbl_user2 = Label(self.frame_panel, font="Nazli 18 bold")

        self.lbl_user3 = Label(self.frame_panel, font="Nazli 18 bold")

        self.lbl_user4 = Label(self.frame_panel, font="Nazli 18 bold")

        self.master.mainloop()

    def enter(self):
        try:
            username = self.entry_user.get()
            password = self.entry_pass.get()
            color_selected = self.color_select.get()

            with open("content/players_user_pass.txt", 'r') as file1:
                for line in file1:
                    key, val = line.strip().split()
                    if username == key and val == password:
                        if self.counter_player <= 3:
                            self.values_color.remove(color_selected)

                        self.turn_player_list.append(color_selected)
                        print(len(self.turn_player_list))
                        print(self.turn_player_list)
                        print(self.values_color)
                        print("ok")
                        print(username, '\t', password, '\t', color_selected)
                        self.player_and_colors.append((username, color_selected))
                        self.lbl_players.pack(side=TOP)
                        if color_selected == "BLUE":
                            self.blues = [logic.Bbox(idd=logic.Bbox.blue_step[0]) for _ in range(4)]

                            # self.lbl_blue_1.configure(text=len(self.blues), fg="white", font="Nazli 15 bold", compound=CENTER)
                            self.lbl_blue_1.place(x=80 * ((self.blues[0].idd % 7) - 1) + 132,
                                                  y=80 * (self.blues[0].idd // 7) + 56)  # x + 12  y+6 132,56

                            # self.lbl_blue_2.configure(text=len(self.blues), fg="white", font="Nazli 15 bold", compound=CENTER)
                            self.lbl_blue_2.place(x=80 * ((self.blues[0].idd % 7) - 1) + 132,
                                                  y=80 * (self.blues[0].idd // 7) + 56)  # x + 12  y+6 132,56

                            # self.lbl_blue_3.configure(text=len(self.blues), fg="white", font="Nazli 15 bold", compound=CENTER)
                            self.lbl_blue_3.place(x=80 * ((self.blues[0].idd % 7) - 1) + 132,
                                                  y=80 * (self.blues[0].idd // 7) + 56)  # x + 12  y+6 132,56

                            # self.lbl_blue_4.configure(text=len(self.blues), fg="white", font="Nazli 15 bold", compound=CENTER)
                            self.lbl_blue_4.place(x=80 * ((self.blues[0].idd % 7) - 1) + 132,
                                                  y=80 * (self.blues[0].idd // 7) + 56)  # x + 12  y+6 132,56

                            self.lbl_user1.config(text=username, fg="blue")
                            self.lbl_user1.pack(padx=50, pady=2)

                            self.counter_player += 1
                            print("self.counter_player", self.counter_player)
                        if color_selected == "RED":
                            self.reds = [logic.Rbox() for _ in range(4)]
                            self.lbl_red.configure(text=4, fg="white", font="Nazli 15 bold", compound=CENTER)
                            self.lbl_red.place(x=612, y=56)
                            self.lbl_user2.config(text=username, fg="red")
                            self.lbl_user2.pack(padx=50, pady=2)

                            self.counter_player += 1
                            print("self.counter_player", self.counter_player)
                        if color_selected == "GREEN":
                            self.greens = [logic.Gbox() for _ in range(4)]
                            self.lbl_green.configure(text=len(self.greens), fg="white", font="Nazli 15 bold",
                                                     compound=CENTER)
                            self.lbl_green.place(x=132, y=536)
                            self.lbl_user3.config(text=username, fg="green")
                            self.lbl_user3.pack(padx=50, pady=2)

                            self.counter_player += 1
                            print("self.counter_player", self.counter_player)
                        if color_selected == "YELLOW":
                            self.yellows = [logic.Ybox() for _ in range(4)]
                            self.lbl_yellow.configure(text=len(self.yellows), fg="white", font="Nazli 15 bold",
                                                      compound=CENTER)
                            self.lbl_yellow.place(x=612, y=536)
                            self.lbl_user4.config(text=username, fg="yellow")
                            self.lbl_user4.pack(padx=50, pady=2)

                            self.counter_player += 1
                            print("self.counter_player", self.counter_player)
                        self.cancel()

                        if self.counter_player < 2:
                            self.filemenu.entryconfigure(1, state=DISABLED)
                        if self.counter_player >= 2:
                            self.filemenu.entryconfigure(1, state=NORMAL)
                        if self.counter_player == 4:
                            self.filemenu.entryconfigure(0, state=DISABLED)
                        print("akhar", self.counter_player)
                        break
                else:
                    print("UserName Not Found or PassWord Incorrect!")
                    # messagebox.showerror(title="Error",message="UserName Not Found or PassWord Incorrect!")
                    self.lbl_ok.configure(text="UserName Not Found or PassWord Incorrect!", fg="#ff0000",
                                          font="Nazli 15 bold")
                    self.lbl_ok.place(x=185, y=210)

        except ValueError:
            # messagebox.showerror(title="Error",message="ggggg")
            self.lbl_ok.configure(text="Error!")
            self.lbl_ok.place(x=300, y=225)

    def register(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()
        if username and password:
            with open("content/players_user_pass.txt", 'a') as f:
                # f.write('\n')
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
        self.login_form.transient(self.master)
        self.login_form.withdraw()

    def new_game(self):
        print("Restart Game!")
        self.destroy()

        board = Tk()
        print("AddPlayer.counter_player,", AddPlayer.counter_player)
        Board(board)

    def exit_game(self):
        self.destroy()

    def destroy(self):
        self.master.destroy()

    def add_player(self):
        self.login_form = Toplevel(self.master)
        self.login_form.title("Login-Mensch")
        self.login_form.geometry("700x400+300+120")
        self.login_form.resizable(0, 0)
        # self.login_form.lower(self.master)
        self.login_form.lift(self.master)

        self.label_user = Label(self.login_form, text="UserName", font="Nazli 14 bold").place(x=220, y=100)

        self.entry_user = Entry(self.login_form, fg="blue", textvariable=StringVar(), selectforeground="red", width=23)
        self.entry_user.place(x=300, y=108)

        self.label_pass = Label(self.login_form, text="PassWord", font="Nazli 14 bold").place(x=220, y=140)
        self.entry_pass = Entry(self.login_form, show="*", fg="blue", selectforeground="red", width=23)
        self.entry_pass.place(x=300, y=148)

        self.color_selection = Label(self.login_form, text="ColorPiece", font="Nazli 14 bold").place(x=220,
                                                                                                     y=180)
        self.color_select = ttk.Combobox(self.login_form, textvariable=StringVar())
        self.color_select.config(values=self.values_color, state='readonly')
        self.color_select.place(x=300, y=188)
        self.lbl_ok = Label(self.login_form)
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

        print(self.turn_player_list)
        self.frame_roll = Frame(self.frame_left, width=200, height=400)
        self.frame_roll.place(x=0, y=250)
        self.filemenu.entryconfigure(0, state=DISABLED)
        self.filemenu.entryconfigure(1, state=DISABLED)
        self.lbl_turn = Label(self.frame_roll, text="turn: BLUE", font="Nazli 20 bold")
        self.turn()
        # self.lbl_turn.pack()
        self.label_roll = Label(self.frame_roll, image=self.photo_roll_dice, width=150, height=150)
        self.label_roll.pack(pady=10, padx=10)
        self.btn_roll = Button(self.frame_roll, text="Roll", bg="skyblue", bd=4, font="Nazli 14 bold", width=8,
                               command=self.roll_dice)
        self.btn_roll.pack()
        self.lbl_roll = Label(self.frame_roll, font="Nazli 35 bold", fg="blue")
        self.lbl_roll.pack(pady=15)

    def roll_dice(self):
        self.roll_num = random.randint(1, 6)
        self.lbl_roll.configure(text=self.roll_num)
        self.turn_player += 1
        self.turn()
        print(f'turn is :{self.turn_player}')

    def func1(self, event):
        step = logic.Bbox.blue_step[logic.Bbox.blue_step.index(self.blues[0].idd) + self.roll_num]
        self.lbl_blue_1.place(x=80 * (((step+6) //7)-1) + 132, y=80 * ((step+6) % 7) + 56)
        self.blues[0].idd = step
        print("iddd is",self.blues[0].idd)
        self.lbl_blue_2.place(x=80 * (((step+6) //7)-1) + 120, y=80 * ((step+6) % 7) + 50)
        self.lbl_blue_3.place(x=600, y=300)
        self.lbl_blue_4.place(x=700, y=300)

    @staticmethod
    def callback(event):
        print("clicked on ", event.x, event.y)

    def turn(self):
        dic_colors = {"YELLOW": 'yellow', "BLUE": 'blue', "GREEN": 'green', "RED": 'red'}
        color = dic_colors[self.player_and_colors[self.turn_player % len(self.turn_player_list)][1]]
        self.lbl_turn.configure(
            text=f"TURN: {self.player_and_colors[self.turn_player % len(self.turn_player_list)][0]}", fg=color)
        self.lbl_turn.pack()

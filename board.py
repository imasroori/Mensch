from tkinter import *
import random

board = Tk()
board.title('تخته بازی')
board.geometry("950x650")
board.resizable(0, 0)

photo_roll_dice = PhotoImage(file="content/images/roll_dice.png")
photo_blue_player = PhotoImage(file="content/images/BLUE-PLYER.png", width=30, height=45)
photo_green_player = PhotoImage(file="content/images/GREEN-PLAYER.png", width=30, height=45)
photo_red_player = PhotoImage(file="content/images/RED-PLAYER.png", width=30, height=45)
photo_yellow_player = PhotoImage(file="content/images/YELLOW-PLAYER.png", width=30, height=45)


def callback(event):
    print("clicked on ", event.x, event.y)


frame_left = Frame(board, width=200, height=650)
frame_left.grid(row=0, column=0)

frame_right = Frame(board, width=750, height=650, bg="red")
frame_right.grid(row=0, column=1)

can_board = Canvas(frame_right, width=750, height=660)
can_board.pack()

can_board.create_oval(20, 40, 80, 100)
can_board.create_oval(670, 40, 730, 100)
can_board.create_oval(20, 550, 80, 610)
can_board.create_oval(670, 550, 730, 610)

lbl_blue = Label(can_board, image=photo_blue_player)
lbl_blue.place(x=32, y=46)  # x + 12  y+6
lbl_num_blue = Label(can_board, text="4", fg="white", bg="#010080")
lbl_num_blue.place(x=42, y=70)  # x+22 y+30

lbl_red = Label(can_board, image=photo_red_player)
lbl_red.place(x=682, y=46)
lbl_num_red = Label(can_board, text="4", fg="white", bg="red")
lbl_num_red.place(x=692, y=70)

lbl_green = Label(can_board, image=photo_green_player)
lbl_green.place(x=32, y=556)
lbl_num_green = Label(can_board, text="4", fg="white", bg="green")
lbl_num_green.place(x=42, y=580)

lbl_yellow = Label(can_board, image=photo_yellow_player)
lbl_yellow.place(x=682, y=556)
lbl_num_yellow = Label(can_board, text="4", fg="white", bg="yellow")
lbl_num_yellow.place(x=692, y=580)

for i in range(40, 220, 80):
    can_board.create_oval(250, i, 310, i + 60)
    if i < 180:
        can_board.create_oval(325, i, 385, i + 60)

for i in range(390, 570, 80):
    can_board.create_oval(250, i, 310, i + 60)
    if i > 430:
        can_board.create_oval(325, i, 385, i + 60)

for i in range(40, 220, 80):
    can_board.create_oval(400, i, 460, i + 60)

for i in range(390, 570, 80):
    can_board.create_oval(400, i, 460, i + 60)

for i in range(20, 200, 80):
    can_board.create_oval(i, 280, i + 60, 340)
    if i < 110:
        can_board.create_oval(i, 280, i + 60, 340)

for i in range(570, 750, 80):
    can_board.create_oval(i, 210, i + 60, 270)
    if i > 430:
        can_board.create_oval(325, i, 385, i + 60)

# for i in range(40,220,80):
#     can_board.create_oval(400, i, 460, i+60)
#
#
# for i in range(390,570,80):
#     can_board.create_oval(400, i, 460, i+60)
#


frame_panel = Frame(frame_left, width=200, height=250)
frame_panel.place(x=0, y=0)

lbl_user1 = Label(frame_panel, text="Iman", font="Nazli 18 bold")
lbl_user1.pack(padx=50, pady=2)
lbl_user2 = Label(frame_panel, text="Ali", font="Nazli 18 bold")
lbl_user2.pack(padx=50, pady=2)
lbl_user3 = Label(frame_panel, text="Amin", font="Nazli 18 bold")
lbl_user3.pack(padx=50, pady=2)
lbl_user4 = Label(frame_panel, text="Fatemeh", font="Nazli 18 bold")
lbl_user4.pack(padx=50, pady=2)

frame_roll = Frame(frame_left, width=200, height=400)
frame_roll.place(x=0, y=250)


# paned_roll = PanedWindow(frame_roll)
# paned_roll.pack()
def roll_dice():
    roll_num = random.randint(1, 6)
    lbl_roll.configure(text=roll_num)


lbl_turn = Label(frame_roll, text="turn: BLUE", font="Nazli 20 bold")
lbl_turn.pack()
label_roll = Label(frame_roll, image=photo_roll_dice, width=150, height=150)
label_roll.pack(pady=10, padx=10)
btn_roll = Button(frame_roll, text="Roll", bg="skyblue", bd=4, font="Nazli 14 bold", width=8, command=roll_dice)
btn_roll.pack()
lbl_roll = Label(frame_roll, font="Nazli 35 bold", fg="blue")
lbl_roll.pack(pady=15)

board.bind("<Button-1>", callback)

board.mainloop()

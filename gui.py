from tkinter import *

from tkinter import ttk


def quit():
    print("quit function is running!")
    login_form.destroy()


values_color = ['YELLOW', 'GREEN', 'BLUE', 'RED']


def check_user():
    username = entry_user.get()
    password = entry_pass.get()
    color_selected = color_select.get()
    values_color.remove(color_selected)
    print(values_color)
    with open("content/players_user_pass.txt", 'r') as file1:
        for line in file1:
            key, val = line.strip().split()
            print(key)
            print(val)
            if username == key and val == password:
                print("ok")
                print(username)
                print(password)
                print(color_selected)
                break
        else:
            print("نام کاربری موجود نیست!")


login_form = Tk()
login_form.title("Login-Mensch")
login_form.geometry("950x550")

photo_mensch = PhotoImage(file="content/mensch-image.png")
label_image = Label(login_form, text="Login Page", image=photo_mensch, fg="black", bd=2, relief="ridge").place(x=275)

label_user = Label(login_form, text="نام کاربری", bg="skyblue", fg="red", relief="ridge",
                   bd=2, font="Nazli 10 bold").place(x=330, y=250)

v = StringVar()
entry_user = Entry(login_form, fg="blue", textvariable=v, selectforeground="red", width=30)
entry_user.place(x=420, y=250)

label_pass = Label(login_form, text="رمز عبور", bg="skyblue", fg="red", relief="ridge",
                   bd=2, font="Nazli 10 bold").place(x=330, y=290)
entry_pass = Entry(login_form, show="*", fg="blue", selectforeground="red", width=30)
entry_pass.place(x=420, y=290)

color_selection = Label(login_form, text="رنگ مهره مورد نظر را انتخاب کنید", font="Nazli 14 bold").place(x=400, y=320)
color_select = ttk.Combobox(login_form, textvariable=StringVar())
color_select.config(values=values_color, state='readpnly')
color_select.place(x=420, y=360)

btn_enter = Button(login_form, text="ورود", bg="yellow", fg="red", font="Nazli 15 bold", activebackground="skyblue",
                   activeforeground="blue", command=check_user).place(x=400, y=400)
btn_exit = Button(login_form, text="خروج", bg="yellow", fg="red", font="Nazli 15 bold", activebackground="skyblue",
                  activeforeground="blue", command=quit).place(x=500, y=400)

login_form.mainloop()

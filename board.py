from tkinter import *

board = Tk()
board.title('تخته بازی')
board.geometry("800x500")
lable = Label(board,bg="red",bd=20,width=20,height=10).grid(row=0,column=0,padx=0,pady=0)
lable1 = Label(board,bg="green",bd=20,width=20,height=15).grid(row=1,column=0,padx=0,pady=0)
lable1 = Label(board,bg="green").grid(row=0,column=1)
lable2 = Label(board,bg="red").grid(row=0,column=2)


#### Git activate

board.mainloop()
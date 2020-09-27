import shelve,tkinter
win=tkinter.Tk()
text=tkinter.Label(text=shelve.open('game')[shelve.open('game')['scoregame']+'score'])
text.pack()
win.geometry("350x100")
win.title('Greedy Snake High Score')
win.iconbitmap('GreedySnake.ico')
tkinter.mainloop()

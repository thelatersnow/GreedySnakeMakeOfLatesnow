import tkinter,subprocess,shelve,threading,time
def greedysnake():
	subprocess.Popen(['start','greedysnake.pyw'],shell=True)
def score():
	subprocess.Popen(['start','score.pyw'],shell=True)
grid=tkinter.Grid()
tkdata=tkinter.Tk()
tkdata.title('menu')
tkdata.iconbitmap('menu.ico')
tkinter.Button(tkdata,text='Greedy Snake',command=greedysnake).pack()
tkinter.Button(tkdata,text='Greedy Snake Highscore',command=score).pack()
tkdata.geometry("210x300")
tkinter.mainloop()

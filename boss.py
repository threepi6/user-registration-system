from tkinter import *
import os
win = Tk()
x = 400
y = 160

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
pos_x = int((screen_width / 2) - (x / 2))
pos_y = int((screen_height / 2) - (y / 2))

win.geometry(f'{x}x{y}+{pos_x}+{pos_y}')
win.resizable(0,0)
win.title('Boss')
#______________________Function_______________________
def inventory():
    pathfile = os.path.dirname(__file__)
    os.system(f'python {pathfile}/Inventory.py')

def mrm():
    pathfile = os.path.dirname(__file__)
    os.system(f'python {pathfile}/MRM.py')
#______________________Widget________________________
but_inventory = Button(win,text = 'Inventory', font = 'aryal 10 bold',width = 10,command = inventory)
but_inventory.place(x = 80, y = 65)

but_mrm = Button(win,text = 'MRM', font = 'aryal 10 bold',width = 10, command = mrm)
but_mrm.place(x = 220, y = 65)
win.mainloop()
from tkinter import *
from tkinter import messagebox
import createdb
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
win.title('Login')
pathfile = os.path.dirname(__file__)
#______________________Function________________________
db1 = createdb.Database(f'{pathfile}\Company.db') 
def login():   
    username = ent_username.get()
    password = ent_password.get()
    records = db1.search_login(Employee_ID = username, ID_Number = password)
    if not  records:
        messagebox.showerror('Erorr', 'Username or password is incorrect ')
    else:
        record = db1.search_login(Employee_ID = username, ID_Number = password)
        if record[6] == 'MR Management':
            win.destroy()  
            os.system('python MRM.py')
        elif record[6] == 'Inventory':
            win.destroy()  
            os.system('python Inventory.py')
        elif record[6] == 'Boss':
            win.destroy()  
            os.system('python Boss.py')

def exit():
    anser = messagebox.askquestion('Exit', 'Do you want to exit?')
    if anser == 'yes':
        win.destroy()
#______________________Widget________________________
#___________________Labels&Entrys____________________
lbl_username = Label(win,text = 'Username: ', font = 'aryal 15 bold')
lbl_username.place(x = 25 , y = 25)

ent_username = Entry(win, font = 'aryal 15')
ent_username.place(x = 140, y = 28)


lbl_password = Label(win,text = 'Password: ', font = 'aryal 15 bold')
lbl_password.place(x = 25 , y = 65)

ent_password = Entry(win, font = 'aryal 15', show = '*')
ent_password.place(x = 140, y = 68)
#_______________________Buttons______________________
but_login = Button(win,text = 'Login', font = 'aryal 10 bold',width = 10, command = login)
but_login.place(x = 25, y = 105 )

but_exit = Button(win,text = 'Exit', font = 'aryal 10 bold',width = 10, command = exit)
but_exit.place(x = 272, y = 105 )
win.mainloop()
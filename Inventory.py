from tkinter import *
from tkinter import messagebox
from createdb import *

db = Inventory_table('E:/py/Company.db')
win = Tk()

x = 400
y = 535

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
pos_x = int((screen_width / 2) - (x / 2))
pos_y = int((screen_height / 2) - (y / 2))

win.geometry(f'{x}x{y}+{pos_x}+{pos_y}')
win.resizable(0,0)
win.title('Inventory')
#______________________________________functions________________________________________
def clear():
    ent_item_code.delete(0,END)
    ent_quantity.delete(0,END)
    ent_price.delete(0,END)
    lst.delete(0,END)

def select_record(event):
    global lstindex
    lstindex = lst.curselection()
    record = lst.get(lstindex)
    ent_item_code.insert(0,record[0])
    ent_quantity.insert(0,record[1])
    ent_price.insert(0,record[2])

def get_entrys():
    item_code = ent_item_code.get()
    quantity = ent_quantity.get()
    price = ent_price.get()
    listrecord = [item_code, quantity, price]
    return listrecord

def show_records():
    records = db.show()
    clear()
    for rec in records:
        lst.insert(END,rec)
    
def check_selection():
    if chitem_code.get() == 1:
        ch_item_code = ent_item_code.get()
    else:
        ch_item_code = ''
    
    if chquantity.get() == 1:
        ch_quantity = ent_quantity.get()
    else:
        ch_quantity = '' 
    
    if chprice.get() == 1:
        ch_chprice = ent_price.get()
    else:
        ch_chprice = ''
    
    dic_records = {'item_code' :ch_item_code, 'quantity' : ch_quantity, 'price' : ch_chprice}
    return dic_records
    
def insert_record():
    records = get_entrys()
    if records[0] == '' or records[1] == '' or records[2] == '':
        messagebox.showerror('Error', 'Fill all fields')
    elif records[1].isdigit() != True :
        messagebox.showerror('Error','quantity must be digits')
    elif records[2].isdigit() != True:
        messagebox.showerror('Error','price must be digits')
    else:
        messagebox.showinfo('Insert', f'{db.insert(records[0], int(records[1]), int(records[2]))}')
        show_records()

def update_record():
    itemcode = lst.get(lstindex)
    records = get_entrys()
    if records[0] == '' or records[1] == '' or records[2] == '':
        messagebox.showerror('Error', 'Fill all fields')
    elif records[1].isdigit() != True :
        messagebox.showerror('Error','quantity must be digits')
    elif records[2].isdigit() != True:
        messagebox.showerror('Error','price must be digits')
    elif records[0] != itemcode[0]:
        messagebox.showerror('Error', 'Item Code must not be changed')
    else:
        messagebox.showinfo('Insert', f'{db.update(itemcode[0], records[1], records[2])}')
        show_records()
    
def delete_records():
    answer = messagebox.askquestion('Delete', 'Do you want delete this record?')
    if answer == 'yes':
        item_code = lst.get(lstindex)
        messagebox.showinfo('Delete', f'{db.delete(item_code[0])}')
        clear()
        show_records()

def buy():
    records = get_entrys()
    if records[0] == '' or records[1] == '':
        messagebox.showerror('Error', 'Fill all fields')
    elif records[0].isdigit() != True:
        messagebox.showerror('Error','Item Code must be digits')
    elif records[1].isdigit() != True:
        messagebox.showerror('Error','quantity must be digits')
    else:
        item = db.sell_and_buy(records[0])
        if item:
            answer = messagebox.askquestion('Buy',f''' Item Code = {item[0]} \n Price = {item[2]}
Quantity = {records[1]} Altogether = {item[2] * int(records[1])}''')
            if answer == 'yes':
                if db.update(item[0], item[1]+ int(records[1]), item[2] ) == 'Update successful':
                    messagebox.showinfo('Buy', 'Buying successful')
                    clear()
                    show_records()
                else:
                    messagebox.showinfo('Buy', f'{db.update(item[0], item[1]+ int(records[1]), item[2])}')
                    clear()
                    show_records()
            else:
                clear()
                show_records()

def sell():
    records = get_entrys()
    if records[0] == '' or records[1] == '':
        messagebox.showerror('Error', 'Fill all fields')
    elif records[0].isdigit() != True:
        messagebox.showerror('Error','Item Code must be digits')
    elif records[1].isdigit() != True:
        messagebox.showerror('Error','quantity must be digits')
    else:
        item = db.sell_and_buy(records[0])
        if item:
            answer = messagebox.askquestion('Sell',f''' Item Code = {item[0]} \n Price = {item[2]}
Quantity = {records[1]} Altogether = {item[2] * int(records[1])}''')
            if answer == 'yes':
                if db.update(item[0], item[1]- int(records[1]), item[2] ) == 'Update successful':
                    messagebox.showinfo('Sell', 'Selling successful')
                    clear()
                    show_records()
                else:
                    messagebox.showinfo('Sell', f'{db.update(item[0], item[1]- int(records[1]), item[2])}')
                    clear()
                    show_records()
            else:
                clear()
                show_records()
def search_records(): 
    dic = check_selection()
    records = db.search(dic['item_code'], dic['quantity'], dic['price'])
    clear()
    if records:
        for rec in records:
            lst.insert(END, rec)
    else:
        lst.insert(END,'No records found.')
#___________________________________________Widgets_____________________________________
#____________________________________________Labels______________________________________
lbl_item_code = Label(win, text = 'Item Code:', font = 'aryal 13 bold')
lbl_item_code.place(x = 5, y = 5)

lbl_quantity = Label(win, text='Quantity:' , font = 'aryal 13 bold')
lbl_quantity.place(x = 5, y = 35)

lbl_price = Label(win, text = 'Price(R):', font = 'aryal 13 bold')
lbl_price.place(x = 5, y = 65 )

#___________________________________________Entrys______________________________________
ent_item_code = Entry(win, font = 'aryal 13')
ent_item_code.place(x = 100, y = 8,width = 290)

ent_quantity = Entry(win, font = 'aryal 13')
ent_quantity.place(x = 100, y = 38,width = 290)

ent_price = Entry(win, font = 'aryal 13')
ent_price.place(x = 100, y = 68,width = 290)

#__________________________________Buttons_______________________________________
but_buy = Button(win, text = 'Buy', font = 'aryal 13 bold', width = 8, command = buy)
but_buy.place(x = 5, y = 95)

but_sell = Button(win, text = 'Sell', font = 'aryal 13 bold', width = 8, command = sell)
but_sell.place(x = 105, y = 95)

but_add = Button(win, text = 'Add', font = 'aryal 13 bold', width = 8, command = insert_record)
but_add.place(x = 205, y = 95)

but_show = Button(win, text = 'Show List', font = 'aryal 13 bold', width = 8, command = show_records)
but_show.place(x = 305, y = 95)

but_update = Button(win, text = 'Update', font = 'aryal 13 bold', width = 8, command = update_record)
but_update.place(x = 5, y = 135)

but_search = Button(win, text = 'Search', font = 'aryal 13 bold', width = 8, command = search_records)
but_search.place(x = 105, y = 135)

but_delete = Button(win, text = 'Delete', font = 'aryal 13 bold', width = 8, command = delete_records)
but_delete.place(x = 205, y = 135)

but_clear = Button(win, text = 'Clear', font = 'aryal 13 bold', width = 8, command = clear)
but_clear.place(x = 305, y = 135)
#__________________________________LabelFrame_____________________________________
lblfarm_lst = LabelFrame(win,width = 390, height = 350)
lblfarm_lst.place(x = 5, y = 180)
#__________________________________Checkbuttons__________________________________
chitem_code = IntVar()
chquantity = IntVar()
chprice = IntVar()

chbut_itemcode = Checkbutton(lblfarm_lst,text = 'Item Code', font = 'aryal 10 bold',variable = chitem_code, command = check_selection)
chbut_itemcode.place(x = 65, y = 5)

chbut_quantity = Checkbutton(lblfarm_lst,text = 'Quantity', font = 'aryal 10 bold',variable = chquantity, command = check_selection)
chbut_quantity.place(x = 160, y = 5)

chbut_price = Checkbutton(lblfarm_lst,text = 'Price', font = 'aryal 10 bold',variable = chprice, command = check_selection)
chbut_price.place(x = 240, y = 5)
#__________________________________listbox_______________________________________

sb = Scrollbar(lblfarm_lst)
sb.place(x = 365, y = 40, height = 300)

lst = Listbox(lblfarm_lst,font = 'aryal 15 bold')
lst.place(x = 5, y = 40,width = 360, height = 300)

sb.config(command = lst.yview)

lst.bind('<<ListboxSelect>>', select_record)
win.mainloop()

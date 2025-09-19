from tkinter import *
from tkinter import messagebox
import os
from createdb import *
win = Tk()

pathfile = os.path.dirname(__file__)

x = 700
y = 600 
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
pos_x = int((screen_width / 2) - (x / 2))
pos_y = int((screen_height / 2) - (y / 2))

win.geometry(f"{x}x{y}+{pos_x}+{pos_y}")
win.resizable(0,0)
win.title('MR Management')
db = Mrm_table(f'{pathfile}/Company.db')
#______________________________________functions________________________________________
def clear():
    ent_name.delete(0, END)
    ent_family.delete(0, END)
    ent_phone.delete(0, END)
    ent_id_number.delete(0, END)
    ent_employee_id.delete(0, END)
    rgender.set('Male')
    rrole.set('Inventory')
    lst.delete(0, END)

def show_records():
    clear()
    record = db.show()
    for rec in record:
        lst.insert(END, rec)

def select_record(event):
    clear()
    global index
    index = lst.curselection()
    record = lst.get(index)
    ent_name.insert(END, record[0])
    ent_family.insert(END, record[1])
    ent_phone.insert(END, record[2])
    ent_id_number.insert(END, record[3])
    ent_employee_id.insert(END, record[4])

def get_entry():
    name = ent_name.get()
    family = ent_family.get()
    phone = ent_phone.get()
    idnumber = ent_id_number.get()
    employee = ent_employee_id.get()
    gender = rgender.get()
    role = rrole.get()
    lst_get=[name, family, phone, idnumber, employee, gender, role]
    return lst_get

def insert_record():
    lst_get = get_entry()
    if lst_get[0] == '' or lst_get[1] == '' or lst_get[2] == '' or lst_get[3] == '' or lst_get[4] == '':
        messagebox.showerror('Error', 'Fill all fields')
    elif lst_get[2].isdigit() == False or len(lst_get[2]) != 11:
        messagebox.showerror('Error','Phone number must be 11 digits')
    elif lst_get[3].isdigit() == False or len(lst_get[3]) != 10:
        messagebox.showerror('Error','ID Number must be 10 digits')
    else:
        anser = messagebox.askquestion('Information',f'''Name: {lst_get[0]}\nFamliy: {lst_get[1]}\n Phone: {lst_get[2]}\nID Number: {lst_get[3]}
                                       \nEmployee ID: {lst_get[4]}\nGender: {lst_get[5]}\nRole: {lst_get[6]}
                                        \n Are you sure?''')
        if anser == 'yes':
            messagebox.showinfo('Insert',f'{db.insert(lst_get[0], lst_get[1], 
                                                      lst_get[2], lst_get[3], lst_get[4], lst_get[5], lst_get[6])}')
            clear()
            show_records()

def update_records():
    recored = lst.get(index)
    lst_get = get_entry()
    if lst_get[0] == '' or lst_get[1] == '' or lst_get[2] == '' or lst_get[3] == '' or lst_get[4] == '':
        messagebox.showerror('Error', 'Fill all fields')
    elif lst_get[2].isdigit() == False or len(lst_get[2]) != 11:
        messagebox.showerror('Error','Phone number must be 11 digits')
    elif lst_get[3].isdigit() == False or len(lst_get[3]) != 10:
        messagebox.showerror('Error','ID Number must be 10 digits')
    elif lst_get[4] != recored[4]:
        messagebox.showerror('Error', 'Employee ID must not be changed')
    else:
        messagebox.showinfo('Update',f'{db.update(lst_get[0], lst_get[1], lst_get[2], lst_get[3], lst_get[5], lst_get[6], lst_get[4])}')
        show_records()
        clear()

def delete_record():
    answer = messagebox.askquestion('Delete', 'Do you want delete this record?')
    if answer == 'yes':
        recored = lst.get(index)
        messagebox.showinfo('Exit',f'{db.delete(recored[4])}')
        clear()
        show_records()

def check_selection():
    if chname.get() == 1:
        ch_name = ent_name.get()
    else:
        ch_name = ''
    
    if chfamily.get() == 1:
        ch_family = ent_family.get()
    else:
        ch_family = '' 
    
    if chphone.get() == 1:
        ch_phone = ent_phone.get()
    else:
        ch_phone = ''
    
    if chidnumber.get() == 1:
        ch_idnumber = ent_id_number.get()
    else:
        ch_idnumber = ''
    
    if chemployeeid.get() == 1:
        ch_emoliyee = ent_employee_id.get()
    else:
        ch_emoliyee = ''

    if chgender.get() == 1:
        ch_gemder = rgender.get()
    else:
        ch_gemder = ''

    if chrole.get() == 1:
        ch_role = rrole.get()
    else:
        ch_role = ''

    dic_records = {'name' : ch_name, 'family' : ch_family, 'phone' : ch_phone, 'idnumber' : ch_idnumber,
                   'employeeid' : ch_emoliyee, 'gender' : ch_gemder, 'role' : ch_role}
    
    return dic_records

def search_records():
    dic = check_selection()
    records = db.search(dic['name'], dic['family'], dic['phone'], dic['idnumber'], 
                        dic['employeeid'], dic['gender'], dic['role'])
    clear()
    if records:
        for rec in records:
            lst.insert(END, rec)
    else:
        lst.insert(END,'No records found.')
#___________________________________________Widgets_____________________________________
#___________________________________________Labels______________________________________
lbl_name = Label(win, text = 'Name:', font = 'aryal 13 bold')
lbl_name.place(x = 5, y = 5)

lbl_family = Label(win, text = 'Family:', font = 'aryal 13 bold')
lbl_family.place(x = 5, y = 35)

lbl_phone = Label(win, text = 'Phone:', font = 'aryal 13 bold')
lbl_phone.place(x = 5, y = 65)

lbl_id_number = Label(win, text = 'ID Number:', font = 'aryal 13 bold')
lbl_id_number.place(x = 5, y = 95)

lbl_employee_id = Label(win, text = 'Employee ID:', font = 'aryal 13 bold')
lbl_employee_id.place(x = 5, y = 125)

#___________________________________________Entrys______________________________________
ent_name = Entry(win, font = 'aryal 13 bold')
ent_name.place(x =120, y = 8 )

ent_family = Entry(win, font = 'aryal 13 bold')
ent_family.place(x =120, y = 38)

ent_phone = Entry(win, font = 'aryal 13 bold')
ent_phone.place(x =120, y = 68)

ent_id_number = Entry(win, font = 'aryal 13 bold')
ent_id_number.place(x =120, y = 98 )

ent_employee_id = Entry(win, font = 'aryal 13 bold')
ent_employee_id.place(x =120, y = 128 )

#__________________________________LabelFrame_Gender_______________________________________
lblfarm_gender = LabelFrame(text = 'Gender', font = 'aryal 10 bold' ,width = 382, height = 75)
lblfarm_gender.place(x = 310, y = 5)

rgender = StringVar()
rgender.set('Male')

rmale = Radiobutton(lblfarm_gender, text = 'Male', font = 'aryal 10 bold', variable = rgender, value = 'Male')
rmale.place(x = 50, y = 10)

rfemale = Radiobutton(lblfarm_gender, text = 'Female', font = 'aryal 10 bold', variable = rgender, value = 'Female')
rfemale.place(x = 250, y = 10)

#__________________________________LabelFrame_Role_______________________________________
lblfarm_role = LabelFrame(text = 'Role', font = 'aryal 10 bold' ,width = 382, height = 75)
lblfarm_role.place(x = 310, y = 80)

rrole = StringVar()
rrole.set('Inventory')

rinventory = Radiobutton(lblfarm_role, text = 'Inventory', font = 'aryal 10 bold', variable = rrole, value = 'Inventory')
rinventory.place(x = 10, y = 10)

rmrm = Radiobutton(lblfarm_role, text = 'MR Management', font = 'aryal 10 bold', variable = rrole, value = 'MR Management')
rmrm.place(x = 130, y = 10)

rboss = Radiobutton(lblfarm_role, text = 'Boss', font = 'aryal 10 bold', variable = rrole, value = 'Boss')
rboss.place(x = 300, y = 10)
#__________________________________Buttons_______________________________________
but_insert = Button(win, text = 'Insert', font = 'aryal 13 bold', width = 8, command = insert_record)
but_insert.place(x = 50, y = 160)

but_update = Button(win, text = 'Update', font = 'aryal 13 bold', width = 8, command = update_records )
but_update.place(x = 150, y = 160)

but_delete = Button(win, text = 'Delete', font = 'aryal 13 bold', width = 8, command = delete_record)
but_delete.place(x = 250, y = 160)

but_search = Button(win, text = 'Search', font = 'aryal 13 bold', width = 8, command = search_records)
but_search.place(x = 350, y = 160)

but_show = Button(win, text = 'Show List', font = 'aryal 13 bold', width = 8, command = show_records)
but_show.place(x = 450, y = 160)

but_clear = Button(win, text = 'Clear', font = 'aryal 13 bold', width = 8, command = clear)
but_clear.place(x = 550, y = 160)
#__________________________________LabelFrame_search_and_listbox_______________________________________
lblfarm_search = LabelFrame(win, width = 690, height = 390,)
lblfarm_search.place(x = 5, y = 200)

#__________________________________________Checkbuttons_________________________________________________
chname = IntVar()
chfamily = IntVar()
chphone = IntVar()
chidnumber = IntVar()
chemployeeid = IntVar()
chgender = IntVar()
chrole = IntVar()

chbut_name = Checkbutton(lblfarm_search, text = 'Name', font = 'aryal 10 bold',variable = chname,command = check_selection)
chbut_name.place(x = 55, y = 5)

chbut_family = Checkbutton(lblfarm_search, text = 'Family', font = 'aryal 10 bold', variable = chfamily, command = check_selection)
chbut_family.place(x = 120, y = 5)

chbut_phone = Checkbutton(lblfarm_search, text = 'Phone', font = 'aryal 10 bold', variable = chphone, command = check_selection)
chbut_phone.place(x = 195, y = 5)

chbut_idnumber = Checkbutton(lblfarm_search, text = 'ID Number', font = 'aryal 10 bold', variable = chidnumber, command = check_selection)
chbut_idnumber.place(x = 270, y = 5)

chbut_employeeid = Checkbutton(lblfarm_search, text = 'Employee ID', font = 'aryal 10 bold', variable = chemployeeid, command = check_selection)
chbut_employeeid.place(x = 370, y = 5)

chbut_gender = Checkbutton(lblfarm_search, text = 'Gender', font = 'aryal 10 bold', variable = chgender, command = check_selection)
chbut_gender.place(x = 480, y = 5)

chbut_role = Checkbutton(lblfarm_search, text = 'Role', font = 'aryal 10 bold', variable = chrole, command = check_selection)
chbut_role.place(x = 560, y = 5)

#__________________________________Buttons_______________________________________
slst = Scrollbar(lblfarm_search)
slst.place(x = 659, y = 35, height = 345 )

lst = Listbox(lblfarm_search, font = 'aryal 15 bold', yscrollcommand = slst.set)
lst.place(x = 5, y = 35, width = 655, height = 345)

slst.config(command = lst.yview)
lst.bind('<<ListboxSelect>>', select_record)
win.mainloop()

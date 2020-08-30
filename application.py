from tkinter import Tk, StringVar, Label, Listbox, Entry, W, Scrollbar, Button, END, messagebox
from db import Database

db = Database('student-data.db')

def populate_list():
    student_list.delete(0, END)
    for row in db.fetch():
        student_list.insert(END, row)

def add_item():
    if name_text.get() == "" or grade_text.get() =="":
        messagebox.showerror('Required Fields', 'Fields can not be left empty')
        return
    db.insert(name_text.get(), grade_text.get())
    student_list.delete(0, END)
    student_list.insert(END, (name_text.get(), grade_text.get()))
    clear_text()
    populate_list()

def select_item(event):
    global selected_item
    index = student_list.curselection()[0]
    selected_item = student_list.get(index)

    name_entry.delete(0,END)
    name_entry.insert(END, selected_item[1])
    grade_entry.delete(0,END)
    grade_entry.insert(END, selected_item[2])

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0],name_text.get(), grade_text.get() )
    remove_item()
    populate_list()


def clear_text():
    name_entry.delete(0,END)
    grade_entry.delete(0,END)

#create window object
app = Tk()

#name :
name_text = StringVar()
name_label = Label(app, text='Student Name', font=('bold', 12), pady=20)
name_label.grid(row=0, column=0, sticky=W)
name_entry = Entry(app, text=name_text)
name_entry.grid(row=0, column=1)

#Grade :
grade_text = StringVar()
grade_label = Label(app, text='Student Grade', font=('bold', 12))
grade_label.grid(row=0, column=2, sticky=W)
grade_entry = Entry(app, text=grade_text)
grade_entry.grid(row=0, column=3)

#listBox
student_list = Listbox(app ,height=10, width=70, border=0)
student_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

#create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

#set scroll to listbox:
student_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=student_list.yview)

#bind select
student_list.bind('<<ListboxSelect>>', select_item)
#buttons:
add_btn = Button(app, text='Add Student', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Student', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)


app.title('Student Data Manager')
app.geometry('600x300')

populate_list()

#start program
app.mainloop()



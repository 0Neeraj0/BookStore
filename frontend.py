"""
A program that stores the books information
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add entry
Delete
Close
"""

from tkinter import *
import backend

def get_selected_row(event):
    if list1.size()==0:
        return
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    results=backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    for row in results:
        list1.insert(END, row)

def add_command():
    if title_text.get()!="" and author_text.get()!="" and year_text.get()!="" and isbn_text.get()!="":
        backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        list1.delete(0, END)
        list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    else:
        return

def update_command():
    if list1.size()==0:
        return
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def delete_command():
    if list1.size()==0:
        return
    backend.delete(selected_tuple[0])

# def is_not_convertable_to_int(input_string):
#     try:
#         int(input_string)
#         return False
#     except ValueError:
#         return True;

window=Tk()

window.wm_title("BookStore")

l1=Label(window, text="Title")
l1.grid(row=0, column=0)

l1=Label(window, text="Author")
l1.grid(row=0, column=2)

l1=Label(window, text="Year")
l1.grid(row=1, column=0)

l1=Label(window, text="ISBN")
l1.grid(row=1, column=2)

title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)


author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# if is_not_convertable_to_int(year_text.get() and year_text.get()!=""):
#     top=Toplevel(window)
#     top.title("Error")
#     Label(top, text="Invalid Inpute for Year, Year should be Integer").place(x=150, y=80)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)


sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)


b1=Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)




window.mainloop()

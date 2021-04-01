import pymongo
from pymongo import MongoClient
import pyperclip
import random_password_generator
from tkinter import *
from tkinter import messagebox

# Event for button_close
def closeWindow():
    root.destroy()

# Event for button_send
def send_request():
    radio = r.get()
    entry = entry_input.get()
    new_password = ''

    if entry.strip() == '':
        messagebox.showerror('Invalid Input', 'Text box is empty...')
    else:
        if radio == 1:
            new_password = random_password_generator.create_password(new_password)
            collection.insert_one({ "_id": f'{entry}', "password": f"{new_password}" })
            label_password.config(text=new_password)
            pyperclip.copy(new_password)
            msg_added = messagebox.showinfo('Success!', 'Password added successfully to database!')
        elif radio == 2:
            result = collection.find_one({"_id": f"{entry}"})
            label_password.config(text=result['password'])
            pyperclip.copy(result['password'])
            messagebox.showinfo('Success!', 'Password added to clipboard!')
        elif radio == 3:
            result = collection.delete_one({"_id": f"{entry}"})
            delete = messagebox.showinfo('Success!', 'Password successfully deleted!')
        else:
            error = messagebox.showerror('Error','Nothing selected...')

def show_all():
    id_list = []
    password_list = []
    current_line = []

    results = collection.find()
    for result in results:
        id_list.append(result['_id'])
        password_list.append(result['password'])
    
    if len(id_list) == 0 and len(password_list) == 0:
        messagebox.showwarning('Empty List', 'No passwords detected...')
    else:
        for x in range(0, len(id_list)):
            current_line.append(f'{id_list[x].capitalize()}: {password_list[x]}')
        print_box = '\n'.join(current_line)
        messagebox.showinfo('Password List', print_box)

# MongoDB Access
cluster = MongoClient("*Input URL to MongoDB database here*")
db = cluster["*Input Cluster name here*"]
collection = db["*Input Collection name here*"]
id = 0
password = ''

# Tkinter Window Config
root = Tk()
root.title('Password Manager')
root.iconbitmap('*path to*password.ico')

# Radio button frame
frame_radio = LabelFrame(root)
frame_radio.pack(side=LEFT, fill=Y, padx=5, pady=5)
frame_input = LabelFrame(root)
frame_input.pack(side=RIGHT, fill=Y, padx=5, pady=5)

r = IntVar()

# Radio buttons
radio_new_password = Radiobutton(frame_radio, variable=r, value=1, text='New Password', font=('Helvetica', 12))
radio_new_password.pack()

radio_get_password = Radiobutton(frame_radio, variable=r, value=2, text='Access Password', font=('Helvetica', 12))
radio_get_password.pack()

radio_del_password = Radiobutton(frame_radio, variable=r, value=3, text='Delete Password', font=('Helvetica', 12))
radio_del_password.pack()

# Text inputs/outputs
label_input = Label(frame_input, text='Account:')
label_input.grid()
entry_input = Entry(frame_input)
entry_input.grid(column=1, row=0, padx=5, pady=5)

label_output = Label(frame_input, text='Password:')
label_output.grid(column=0, row=1)
label_password = Label(frame_input)
label_password.grid(column=1, row=1, padx=5, pady=5)

# Close window button
button_close = Button(frame_input, text='Close', font=('Helvetica', 12), command=closeWindow)
button_close.grid(column=0, row=2, pady=5)

# Send request button
button_send = Button(frame_input, text='Send Request', font=('Helvetica', 12), command=send_request)
button_send.grid(column=1, row=2, pady=5)

# Show all passwords button
button_show_all = Button(frame_radio, text='Show Passwords', font=('Helvetica', 12), command=show_all)
button_show_all.pack(pady=5)

root.mainloop()
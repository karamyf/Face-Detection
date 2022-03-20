import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import shutil
import os
import sys

"""


print('''
    1. Display Face List
    2. Display Unknown List
    3. Exit
    ''')
choice = int(input("Enter Your Choice : "))
src = os.path.abspath (sys.argv[0])
if( choice == 1 ) :
    #os.startfile('images')
    dir = os.startfile('images')
    saveloc = os.path.dirname(os.path.realpath(src))
    print(saveloc)
if( choice == 2 ) :
    os.startfile('dataset') 
if( choice == 3 ) :
    exit()


"""
cam_num = 0
#Change Default Camera
#answer = input("Do you Want to Change Default Camera y/n : ")
#if ( answer == "y" or answer == "yes" or answer == "Y" or answer == "YES" ):
#    cam_num = int(input("Enter Camera Port: "))



# create the main window
mainwindow = tk.Tk()
mainwindow.title('Tkinter Open File Dialog')
mainwindow.resizable(False, False)
mainwindow.geometry('300x150')
name_var = tk.StringVar()

def select_file():
    global filename
    filetypes = (
        ('image files', '*.jpg'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='dataset',
        filetypes=filetypes)

    path_of_file = filename

    return filename

def rename_file():
    name = name_var.get()
    dst_path = r"C:\Users\Karam\Desktop\Work\Python Projects\source code\images"
    destination = os.path.join(dst_path, name+ ".jpg")
    os.rename(filename, destination)

# open button

open_button = ttk.Button(
    mainwindow,
    text='Open a File',
    command=lambda:[select_file()],

)


# creating a label for
# name using widget Label
name_label = tk.Label(mainwindow, text='Name', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(mainwindow, textvariable=name_var, font=('calibre', 10, 'normal'))



sub_btn = tk.Button(mainwindow, text='Submit', command=rename_file)

open_button.grid(row=0, column=1)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# run the application
mainwindow.mainloop()

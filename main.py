from tkinter import *
from tkinter import font
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

#creating the window
root = Tk()
root.title("Art Tracker")
root.geometry("1000x625")
root.configure(bg='#9399AC')

root.columnconfigure(0,weight=7) 
root.columnconfigure(1,weight=1) 
root.columnconfigure(2,weight=1) 
root.columnconfigure(3,weight=1) 
root.rowconfigure(0, weight=1) 
root.rowconfigure(1, weight=1) 
root.rowconfigure(2, weight=1) 


#changing the icon
photo = ImageTk.PhotoImage(Image.open("ArtTracker/resources/painticon.ico"))
root.wm_iconphoto(False, photo)
#https://www.flaticon.com/free-icon/paint-brush_587377


#formatting the artworks window
bg_frame = LabelFrame(root, padx=0, pady=30, bg='#7B8292', bd=0)
bg_frame.grid(row=0, column=0, padx=50, pady=50, sticky="NESW", rowspan=3)

#creating the item frames
item_frame_1 = LabelFrame(bg_frame, padx=10, pady=10, bg='#4D5660', bd=0)
item_frame_1.grid(row=0, column=1, sticky="NESW", padx=10, pady=10)
item_frame_2 = LabelFrame(bg_frame, padx=10, pady=10, bg='#4D5660', bd=0)
item_frame_2.grid(row=1, column=1, sticky="NESW", padx=10, pady=10)
item_frame_3 = LabelFrame(bg_frame, padx=10, pady=10, bg='#4D5660', bd=0)
item_frame_3.grid(row=2, column=1, sticky="NESW", padx=10, pady=10)
item_frame_4 = LabelFrame(bg_frame, padx=10, pady=10, bg='#4D5660', bd=0)
item_frame_4.grid(row=3, column=1, sticky="NESW", padx=10, pady=10)
item_frame_5 = LabelFrame(bg_frame, padx=10, pady=10, bg='#4D5660', bd=0)
item_frame_5.grid(row=4, column=1, sticky="NESW", padx=10, pady=10)

bg_frame.columnconfigure(0,weight=1)
bg_frame.columnconfigure(1,weight=6)
bg_frame.columnconfigure(2,weight=1)

bg_frame.rowconfigure(0,weight=1) 
bg_frame.rowconfigure(1,weight=1) 
bg_frame.rowconfigure(2,weight=1) 
bg_frame.rowconfigure(3,weight=1) 
bg_frame.rowconfigure(4,weight=1) 

forward_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/forward_icon.png"))
back_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/back_icon.png"))

forward_button = Button(bg_frame, text=">", image=forward_img, bg='#7B8292', bd=0)
forward_button.grid(row=2, column=2, sticky="NESW")
back_button = Button(bg_frame, text=">", image=back_img, bg='#7B8292', bd=0)
back_button.grid(row=2, column=0, sticky="NESW")


item_frame_1.rowconfigure(0,weight=1)
item_frame_2.rowconfigure(0,weight=1) 
item_frame_3.rowconfigure(0,weight=1) 
item_frame_4.rowconfigure(0,weight=1) 
item_frame_5.rowconfigure(0,weight=1) 


placeholder_1 = Label(item_frame_1, text="Placeholder", fg='white', bg='#4D5660', font=("Segoe UI Black", 18))
placeholder_1.pack(side=LEFT)
placeholder_2 = Label(item_frame_2, text="Placeholder", fg='white', bg='#4D5660', font=("Segoe UI Black", 18))
placeholder_2.pack(side=LEFT)
placeholder_3 = Label(item_frame_3, text="Placeholder", fg='white', bg='#4D5660', font=("Segoe UI Black", 18))
placeholder_3.pack(side=LEFT)
placeholder_4 = Label(item_frame_4, text="Placeholder", fg='white', bg='#4D5660', font=("Segoe UI Black", 18))
placeholder_4.pack(side=LEFT)
placeholder_5 = Label(item_frame_5, text="Placeholder", fg='white', bg='#4D5660', font=("Segoe UI Black", 18))
placeholder_5.pack(side=LEFT)


delete_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/delete_icon.png"))

delete_1 = Button(item_frame_1, bd=0, text="Delete", image=delete_img, bg='#9399AC')
delete_1.pack(side=RIGHT)
delete_2 = Button(item_frame_2, bd=0, text="Delete", image=delete_img, bg='#9399AC')
delete_2.pack(side=RIGHT)
delete_3 = Button(item_frame_3, bd=0, text="Delete", image=delete_img, bg='#9399AC')
delete_3.pack(side=RIGHT)
delete_4 = Button(item_frame_4, bd=0, text="Delete", image=delete_img, bg='#9399AC')
delete_4.pack(side=RIGHT)
delete_5 = Button(item_frame_5, bd=0, text="Delete", image=delete_img, bg='#9399AC')
delete_5.pack(side=RIGHT)


edit_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/edit_icon.png"))

edit_1 = Button(item_frame_1, bd=0, text="Edit", image=edit_img, bg='#9399AC')
edit_1.pack(side=RIGHT, padx=10)
edit_2 = Button(item_frame_2, bd=0, text="Edit", image=edit_img, bg='#9399AC')
edit_2.pack(side=RIGHT, padx=10)
edit_3 = Button(item_frame_3, bd=0, text="Edit", image=edit_img, bg='#9399AC')
edit_3.pack(side=RIGHT, padx=10)
edit_4 = Button(item_frame_4, bd=0, text="Edit", image=edit_img, bg='#9399AC')
edit_4.pack(side=RIGHT, padx=10)
edit_5 = Button(item_frame_5, bd=0, text="Edit", image=edit_img, bg='#9399AC')
edit_5.pack(side=RIGHT, padx=10)


#create save functions
def save_original():
    creation_window.destroy()
    return

def save_fanart():
    creation_window.destroy()
    return



#create artwork function
def artwork_info_window(arttype, action):
    global creation_window
    creation_window = Toplevel(root)
    creation_window.title("Create Artwork")
    creation_window.geometry("1000x625")
    creation_window.configure(bg='#7B8292')
    creation_window.wm_iconphoto(False, photo)
    creation_window.grab_set()

    #configuring the main grid 
    creation_window.columnconfigure(0,weight=1) 
    creation_window.columnconfigure(1,weight=1) 
    creation_window.columnconfigure(2,weight=1) 
    creation_window.columnconfigure(3,weight=7) 
    creation_window.rowconfigure(0, weight=1) 
    creation_window.rowconfigure(1, weight=1) 
    creation_window.rowconfigure(2, weight=1) 

    #creating the frame where the information will be input
    info_frame = LabelFrame(creation_window, padx=20, pady=10, bg='#9399AC', bd=0)
    info_frame.grid(row=0, column=3, padx=50, pady=50, sticky="NESW", rowspan=3)
    
    info_frame.columnconfigure(0,weight=1)
    info_frame.columnconfigure(1,weight=1)
    info_frame.rowconfigure(0,weight=1)
    info_frame.rowconfigure(1,weight=1)
    info_frame.rowconfigure(2,weight=1)
    info_frame.rowconfigure(3,weight=1)
    info_frame.rowconfigure(4,weight=1)
    info_frame.rowconfigure(5,weight=1)
    info_frame.rowconfigure(6,weight=1)
    info_frame.rowconfigure(7,weight=1)

    #creating the labels and entries
    name_lbl = Label(info_frame, text="Name", bg='#9399AC', fg='#4D5660', font=("Segoe UI Black", 22))
    name_lbl.grid(row=0, column=0, sticky="W")
    name_inp = Entry(info_frame, width=50, bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 16))
    name_inp.grid(row=1, column=0, sticky="W", padx=(2, 50))

    status_lbl = Label(info_frame, text="Status", bg='#9399AC', fg='#4D5660', font=("Segoe UI Black", 22))
    status_lbl.grid(row=2, column=0, sticky="W")
    status_inp = Entry(info_frame, width=50, bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 16))
    status_inp.grid(row=3, column=0, sticky="W", padx=(2, 50))

    medium_lbl = Label(info_frame, text="Medium", bg='#9399AC', fg='#4D5660', font=("Segoe UI Black", 22))
    medium_lbl.grid(row=4, column=0, sticky="W")
    medium_inp = Entry(info_frame, width=50, bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 16))
    medium_inp.grid(row=5, column=0, sticky="W", padx=(2, 50))

    #ORIGINAL ARTWORK
    if arttype == 'original':
        subject_lbl = Label(info_frame, text="Subject", bg='#9399AC', fg='#4D5660', font=("Segoe UI Black", 22))
        subject_lbl.grid(row=6, column=0, sticky="W")
        subject_inp = Entry(info_frame, width=50, bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 16))
        subject_inp.grid(row=7, column=0, sticky="W", padx=(2, 50), pady=(0, 20))

        desc_lbl = Label(info_frame, text="Description", bg='#9399AC', fg='#4D5660', font=("Segoe UI Black", 22))
        desc_lbl.grid(row=0, column=1, padx=0, pady=0, sticky="W")
        desc_inp = Entry(info_frame, width=50, bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 16))
        desc_inp.grid(row=1, column=1, sticky="W", padx=(2, 50))

        if action == 'create' or action == 'edit':
            save_bg = Frame(info_frame, bg='#FFFFFF', bd=5) 
            save_bg.grid(row=2, column=1, sticky="W", pady=0, rowspan=2)
            save_btn = Button(save_bg, text="Save", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=save_original)
            save_btn.grid(row=0, column=0, padx=0, pady=0, sticky="W")


    #FANART
    else:
        fandom_lbl = Label(info_frame, text="Fandom", bg='#9399AC', fg='#4D5660', font=("Segoe UI Black", 22))
        fandom_lbl.grid(row=6, column=0, sticky="W")
        fandom_inp = Entry(info_frame, width=50, bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 16))
        fandom_inp.grid(row=7, column=0, sticky="W", padx=(2, 50), pady=(0, 20))

        character_lbl = Label(info_frame, text="Character", bg='#9399AC', fg='#4D5660', font=("Segoe UI Black", 22))
        character_lbl.grid(row=0, column=1, padx=0, pady=0, sticky="W")
        character_inp = Entry(info_frame, width=50, bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 16))
        character_inp.grid(row=1, column=1, sticky="W", padx=(2, 50))

        desc_lbl = Label(info_frame, text="Description", bg='#9399AC', fg='#4D5660', font=("Segoe UI Black", 22))
        desc_lbl.grid(row=2, column=1, padx=0, pady=0, sticky="W")
        desc_inp = Entry(info_frame, width=50, bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 16))
        desc_inp.grid(row=3, column=1, sticky="W", padx=(2, 50))

        if action == 'create' or action == 'edit':
            save_bg = Frame(info_frame, bg='#FFFFFF', bd=5) 
            save_bg.grid(row=4, column=1, sticky="W", pady=0, rowspan=2)
            save_btn = Button(save_bg, text="Save", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=save_fanart)
            save_btn.grid(row=0, column=0, padx=0, pady=0, sticky="W")






#creating the options functionality
def choose_arttype():
    arttype_dialog = Toplevel(root)
    arttype_dialog.title("Choose art type")
    arttype_dialog.geometry("400x200")
    arttype_dialog.configure(bg='#9399AC')
    arttype_dialog.wm_iconphoto(False, photo)
    arttype_dialog.grab_set()

    arttype_dialog.rowconfigure(0, weight=1) 
    arttype_dialog.columnconfigure(0, weight=1) 
    arttype_dialog.columnconfigure(1, weight=1) 

    def original_press():
        arttype_dialog.destroy()
        artwork_info_window('original', 'create')
        
    
    def fanart_press():
        arttype_dialog.destroy()
        artwork_info_window('fanart', 'create')
        


    original_btn = Button(arttype_dialog, text="Original", bg='#4D5660', fg='#FFFFFF', bd=0, command=original_press, font=("Segoe UI Black", 18))
    original_btn.grid(row=0, column=0, padx=10, pady=10, sticky="NESW")
    fanart_btn = Button(arttype_dialog, text="Fanart", bg='#4D5660', fg='#FFFFFF', bd=0, command=fanart_press, font=("Segoe UI Black", 18))
    fanart_btn.grid(row=0, column=1, padx=10, pady=10, sticky="NESW")

    



#formatting the options strip
options_frame = LabelFrame(root, padx=30, pady=30, bg='#4D5660', bd=0)
options_frame.grid(row=0, column=2, sticky="NESW", rowspan=3)

#options
filter_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/filter_icon.png"))
add_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/add_img.png"))



filter_bg = Frame(root, bg='#FFFFFF', bd=0) 
filter_bg.grid(row=0, column=1, padx=10, pady=10, columnspan=3)
add_bg = Frame(root, bg='#FFFFFF', bd=0) 
add_bg.grid(row=1, column=1, padx=10, pady=10, columnspan=3)


filter_btn = Button(filter_bg, relief='flat', text="Search", image=filter_img, bg='#E2CDB4', bd=10)
filter_btn.grid(row=0, column=0, padx=10, pady=10)
add_btn = Button(add_bg, relief='flat', text="Add", image=add_img, bg='#E2CDB4', bd=10, command=choose_arttype)
add_btn.grid(row=0, column=0, padx=10, pady=10)


root.mainloop()
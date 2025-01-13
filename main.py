from tkinter import *
from tkinter import font
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime

#creating classes 
#artwork parent class
class Artwork:
    def __init__(self, name, desc, status, medium, creation_date=None):
        self.name = name
        self.desc = desc
        self.status = status
        self.medium = medium
        if creation_date == None:
            self.creation_date = datetime.date.today()
        else:
            self.creation_date = creation_date
    def update(self, name, desc, status, medium):
        self.name = name
        self.desc = desc
        self.status = status
        self.medium = medium


#fanart subclass
class Fanart(Artwork):
    def __init__(self, name, desc, status, medium, fandom, character, creation_date=None):
        super().__init__(name, desc, status, medium, creation_date=creation_date)
        self.fandom = fandom
        self.character = character
    def update(self, name, desc, status, medium, fandom, character):
        super().update(name, desc, status, medium)
        self.fandom = fandom
        self.character = character

#original subclass
class Original(Artwork):
    def __init__(self, name, desc, status, medium, subject, creation_date=None):
        super().__init__(name, desc, status, medium, creation_date=creation_date)
        self.subject = subject
    def update(self, name, desc, status, medium, subject):
        super().update(name, desc, status, medium)
        self.subject = subject


#reading from a CSV for data storage
def read_csv():
    fanart_list = []
    original_list = []

    #format of each line: type, name, desc, status, medium, subject, fandom, character, creation_date
    with open("ArtTracker/resources/artworks.txt", "r") as readingFile:
        
        stored_artworks = readingFile.readlines()
        #recreates the objects from info in the file
        for artwork_line in stored_artworks:
            attributes_list = artwork_line.split(', ')

            if attributes_list[0] == 'original':
                fetched_original = Original(attributes_list[1], attributes_list[2], attributes_list[3], attributes_list[4], attributes_list[5], (attributes_list[-1])[:-1])
                original_list.append(fetched_original)
            else:
                fetched_fanart = Fanart(attributes_list[1], attributes_list[2], attributes_list[3], attributes_list[4], attributes_list[6], attributes_list[7], (attributes_list[-1])[:-1])
                fanart_list.append(fetched_fanart)
                
    return fanart_list, original_list


#returning current objects to the csv
def write_csv(fanart_list, original_list):
    #format of each line: type, name, desc, status, medium, subject, fandom, character, creation_date
    fanart_string = ""
    original_string = ""

    for fanart in fanart_list:
        fanart_string += f"fanart, {fanart.name}, {fanart.desc}, {fanart.status}, {fanart.medium}, None, {fanart.fandom}, {fanart.character}, {fanart.creation_date}\n"
    for original in original_list:
        original_string += f"original, {original.name}, {original.desc}, {original.status}, {original.medium}, {original.subject}, None, None, {original.creation_date}\n"
    file_string = fanart_string + original_string[:-1]

    with open("ArtTracker/resources/artworks.txt", "w") as writing_file:
        writing_file.write(file_string)




#creating the tkinter window
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


#save database functions
def save_original():
    creation_window.destroy()
    return

def save_fanart():
    creation_window.destroy()
    return

#update database functions
def update_original(artwork_id):
    creation_window.destroy()
    return

def update_fanart(artwork_id):
    creation_window.destroy()
    return

#filter database functions
def filter_originals():
    creation_window.destroy()
    return

def filter_fanarts(d):
    creation_window.destroy()
    return





#artwork info window
def artwork_info_window(arttype, action, artwork_id=None):
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

        btn_bg = Frame(info_frame, bg='#FFFFFF', bd=5) 
        btn_bg.grid(row=2, column=1, sticky="W", pady=0, rowspan=2)

        if action == 'create':
            save_btn = Button(btn_bg, text="Save", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=save_original)
            save_btn.grid(row=0, column=0, padx=0, pady=0, sticky="W")
        elif action == 'edit':
            update_btn = Button(btn_bg, text="Update", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=lambda: update_original('placeholder'))
            update_btn.grid(row=0, column=0, padx=0, pady=0, sticky="W")
        elif action == 'filter':
            save_btn = Button(btn_bg, text="Go", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=filter_originals)
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

        btn_bg = Frame(info_frame, bg='#FFFFFF', bd=5) 
        btn_bg.grid(row=4, column=1, sticky="W", pady=0, rowspan=2)

        if action == 'create':
            save_btn = Button(btn_bg, text="Save", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=save_fanart)
            save_btn.grid(row=0, column=0, padx=0, pady=0, sticky="W")
        elif action == 'edit':
            save_btn = Button(btn_bg, text="Update", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=lambda: update_fanart('placeholder'))
            save_btn.grid(row=0, column=0, padx=0, pady=0, sticky="W")
        elif action == 'filter':
            filter_btn = Button(btn_bg, text="Go", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=filter_fanarts)
            filter_btn.grid(row=0, column=0, padx=0, pady=0, sticky="W")






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


placeholder_1 = Button(item_frame_1, text="Placeholder", fg='white', bg='#4D5660', relief='flat', font=("Segoe UI Black", 18), command=lambda: artwork_info_window('original', 'view', 'placeholder'))
placeholder_1.pack(side=LEFT)
placeholder_2 = Button(item_frame_2, text="Placeholder", fg='white', bg='#4D5660', relief='flat', font=("Segoe UI Black", 18), command=lambda: artwork_info_window('original', 'view', 'placeholder'))
placeholder_2.pack(side=LEFT)
placeholder_3 = Button(item_frame_3, text="Placeholder", fg='white', bg='#4D5660', relief='flat', font=("Segoe UI Black", 18), command=lambda: artwork_info_window('original', 'view', 'placeholder'))
placeholder_3.pack(side=LEFT)
placeholder_4 = Button(item_frame_4, text="Placeholder", fg='white', bg='#4D5660', relief='flat', font=("Segoe UI Black", 18), command=lambda: artwork_info_window('original', 'view', 'placeholder'))
placeholder_4.pack(side=LEFT)
placeholder_5 = Button(item_frame_5, text="Placeholder", fg='white', bg='#4D5660', relief='flat', font=("Segoe UI Black", 18), command=lambda: artwork_info_window('original', 'view', 'placeholder'))
placeholder_5.pack(side=LEFT)


#delete functionality
def delete_artwork(artwork_id):
    delete_dialog = Toplevel(root)
    delete_dialog.title("Delete artwork")
    delete_dialog.geometry("400x200")
    delete_dialog.configure(bg='#4D5660')
    delete_dialog.wm_iconphoto(False, photo)
    delete_dialog.grab_set()

    delete_dialog.rowconfigure(0, weight=1)
    delete_dialog.rowconfigure(1, weight=1) 
    delete_dialog.rowconfigure(2, weight=2) 
    delete_dialog.columnconfigure(0, weight=1) 
    delete_dialog.columnconfigure(1, weight=1) 

    def yes_press():
        #placeholder for delete function
        delete_dialog.destroy()

    def no_press():
        delete_dialog.destroy()
        
    info_lbl_1 = Label(delete_dialog, text="Delete this artwork?", bg='#4D5660', fg='#FFFFFF', font=("Segoe UI Black", 18))
    info_lbl_1.grid(row=0, column=0, padx=25, pady=(20, 0), columnspan=2, sticky="W")
    info_lbl_2 = Label(delete_dialog, text="This action cannot be undone.", bg='#4D5660', fg='#FFFFFF', font=("Segoe UI Black", 18))
    info_lbl_2.grid(row=1, column=0, padx=25, pady=0, columnspan=2, sticky="W")

    original_btn = Button(delete_dialog, text="Yes", bg='#9399AC', fg='#FFFFFF', bd=0, command=yes_press, font=("Segoe UI Black", 18))
    original_btn.grid(row=2, column=0, padx=25, pady=25, sticky="NESW")
    fanart_btn = Button(delete_dialog, text="No", bg='#9399AC', fg='#FFFFFF', bd=0, command=no_press, font=("Segoe UI Black", 18))
    fanart_btn.grid(row=2, column=1, padx=25, pady=25, sticky="NESW")





delete_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/delete_icon.png"))

delete_1 = Button(item_frame_1, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda: delete_artwork('ID Placeholder'))
delete_1.pack(side=RIGHT)
delete_2 = Button(item_frame_2, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda: delete_artwork('ID Placeholder'))
delete_2.pack(side=RIGHT)
delete_3 = Button(item_frame_3, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda: delete_artwork('ID Placeholder'))
delete_3.pack(side=RIGHT)
delete_4 = Button(item_frame_4, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda: delete_artwork('ID Placeholder'))
delete_4.pack(side=RIGHT)
delete_5 = Button(item_frame_5, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda: delete_artwork('ID Placeholder'))
delete_5.pack(side=RIGHT)


edit_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/edit_icon.png"))

#MUST SWAP OUT PARAMETERS FOR ACTUAL ARTWORK ID AND TYPE
edit_1 = Button(item_frame_1, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda: artwork_info_window('original', 'edit', 'placeholder'))
edit_1.pack(side=RIGHT, padx=10)
edit_2 = Button(item_frame_2, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda: artwork_info_window('original', 'edit', 'placeholder'))
edit_2.pack(side=RIGHT, padx=10)
edit_3 = Button(item_frame_3, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda: artwork_info_window('original', 'edit', 'placeholder'))
edit_3.pack(side=RIGHT, padx=10)
edit_4 = Button(item_frame_4, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda: artwork_info_window('original', 'edit', 'placeholder'))
edit_4.pack(side=RIGHT, padx=10)
edit_5 = Button(item_frame_5, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda: artwork_info_window('original', 'edit', 'placeholder'))
edit_5.pack(side=RIGHT, padx=10)





#creating the options functionality
def choose_arttype(action):
    arttype_dialog = Toplevel(root)
    arttype_dialog.title("Choose art type")
    arttype_dialog.geometry("400x200")
    arttype_dialog.configure(bg='#9399AC')
    arttype_dialog.wm_iconphoto(False, photo)
    arttype_dialog.grab_set()

    arttype_dialog.rowconfigure(0, weight=1) 
    arttype_dialog.columnconfigure(0, weight=1) 
    arttype_dialog.columnconfigure(1, weight=1) 

    if action == 'create':
        def original_press():
            arttype_dialog.destroy()
            artwork_info_window('original', 'create')
        def fanart_press():
            arttype_dialog.destroy()
            artwork_info_window('fanart', 'create')
        
    if action == 'filter':
        def original_press():
            arttype_dialog.destroy()
            artwork_info_window('original', 'filter')
        def fanart_press():
            arttype_dialog.destroy()
            artwork_info_window('fanart', 'filter')

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


filter_btn = Button(filter_bg, relief='flat', text="Search", image=filter_img, bg='#E2CDB4', bd=10, command=lambda: choose_arttype('filter'))
filter_btn.grid(row=0, column=0, padx=10, pady=10)
add_btn = Button(add_bg, relief='flat', text="Add", image=add_img, bg='#E2CDB4', bd=10, command=lambda: choose_arttype('create'))
add_btn.grid(row=0, column=0, padx=10, pady=10)



root.mainloop()
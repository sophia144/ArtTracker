from tkinter import *
from tkinter import font
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime

#modules for the graph window
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colormaps

#modules for restarting
import sys
import os


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
root.rowconfigure(3, weight=1) 


#changing the icon
photo = ImageTk.PhotoImage(Image.open("ArtTracker/resources/painticon.ico"))
root.wm_iconphoto(False, photo)
#https://www.flaticon.com/free-icon/paint-brush_587377

#setting up icons
delete_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/delete_icon.png"))
forward_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/forward_icon.png"))
back_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/back_icon.png"))
edit_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/edit_icon.png"))
filter_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/filter_icon.png"))
add_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/add_img.png"))
home_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/home_icon.png"))
chart_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/chart_icon.png"))

#setting up list of artworks
fanart_list, original_list = read_csv()
all_artworks = fanart_list + original_list

#formatting the artworks window
bg_frame = LabelFrame(root, padx=0, pady=30, bg='#7B8292', bd=0)
bg_frame.grid(row=0, column=0, padx=50, pady=50, sticky="NESW", rowspan=4)

bg_frame.columnconfigure(0,weight=1)
bg_frame.columnconfigure(1,weight=6)
bg_frame.columnconfigure(2,weight=1)

bg_frame.rowconfigure(0,weight=1) 
bg_frame.rowconfigure(1,weight=1) 
bg_frame.rowconfigure(2,weight=1) 
bg_frame.rowconfigure(3,weight=1) 
bg_frame.rowconfigure(4,weight=1) 

page_num = 1

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


item_frame_1.rowconfigure(0,weight=1)
item_frame_2.rowconfigure(0,weight=1) 
item_frame_3.rowconfigure(0,weight=1) 
item_frame_4.rowconfigure(0,weight=1) 
item_frame_5.rowconfigure(0,weight=1) 

current_artworks = all_artworks

#artwork info window
def presence_check(input_boxes):
    full = True
    for box in input_boxes:
        if box.get().strip() == "":
            full = False
    return full

def artwork_info_window(arttype, action, artwork=None):
    global creation_window
    global name_inp
    global clicked
    global medium_inp
    global subject_inp
    global desc_inp
    global fandom_inp
    global character_inp

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
    # datatype of dropdown menu
    clicked = StringVar() 
    clicked.set("Planned") 
    # Create Dropdown menu 
    if action == 'filter':
        options = ["", "Planned", "In Progress", "Completed"] 
        clicked.set("")
        status_inp = OptionMenu(info_frame, clicked, *options) 
    else:
        options = ["Planned", "In Progress", "Completed"] 
        status_inp = OptionMenu(info_frame, clicked, *options) 
    
    status_inp.config(width=50, bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 16), anchor="w")
    status_inp.grid(row=3, column=0, sticky="W", padx=(2, 50))

    medium_lbl = Label(info_frame, text="Medium", bg='#9399AC', fg='#4D5660', font=("Segoe UI Black", 22))
    medium_lbl.grid(row=4, column=0, sticky="W")
    medium_inp = Entry(info_frame, width=50, bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 16))
    medium_inp.grid(row=5, column=0, sticky="W", padx=(2, 50))



    #ORIGINAL ARTWORK
    if arttype == Original:
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
        

        #fills textboxes with pre-existing info
        if action == 'edit' or action == 'view':
            name_inp.insert(0, artwork.name)
            clicked.set(artwork.status)
            medium_inp.insert(0, artwork.medium)
            subject_inp.insert(0, artwork.subject)
            desc_inp.insert(0, artwork.desc)
        #makes textboxes uneditable if viewing
        if action == 'view':
            name_inp.config(state='disabled')
            status_inp.config(state='disabled')
            medium_inp.config(state='disabled')
            subject_inp.config(state='disabled')
            desc_inp.config(state='disabled')


        #adding various buttons depending on what the user is doing
        if action == 'create':
            save_btn = Button(btn_bg, text="Save", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=save_original)
            save_btn.grid(row=0, column=0, padx=0, pady=0, sticky="W")
        elif action == 'edit':
            update_btn = Button(btn_bg, text="Update", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=lambda: update_original(artwork))
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


        #fills textboxes with pre-existing info
        if action == 'edit' or action == 'view':
            name_inp.insert(0, artwork.name)
            clicked.set(artwork.status)
            medium_inp.insert(0, artwork.medium)
            fandom_inp.insert(0, artwork.fandom)
            character_inp.insert(0, artwork.character)
            desc_inp.insert(0, artwork.desc)
        #makes textboxes uneditable if viewing
        if action == 'view':
            name_inp.config(state='disabled')
            status_inp.config(state='disabled')
            medium_inp.config(state='disabled')
            fandom_inp.config(state='disabled')
            character_inp.config(state='disabled')
            desc_inp.config(state='disabled')


        #adding various buttons depending on what the user is doing
        if action == 'create':
            save_btn = Button(btn_bg, text="Save", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=save_fanart)
            save_btn.grid(row=0, column=0, padx=0, pady=0, sticky="W")
        elif action == 'edit':
            save_btn = Button(btn_bg, text="Update", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=lambda: update_fanart(artwork))
            save_btn.grid(row=0, column=0, padx=0, pady=0, sticky="W")
        elif action == 'filter':
            filter_btn = Button(btn_bg, text="Go", bg='#E2CDB4', fg='#FFFFFF', relief='flat', bd=0, font=("Segoe UI Black", 18), command=filter_fanarts)
            filter_btn.grid(row=0, column=0, padx=0, pady=0, sticky="W")


#other functions
def destroy_item_frames():
    global item_frame_1
    global item_frame_2
    global item_frame_3
    global item_frame_4
    global item_frame_5

    frames = [item_frame_1, item_frame_2, item_frame_3, item_frame_4, item_frame_5]
    for frame in frames:
        frame.destroy()

def reinitialize_frames():
    global item_frame_1
    global item_frame_2
    global item_frame_3
    global item_frame_4
    global item_frame_5

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

def create_delete_list(current_artworks):
    #calculating the number of pages
    num_pages = len(current_artworks) // 5
    delete_buttons = []

    #creating a button for each artwork in the list
    artworks_by_page = []
    for i in range(0, len(current_artworks), 5):
        artworks_by_page += [current_artworks[i:i + 5]]

    for page in artworks_by_page:
        delete_buttons.append(Button(item_frame_1, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda artwork = page[0]: delete_artwork(artwork)))
        
        #in case there is only one button in the last group
        try:
            delete_buttons.append(Button(item_frame_2, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda artwork = page[1]: delete_artwork(artwork)))
        except:
            pass

        try:
            delete_buttons.append(Button(item_frame_3, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda artwork = page[2]: delete_artwork(artwork)))
        except:
            pass

        try:
            delete_buttons.append(Button(item_frame_4, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda artwork = page[3]: delete_artwork(artwork)))
        except:
            pass

        try:
            delete_buttons.append(Button(item_frame_5, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda artwork = page[4]: delete_artwork(artwork)))
        except:
            pass

    return delete_buttons

def create_edit_list(current_artworks):
    #calculating the number of pages
    num_pages = len(current_artworks) // 5
    edit_buttons = []

    #creating a button for each artwork in the list
    artworks_by_page = []
    for i in range(0, len(current_artworks), 5):
        artworks_by_page += [current_artworks[i:i + 5]]

    for page in artworks_by_page:
        edit_buttons.append(Button(item_frame_1, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda artwork = page[0], type = type(page[0]): artwork_info_window(type, 'edit', artwork)))
        
        #in case there is only one button in the last group
        try:
            edit_buttons.append(Button(item_frame_2, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda artwork = page[1], type = type(page[1]): artwork_info_window(type, 'edit', artwork)))
        except:
            pass

        try:
            edit_buttons.append(Button(item_frame_3, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda artwork = page[2], type = type(page[2]): artwork_info_window(type, 'edit', artwork)))
        except:
            pass

        try:
            edit_buttons.append(Button(item_frame_4, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda artwork = page[3], type = type(page[3]): artwork_info_window(type, 'edit', artwork)))
        except:
            pass

        try:
            edit_buttons.append(Button(item_frame_5, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda artwork = page[4], type = type(page[4]): artwork_info_window(type, 'edit', artwork)))
        except:
            pass

    return edit_buttons

def create_buttons_list(current_artworks):
    #calculating the number of pages
    num_pages = len(current_artworks) // 5
    artwork_buttons = []

    #creating a button for each artwork in the list
    artworks_by_page = []
    for i in range(0, len(current_artworks), 5):
        artworks_by_page += [current_artworks[i:i + 5]]

    for page in artworks_by_page:
        artwork_buttons.append(Button(item_frame_1, text=page[0].name, fg='white', bg='#4D5660', relief='flat', font=("Segoe UI Black", 18), command=lambda artwork = page[0], type = type(page[0]): artwork_info_window(type, 'view', artwork)))
        
        #in case there is only one button in the last group
        try:
            artwork_buttons.append(Button(item_frame_2, text=page[1].name, fg='white', bg='#4D5660', relief='flat', font=("Segoe UI Black", 18), command=lambda artwork = page[1], type = type(page[1]): artwork_info_window(type, 'view', artwork)))
        except:
            pass

        try:
            artwork_buttons.append(Button(item_frame_3, text=page[2].name, fg='white', bg='#4D5660', relief='flat', font=("Segoe UI Black", 18), command=lambda artwork = page[2], type = type(page[2]): artwork_info_window(type, 'view', artwork)))
        except:
            pass

        try:
            artwork_buttons.append(Button(item_frame_4, text=page[3].name, fg='white', bg='#4D5660', relief='flat', font=("Segoe UI Black", 18), command=lambda artwork = page[3], type = type(page[3]): artwork_info_window(type, 'view', artwork)))
        except:
            pass

        try:
            artwork_buttons.append(Button(item_frame_5, text=page[4].name, fg='white', bg='#4D5660', relief='flat', font=("Segoe UI Black", 18), command=lambda artwork = page[4], type = type(page[4]): artwork_info_window(type, 'view', artwork)))
        except:
            pass

    return artwork_buttons, artworks_by_page

def setup_home(home_artworks, first_run=False):
    global artwork_button_1
    global artwork_button_2
    global artwork_button_3
    global artwork_button_4
    global artwork_button_5

    global current_artworks

    current_artworks = home_artworks
    artwork_buttons, artworks_by_page = create_buttons_list(current_artworks)


    

    if first_run == False:
           forget_home_buttons()

    try:
        artwork_button_1 = artwork_buttons[0]
        artwork_button_1.pack(side=LEFT)
    except: 
        item_frame_1.destroy()

    try:
        artwork_button_2 = artwork_buttons[1]
        artwork_button_2.pack(side=LEFT)
    except: 
        item_frame_2.destroy()

    try:
        artwork_button_3 = artwork_buttons[2]
        artwork_button_3.pack(side=LEFT)
    except:
        item_frame_3.destroy()

    try:
        artwork_button_4 = artwork_buttons[3]
        artwork_button_4.pack(side=LEFT)
    except:
        item_frame_4.destroy()

    try:
        artwork_button_5 = artwork_buttons[4]
        artwork_button_5.pack(side=LEFT)
    except:
        item_frame_5.destroy()

def forget_home_buttons():
    global artwork_button_1
    global artwork_button_2
    global artwork_button_3
    global artwork_button_4
    global artwork_button_5

    if len(all_artworks) >= 5:
        buttons = [artwork_button_1, artwork_button_2, artwork_button_3, artwork_button_4, artwork_button_5]
    elif len(all_artworks) == 4:
        buttons = [artwork_button_1, artwork_button_2, artwork_button_3, artwork_button_4]
    elif len(all_artworks) == 3:
        buttons = [artwork_button_1, artwork_button_2, artwork_button_3]
    elif len(all_artworks) == 2:
        buttons = [artwork_button_1, artwork_button_2]

    for button in buttons:
        button.destroy()

def update_variables():
    global all_artworks
    global current_artworks

    current_artworks = all_artworks
    write_csv(fanart_list, original_list)
    all_artworks = fanart_list + original_list
    forget_home_buttons()
    setup_home(current_artworks)

    if len(all_artworks) > 5:
        forward_button.config(state=NORMAL)


#scrolling funtions
def scroll_forward(page_num):
    global current_artworks
    global forward_button
    global back_button

    global artwork_button_1
    global artwork_button_2
    global artwork_button_3
    global artwork_button_4
    global artwork_button_5

    global item_frame_1
    global item_frame_2
    global item_frame_3
    global item_frame_4
    global item_frame_5

    global delete_1
    global delete_2
    global delete_3
    global delete_4
    global delete_5

    destroy_item_frames()
    reinitialize_frames()

    if len(all_artworks) >= 5:
        buttons = [artwork_button_1, artwork_button_2, artwork_button_3, artwork_button_4, artwork_button_5]
    elif len(all_artworks) == 4:
        buttons = [artwork_button_1, artwork_button_2, artwork_button_3, artwork_button_4]
    elif len(all_artworks) == 3:
        buttons = [artwork_button_1, artwork_button_2, artwork_button_3]
    else:
        buttons = [artwork_button_1, artwork_button_2]

    frames = [item_frame_1, item_frame_2, item_frame_3, item_frame_4, item_frame_5]

    if len(all_artworks) >= 5:
        delete_buttons = [delete_1, delete_2, delete_3, delete_4, delete_5]
    elif len(all_artworks) == 4:
        delete_buttons = [delete_1, delete_2, delete_3, delete_4]
    elif len(all_artworks) == 3:
        delete_buttons = [delete_1, delete_2, delete_3]
    else:
        delete_buttons = [delete_1, delete_2]


    if len(all_artworks) >= 5:
        edit_buttons = [edit_1, edit_2, edit_3, edit_4, edit_5]
    elif len(all_artworks) == 4:
        edit_buttons = [edit_1, edit_2, edit_3, edit_4]
    elif len(all_artworks) == 3:
        edit_buttons = [edit_1, edit_2, edit_3]
    else:
        edit_buttons = [edit_1, edit_2]


    delete_buttons = create_delete_list(current_artworks)
    edit_buttons = create_edit_list(current_artworks)
    artwork_buttons, artworks_by_page = create_buttons_list(current_artworks)

    #splitting artwork buttons by page
    buttons_by_page = []
    for i in range(0, len(artwork_buttons), 5):
        buttons_by_page += [artwork_buttons[i:i + 5]]
    
    #splitting delete buttons by page
    delete_by_page = []
    for i in range(0, len(delete_buttons), 5):
        delete_by_page += [delete_buttons[i:i + 5]]

    #splitting edit buttons by page
    edit_by_page = []
    for i in range(0, len(edit_buttons), 5):
        edit_by_page += [edit_buttons[i:i + 5]]


    #replaces all artwork buttons with that of the next page
    forget_home_buttons()
    for button_number in range(0, 5):
        try:
            buttons[button_number] = buttons_by_page[page_num - 1][button_number]
            buttons[button_number].pack(side=LEFT)

            delete_buttons[button_number] = delete_by_page[page_num - 1][button_number]
            delete_buttons[button_number].pack(side=RIGHT)

            edit_buttons[button_number] = edit_by_page[page_num - 1][button_number]
            edit_buttons[button_number].pack(side=RIGHT, padx=10)

        except IndexError: 
            frames[button_number].destroy()

    
    #handles first and last pages
    if page_num == len(buttons_by_page):
        forward_button.config(state=DISABLED)
    else:
        forward_button.config(command=lambda page_num = page_num + 1: scroll_forward(page_num), state=NORMAL)
    
    back_button.config(command=lambda page_num = page_num - 1: scroll_back(page_num))
    back_button.config(state=NORMAL)


    forward_button.grid(row=2, column=2, sticky="NESW")
    back_button.grid(row=2, column=0, sticky="NESW") 

def scroll_back(page_num):
    global current_artworks
    global forward_button
    global back_button

    global artwork_button_1
    global artwork_button_2
    global artwork_button_3
    global artwork_button_4
    global artwork_button_5

    global item_frame_1
    global item_frame_2
    global item_frame_3
    global item_frame_4
    global item_frame_5

    destroy_item_frames()
    reinitialize_frames()

    if len(all_artworks) >= 5:
        buttons = [artwork_button_1, artwork_button_2, artwork_button_3, artwork_button_4, artwork_button_5]
    elif len(all_artworks) == 4:
        buttons = [artwork_button_1, artwork_button_2, artwork_button_3, artwork_button_4]
    elif len(all_artworks) == 3:
        buttons = [artwork_button_1, artwork_button_2, artwork_button_3]
    else:
        buttons = [artwork_button_1, artwork_button_2]

    frames = [item_frame_1, item_frame_2, item_frame_3, item_frame_4, item_frame_5]

    if len(all_artworks) >= 5:
        delete_buttons = [delete_1, delete_2, delete_3, delete_4, delete_5]
    elif len(all_artworks) == 4:
        delete_buttons = [delete_1, delete_2, delete_3, delete_4]
    elif len(all_artworks) == 3:
        delete_buttons = [delete_1, delete_2, delete_3]
    else:
        delete_buttons = [delete_1, delete_2]


    if len(all_artworks) >= 5:
        edit_buttons = [edit_1, edit_2, edit_3, edit_4, edit_5]
    elif len(all_artworks) == 4:
        edit_buttons = [edit_1, edit_2, edit_3, edit_4]
    elif len(all_artworks) == 3:
        edit_buttons = [edit_1, edit_2, edit_3]
    else:
        edit_buttons = [edit_1, edit_2]

    delete_buttons = create_delete_list(current_artworks)
    edit_buttons = create_edit_list(current_artworks)
    artwork_buttons, artworks_by_page = create_buttons_list(current_artworks)

    #splitting the buttons by page
    buttons_by_page = []
    for i in range(0, len(artwork_buttons), 5):
        buttons_by_page += [artwork_buttons[i:i + 5]]

    #splitting delete buttons by page
    delete_by_page = []
    for i in range(0, len(delete_buttons), 5):
        delete_by_page += [delete_buttons[i:i + 5]]

    #splitting edit buttons by page
    edit_by_page = []
    for i in range(0, len(edit_buttons), 5):
        edit_by_page += [edit_buttons[i:i + 5]]


    #replaces all artwork buttons with that of the next page
    forget_home_buttons()
    for button_number in range(0, 5):
        try:
            buttons[button_number] = buttons_by_page[page_num - 1][button_number]
            buttons[button_number].pack(side=LEFT)

            delete_buttons[button_number] = delete_by_page[page_num - 1][button_number]
            delete_buttons[button_number].pack(side=RIGHT)

            edit_buttons[button_number] = edit_by_page[page_num - 1][button_number]
            edit_buttons[button_number].pack(side=RIGHT, padx=10)

        except IndexError: 
            frames[button_number].destroy()

    

    if page_num == 1:
        back_button.config(state=DISABLED)
    else:
        back_button.config(command=lambda page_num = page_num - 1: scroll_back(page_num), state=NORMAL)

    forward_button.config(command=lambda page_num = page_num + 1: scroll_forward(page_num), state=NORMAL)
    forward_button.config(state=NORMAL)

    forward_button.grid(row=2, column=2, sticky="NESW")
    back_button.grid(row=2, column=0, sticky="NESW") 




#save artwork functions
def save_original():
    if presence_check([name_inp, desc_inp, clicked, medium_inp, subject_inp]) == True:
        name = name_inp.get()
        desc = desc_inp.get()
        status = clicked.get()
        medium = medium_inp.get()
        subject = subject_inp.get()
        new_original = Original(name, desc, status, medium, subject)
        original_list.append(new_original)
        update_variables()
        forget_home_buttons()
        setup_home(all_artworks)
        creation_window.destroy()
    else:
        messagebox.showerror('Validation Error', 'Error: One or more input fields empty')

def save_fanart():
    if presence_check([name_inp, desc_inp, clicked, medium_inp, fandom_inp, character_inp]) == True:
        name = name_inp.get()
        desc = desc_inp.get()
        status = clicked.get()
        medium = medium_inp.get()
        fandom = fandom_inp.get()
        character = character_inp.get()

        new_fanart = Fanart(name, desc, status, medium, fandom, character)
        fanart_list.append(new_fanart)
        update_variables()
        forget_home_buttons()
        setup_home(all_artworks)
        creation_window.destroy()
    else:
        messagebox.showerror('Validation Error', 'Error: One or more input fields empty')


#update database functions
def update_original(artwork):
    if presence_check([name_inp, desc_inp, clicked, medium_inp, subject_inp]) == True:
        artwork.name = name_inp.get()
        artwork.desc = desc_inp.get()
        artwork.status = clicked.get()
        artwork.medium = medium_inp.get()
        artwork.subject = subject_inp.get()

        forget_home_buttons()
        update_variables()
        creation_window.destroy()
    else:
        messagebox.showerror('Validation Error', 'Error: One or more input fields empty')


def update_fanart(artwork):
    if presence_check([name_inp, desc_inp, clicked, medium_inp, fandom_inp, character_inp]) == True:
        artwork.name = name_inp.get()
        artwork.desc = desc_inp.get()
        artwork.status = clicked.get()
        artwork.medium = medium_inp.get()
        artwork.fandom = fandom_inp.get()
        artwork.character = character_inp.get()

        forget_home_buttons()
        update_variables()
        creation_window.destroy()
    else:
        messagebox.showerror('Validation Error', 'Error: One or more input fields empty')


#filter database functions
def create_filter_dict(type):
    filters = {}

    #gets all filters where the input is not empty
    if name_inp.get().strip() != "":
        filters['name'] = name_inp.get().strip()
    if desc_inp.get().strip() != "":
        filters['description'] = desc_inp.get().strip()
    if clicked.get().strip() != "":
        filters['status'] = clicked.get().strip()
    if medium_inp.get().strip() != "":
        filters['medium'] = medium_inp.get().strip()

    if type == Original:
        if subject_inp.get().strip() != "":
            filters['subject'] = subject_inp.get().strip()
    else:
        if fandom_inp.get().strip() != "":
            filters['fandom'] = fandom_inp.get().strip()
        if character_inp.get().strip() != "":
            filters['character'] = character_inp.get().strip()

    return filters


def filter_originals():
    filters = create_filter_dict(Original)
    filtered_originals = []

    for artwork in original_list:
        match = True
        for attribute, value in filters.items():
            if getattr(artwork, attribute).upper() != value.upper():
                match = False
        if match == True:
            filtered_originals.append(artwork)
    
    if len(filtered_originals) != 0:
        forget_home_buttons()
        setup_home(filtered_originals)
        creation_window.destroy()
    else: 
        messagebox.showerror('Error', 'Error: No artworks meet requirements')
    
    
def filter_fanarts():
    filters = create_filter_dict(Fanart)
    filtered_fanarts = []

    for artwork in fanart_list:
        match = True
        for attribute, value in filters.items():
            if getattr(artwork, attribute).upper() != value.upper():
                match = False
        if match == True:
            filtered_fanarts.append(artwork)
    
    if len(filtered_fanarts) != 0:
        forget_home_buttons()
        setup_home(filtered_fanarts)
        creation_window.destroy()
    else:
        messagebox.showerror('Error', 'Error: No artworks meet requirements')


#delete functionality
def delete_artwork(artwork):
    if len(current_artworks) == 1:
         messagebox.showerror('Error', 'Error: Minimum number of records is 1')

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

    #deletes the artwork record
    def yes_press(artwork):
        if type(artwork) == Original:
            original_list.remove(artwork)
        else:
            fanart_list.remove(artwork)
        update_variables()
        delete_dialog.destroy()

    def no_press():
        delete_dialog.destroy()
    
    #text on the delete window
    info_lbl_1 = Label(delete_dialog, text="Delete this artwork?", bg='#4D5660', fg='#FFFFFF', font=("Segoe UI Black", 18))
    info_lbl_1.grid(row=0, column=0, padx=25, pady=(20, 0), columnspan=2, sticky="W")
    info_lbl_2 = Label(delete_dialog, text="This action cannot be undone.", bg='#4D5660', fg='#FFFFFF', font=("Segoe UI Black", 18))
    info_lbl_2.grid(row=1, column=0, padx=25, pady=0, columnspan=2, sticky="W")

    #buttons on the delete window
    yes_btn = Button(delete_dialog, text="Yes", bg='#9399AC', fg='#FFFFFF', bd=0, command=lambda: yes_press(artwork), font=("Segoe UI Black", 18))
    yes_btn.grid(row=2, column=0, padx=25, pady=25, sticky="NESW")
    no_btn = Button(delete_dialog, text="No", bg='#9399AC', fg='#FFFFFF', bd=0, command=no_press, font=("Segoe UI Black", 18))
    no_btn.grid(row=2, column=1, padx=25, pady=25, sticky="NESW")


#graph creation functionality
def create_graph(artworks):
    planned = 0
    in_progress = 0
    completed = 0

    for artwork in artworks:
        if artwork.status == 'Planned':
            planned += 1
        elif artwork.status == 'In Progress':
            in_progress += 1
        else:
            completed += 1

    #plots a bar chart from the data above
    fig, ax = plt.subplots(figsize=(9,7))
    
    categories = ['Planned', 'In Progress', 'Completed']
    values = [planned, in_progress, completed]
    colors = ['lightcoral', 'goldenrod', 'yellowgreen']
    
    ax.bar(categories, values, color=colors, width=0.65)
    plt.xlabel('Status', fontsize=15, labelpad=20)
    plt.ylabel('Artworks', fontsize=15, labelpad=20)
    ax.set_title('Artworks by Status', fontsize=20, pad=20)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig("bar_chart.png", format="png", dpi=60)
    plt.close()



#graph page functionality
def create_graph_window():
    global graph_window
    global bar_photo

    graph_window = Toplevel(root)
    graph_window.title("Statistics")
    graph_window.geometry("1000x625")
    graph_window.configure(bg='#9399AC')
    graph_window.wm_iconphoto(False, photo)
    graph_window.grab_set()
    
    graph_frame = LabelFrame(graph_window, padx=50, pady=50, bg='#FFFFFF', bd=0)
    graph_frame.grid(row=0, column=1, padx=(20, 50), pady=50, sticky="NESW")
    graph_frame.columnconfigure(0, weight=1)
    graph_frame.rowconfigure(0, weight=1)

    create_graph(all_artworks)

    bar_photo = ImageTk.PhotoImage(Image.open("bar_chart.png"))
    bar_label = Label(graph_frame, text = "graph", image=bar_photo, bd=0)
    bar_label.pack(anchor='center')

    stats_frame = LabelFrame(graph_window, padx=10, pady=10, bg='#FFFFFF', bd=0)
    stats_frame.grid(row=0, column=0, padx=(50, 20), pady=50, sticky="NESW")

    sum_lbl = Label(stats_frame, text="Artworks", bg='#FFFFFF', fg='#4D5660', font=("Segoe UI Black", 22))
    sum_lbl.grid(row=0, column=0, sticky="W", padx=5)
    sum_stat = Label(stats_frame, text=f"{len(all_artworks)}", bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 22))
    sum_stat.grid(row=1, column=0, sticky="W")

    space_lbl = Label(stats_frame, text = " ", bg='#FFFFFF')
    space_lbl.grid(row=2, column=0, sticky="W")

    sum_originals_lbl = Label(stats_frame, text="Originals", bg='#FFFFFF', fg='#4D5660', font=("Segoe UI Black", 22))
    sum_originals_lbl.grid(row=3, column=0, sticky="W", padx=5)
    sum_originals_stat = Label(stats_frame, text=f"{len(original_list)}", bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 22))
    sum_originals_stat.grid(row=4, column=0, sticky="W")

    sum_fanarts_lbl = Label(stats_frame, text="Fanarts", bg='#FFFFFF', fg='#4D5660', font=("Segoe UI Black", 22))
    sum_fanarts_lbl.grid(row=5, column=0, sticky="W", padx=5)
    sum_fanarts_stat = Label(stats_frame, text=f"{len(fanart_list)}", bg='#FFFFFF', fg='#4D5660', borderwidth=8, relief="flat", font=("Helvetica", 22))
    sum_fanarts_stat.grid(row=6, column=0, sticky="W")

    #configuring the main grid 
    graph_window.columnconfigure(0,weight=1, uniform="equal") 
    graph_window.columnconfigure(1, weight=2, uniform="equal")
    graph_window.rowconfigure(0, weight=1, uniform="equal") 



current_artworks = all_artworks
setup_home(current_artworks, first_run=True)



forward_button = Button(bg_frame, text=">", image=forward_img, bg='#7B8292', bd=0, command=lambda: scroll_forward(2))
forward_button.grid(row=2, column=2, sticky="NESW")
back_button = Button(bg_frame, text=">", image=back_img, bg='#7B8292', bd=0, command=lambda: scroll_back(1), state=DISABLED)
back_button.grid(row=2, column=0, sticky="NESW")

if len(all_artworks) <= 5:
    forward_button.config(state=DISABLED)

#creating the delete icons 
try:
    delete_1 = Button(item_frame_1, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda artwork=(create_buttons_list(current_artworks))[1][page_num - 1][0]: delete_artwork(artwork))
    delete_1.pack(side=RIGHT)
except IndexError:
    pass

try:
    delete_2 = Button(item_frame_2, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda artwork=(create_buttons_list(current_artworks))[1][page_num - 1][1]: delete_artwork(artwork))
    delete_2.pack(side=RIGHT)
except IndexError:
    pass

try:
    delete_3 = Button(item_frame_3, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda artwork=(create_buttons_list(current_artworks))[1][page_num - 1][2]: delete_artwork(artwork))
    delete_3.pack(side=RIGHT)
except IndexError:
    pass

try:
    delete_4 = Button(item_frame_4, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda artwork=(create_buttons_list(current_artworks))[1][page_num - 1][3]: delete_artwork(artwork))
    delete_4.pack(side=RIGHT)
except IndexError:
    pass

try:
    delete_5 = Button(item_frame_5, bd=0, text="Delete", image=delete_img, bg='#9399AC', command=lambda artwork=(create_buttons_list(current_artworks))[1][page_num - 1][4]: delete_artwork(artwork))
    delete_5.pack(side=RIGHT)
except IndexError:
    pass

#creating the edit icons 
try:
    edit_1 = Button(item_frame_1, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda type=type((create_buttons_list(current_artworks))[1][page_num - 1][0]), artwork=(create_buttons_list(current_artworks))[1][page_num - 1][0]: artwork_info_window(type, 'edit', artwork))
    edit_1.pack(side=RIGHT, padx=10)
except IndexError:
    pass

try:
    edit_2 = Button(item_frame_2, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda type=type((create_buttons_list(current_artworks))[1][page_num - 1][1]), artwork=(create_buttons_list(current_artworks))[1][page_num - 1][1]: artwork_info_window(type, 'edit', artwork))
    edit_2.pack(side=RIGHT, padx=10)
except IndexError:
    pass

try:
    edit_3 = Button(item_frame_3, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda type=type((create_buttons_list(current_artworks))[1][page_num - 1][2]), artwork=(create_buttons_list(current_artworks))[1][page_num - 1][2]: artwork_info_window(type, 'edit', artwork))
    edit_3.pack(side=RIGHT, padx=10)
except IndexError:
    pass

try:
    edit_4 = Button(item_frame_4, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda type=type((create_buttons_list(current_artworks))[1][page_num - 1][3]), artwork=(create_buttons_list(current_artworks))[1][page_num - 1][3]: artwork_info_window(type, 'edit', artwork))
    edit_4.pack(side=RIGHT, padx=10)
except IndexError:
    pass

try:
    edit_5 = Button(item_frame_5, bd=0, text="Edit", image=edit_img, bg='#9399AC', command=lambda type=type((create_buttons_list(current_artworks))[1][page_num - 1][4]), artwork=(create_buttons_list(current_artworks))[1][page_num - 1][4]: artwork_info_window(type, 'edit', artwork))
    edit_5.pack(side=RIGHT, padx=10)
except IndexError:
    pass


#creating the options functionality to choose between original or fanart
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
            artwork_info_window(Original, 'create')
        def fanart_press():
            arttype_dialog.destroy()
            artwork_info_window(Fanart, 'create')
        
    if action == 'filter':
        def original_press():
            arttype_dialog.destroy()
            artwork_info_window(Original, 'filter')
        def fanart_press():
            arttype_dialog.destroy()
            artwork_info_window(Fanart, 'filter')

    original_btn = Button(arttype_dialog, text="Original", bg='#4D5660', fg='#FFFFFF', bd=0, command=original_press, font=("Segoe UI Black", 18))
    original_btn.grid(row=0, column=0, padx=10, pady=10, sticky="NESW")
    fanart_btn = Button(arttype_dialog, text="Fanart", bg='#4D5660', fg='#FFFFFF', bd=0, command=fanart_press, font=("Segoe UI Black", 18))
    fanart_btn.grid(row=0, column=1, padx=10, pady=10, sticky="NESW")

    
#formatting the options strip
options_frame = LabelFrame(root, padx=30, pady=30, bg='#4D5660', bd=0)
options_frame.grid(row=0, column=2, sticky="NESW", rowspan=4)

#options
filter_bg = Frame(root, bg='#FFFFFF', bd=0) 
filter_bg.grid(row=0, column=1, padx=10, pady=10, columnspan=3)
add_bg = Frame(root, bg='#FFFFFF', bd=0) 
add_bg.grid(row=1, column=1, padx=10, pady=10, columnspan=3)
home_bg = Frame(root, bg='#FFFFFF', bd=0) 
home_bg.grid(row=2, column=1, padx=10, pady=10, columnspan=3)
chart_bg = Frame(root, bg='#FFFFFF', bd=0) 
chart_bg.grid(row=3, column=1, padx=10, pady=10, columnspan=3)


filter_btn = Button(filter_bg, relief='flat', text="Search", image=filter_img, bg='#E2CDB4', bd=10, command=lambda: choose_arttype('filter'))
filter_btn.grid(row=0, column=0, padx=10, pady=10)
add_btn = Button(add_bg, relief='flat', text="Add", image=add_img, bg='#E2CDB4', bd=10, command=lambda: choose_arttype('create'))
add_btn.grid(row=0, column=0, padx=10, pady=10)
home_btn = Button(home_bg, relief='flat', text="Home", image=home_img, bg='#E2CDB4', bd=10, command=lambda: print('please close the program and open it again'))
home_btn.grid(row=0, column=0, padx=10, pady=10)
chart_btn = Button(chart_bg, relief='flat', text="Charts", image=chart_img, bg='#E2CDB4', bd=10, command=create_graph_window)
chart_btn.grid(row=0, column=0, padx=10, pady=10)


root.mainloop()
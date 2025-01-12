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

root.columnconfigure(0,weight=7) # column weight 70%
root.columnconfigure(1,weight=1) # column weight 30%
root.columnconfigure(2,weight=1) # column weight 30%
root.columnconfigure(3,weight=1) # column weight 30%
root.rowconfigure(0, weight=1) # row weight 100%
root.rowconfigure(1, weight=1) # row weight 100%
root.rowconfigure(2, weight=1) # row weight 100%


#changing the icon
ico = Image.open("ArtTracker/resources/painticon.ico")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
#https://www.flaticon.com/free-icon/paint-brush_587377


#formatting the home window
bg_frame = LabelFrame(root, padx=30, pady=30, bg='#7B8292', bd=0)
bg_frame.grid(row=0, column=0, padx=50, pady=50, sticky="NESW", rowspan=3)

item_frame_1 = LabelFrame(bg_frame, padx=10, pady=10, bg='#4D5660', bd=0)
item_frame_1.grid(row=0, column=0, sticky="NESW", padx=10, pady=10)
item_frame_2 = LabelFrame(bg_frame, padx=10, pady=10, bg='#4D5660', bd=0)
item_frame_2.grid(row=1, column=0, sticky="NESW", padx=10, pady=10)
item_frame_3 = LabelFrame(bg_frame, padx=10, pady=10, bg='#4D5660', bd=0)
item_frame_3.grid(row=2, column=0, sticky="NESW", padx=10, pady=10)
item_frame_4 = LabelFrame(bg_frame, padx=10, pady=10, bg='#4D5660', bd=0)
item_frame_4.grid(row=3, column=0, sticky="NESW", padx=10, pady=10)
item_frame_5 = LabelFrame(bg_frame, padx=10, pady=10, bg='#4D5660', bd=0)
item_frame_5.grid(row=4, column=0, sticky="NESW", padx=10, pady=10)

bg_frame.columnconfigure(0,weight=1) 
bg_frame.rowconfigure(0,weight=1) # row weight 20%
bg_frame.rowconfigure(1,weight=1) # row weight 20%
bg_frame.rowconfigure(2,weight=1) # row weight 20%
bg_frame.rowconfigure(3,weight=1) # row weight 20%
bg_frame.rowconfigure(4,weight=1) # row weight 20%


item_frame_1.rowconfigure(0,weight=1)
item_frame_2.rowconfigure(0,weight=1) 
item_frame_3.rowconfigure(0,weight=1) 
item_frame_4.rowconfigure(0,weight=1) 
item_frame_5.rowconfigure(0,weight=1) 


placeholder_1 = Label(item_frame_1, text="Placeholder", fg='white', bg='#4D5660', font=("Segoe UI Black", 18))
placeholder_1.grid(row=0, column=0)
placeholder_2 = Label(item_frame_2, text="Placeholder", fg='white', bg='#4D5660', font=("Segoe UI Black", 18))
placeholder_2.grid(row=0, column=0)
placeholder_3 = Label(item_frame_3, text="Placeholder", fg='white', bg='#4D5660', font=("Segoe UI Black", 18))
placeholder_3.grid(row=0, column=0)
placeholder_4 = Label(item_frame_4, text="Placeholder", fg='white', bg='#4D5660', font=("Segoe UI Black", 18))
placeholder_4.grid(row=0, column=0)
placeholder_5 = Label(item_frame_5, text="Placeholder", fg='white', bg='#4D5660', font=("Segoe UI Black", 18))
placeholder_5.grid(row=0, column=0)


options_frame = LabelFrame(root, padx=30, pady=30, bg='#4D5660', bd=0)
options_frame.grid(row=0, column=2, sticky="NESW", rowspan=3)


search_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/search_img.png"))
add_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/add_img.png"))
filter_img = ImageTk.PhotoImage(Image.open("ArtTracker/resources/filter_icon.png"))


search_bg = Frame(root, bg='#FFFFFF', bd=0) 
search_bg.grid(row=0, column=1, padx=10, pady=10, columnspan=3)
add_bg = Frame(root, bg='#FFFFFF', bd=0) 
add_bg.grid(row=1, column=1, padx=10, pady=10, columnspan=3)
filter_bg = Frame(root, bg='#FFFFFF', bd=0) 
filter_bg.grid(row=2, column=1, padx=10, pady=10, columnspan=3)


search_btn = Button(search_bg, relief='flat', text="Search", image=search_img, bg='#E2CDB4', bd=10)
search_btn.grid(row=0, column=0, padx=10, pady=10)
add_btn = Button(add_bg, relief='flat', text="Add", image=add_img, bg='#E2CDB4', bd=10)
add_btn.grid(row=0, column=0, padx=10, pady=10)
filter_btn = Button(filter_bg, relief='flat', text="Filter", image=filter_img, bg='#E2CDB4', bd=10)
filter_btn.grid(row=0, column=0, padx=10, pady=10)


root.mainloop()
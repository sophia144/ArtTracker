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
photo = ImageTk.PhotoImage(Image.open("ArtTracker/resources/painticon.ico"))
root.wm_iconphoto(False, photo)
#https://www.flaticon.com/free-icon/paint-brush_587377


#formatting the artworks window
bg_frame = LabelFrame(root, padx=0, pady=30, bg='#7B8292', bd=0)
bg_frame.grid(row=0, column=0, padx=50, pady=50, sticky="NESW", rowspan=3)

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

bg_frame.rowconfigure(0,weight=1) # row weight 20%
bg_frame.rowconfigure(1,weight=1) # row weight 20%
bg_frame.rowconfigure(2,weight=1) # row weight 20%
bg_frame.rowconfigure(3,weight=1) # row weight 20%
bg_frame.rowconfigure(4,weight=1) # row weight 20%

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


#creating the options functionality
def choose_arttype():
    global arttype_dialog
    arttype_dialog = Toplevel(root)
    arttype_dialog.title("Choose art type")
    arttype_dialog.geometry("400x200")
    arttype_dialog.configure(bg='#9399AC')
    arttype_dialog.wm_iconphoto(False, photo)
    arttype_dialog.grab_set()

    arttype_dialog.rowconfigure(0, weight=1) # row weight 100%
    arttype_dialog.columnconfigure(0, weight=1) # column weight 50%
    arttype_dialog.columnconfigure(1, weight=1) # column weight 50%

    def original_press():
        #original_window()
        arttype_dialog.destroy()
    
    def fanart_press():
        #fanart_window()
        arttype_dialog.destroy()


    original_btn = Button(arttype_dialog, text="Original", bg='#4D5660', fg='#FFFFFF', bd=0, command=original_press, font=("Segoe UI Black", 18))
    original_btn.grid(row=0, column=0, padx=10, pady=10, sticky="NESW")
    fanart_btn = Button(arttype_dialog, text="Fanart", bg='#4D5660', fg='#FFFFFF', bd=0, command=fanart_press, font=("Segoe UI Black", 18))
    fanart_btn.grid(row=0, column=1, padx=10, pady=10, sticky="NESW")

    



#formatting the options strip
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
add_btn = Button(add_bg, relief='flat', text="Add", image=add_img, bg='#E2CDB4', bd=10, command=choose_arttype)
add_btn.grid(row=0, column=0, padx=10, pady=10)
filter_btn = Button(filter_bg, relief='flat', text="Filter", image=filter_img, bg='#E2CDB4', bd=10)
filter_btn.grid(row=0, column=0, padx=10, pady=10)


root.mainloop()
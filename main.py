from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Art Tracker")
root.geometry("600x400")

#changes the icon
ico = Image.open("ArtTracker/resources/painticon.ico")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
#https://www.flaticon.com/free-icon/paint-brush_587377



root.mainloop()
# We start by importing the neccesary libraries
# and by creating the GUI window

import tkinter as tk
window = tk.Tk()
window.geometry("620x780")
window.title(" Age Calculator App ")

# Now the labels and positions
# into de Window

name = tk.Label(text = "Name")
name.grid(column = 0, row = 1)
year = tk.Label(text = "Year")
year.grid(column = 0, row = 2)
month = tk.Label(text = "Month")
month.grid(column = 0, row = 3)
day = tk.Label(text = "Day")
day.grid(column = 0, row = 4)
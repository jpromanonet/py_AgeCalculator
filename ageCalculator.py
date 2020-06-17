# We start by importing the neccesary libraries
# and by creating the GUI window

import tkinter as tk
window = tk.Tk()
window.geometry("620x780")
window.title(" Age Calculator App ")

# Now the labels

name = tk.Label(text = "Name")
name.grid(column = 0, row = 1)

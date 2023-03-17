# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 21:13:49 2023

@author: arifm
"""

import serial
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, OptionMenu, StringVar, Label, Button
from tkinter.ttk import Progressbar, Combobox

app = tk.Tk()

# Define the geometry of the window
app.geometry("600x400")

# Create dropdown menu for sequences
sequence_selected = StringVar()

dropdown = Combobox(app, width=20)
dropdown.set('Select Sequence')
dropdown.pack(pady=12, padx=10)
dropdown.place(x=0, y=0, anchor='nw')
dropdown['values'] = (' Sequence 1', ' Sequence 2', ' Sequence 3')

# Create a progress bar
the_progress = Progressbar(app, orient='horizontal', length=200, mode='determinate')
the_progress.pack(pady=12, padx=10)
the_progress.place(x=600, y=400, anchor='se')
the_progress.start(interval=100)

# Create a Serial object
ser = serial.Serial('COM4', baudrate=9600, timeout=1)

# Input function from Arduino, reads in the data
def input1(ser, label):
    data = ser.readline().decode('ascii').rstrip()
    label.config(text=data)
    label.after(10, input1, ser, label)

# Creating the label with text
label = Label(app, text="", font=("sans-serif", 20), fg="purple")
label.pack(pady=20)
label.place(x=170, y=400, anchor='sw')

# Runs the input1 to update the values
input1(ser, label)

# Creating label for temperature text
temp = Label(app, font=('calibri', 20), text='Temperature:', fg='purple')
temp.place(x=0, y=400, anchor='sw')

# Keep Running the window
app.mainloop()

#Fix for the main problem you should create a serial object outside of input1() function before calling the input1() function and then pass it through as the argument of the function alongside the label since it uses the serrial data. 
'''
Created on 02.01.2023

@author: Simon Trottberger
'''

import tkinter as tk
from tkinter import ttk
import sqlite3
from _functools import partial
from tkinter.colorchooser import askcolor
from sql_functions import *


def add_buttons_option(tab_list, opt_list):
#===============================================================================
# Fenster Optionen
#===============================================================================
    
    window_Titel_label = ttk.Label(tab_list[3], text="Fenster Optionen:")
    window_Titel_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
    
    window_size_label = ttk.Label(tab_list[3], text="Fenster Größe:")
    window_size_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
    
    x_label = ttk.Label(tab_list[3], text="X", width=2)
    x_label.grid(column=2, row=2, sticky=tk.W)

    size_x_entry=tk.StringVar()
    entry_x=tk.Entry(tab_list[3], textvariable=size_x_entry, selectbackground="blue")
    entry_x.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5, ipadx=1, ipady=1)
    size_x_entry.set(opt_list[0][1])
    sizex = entry_x.get()
    
    size_y_entry=tk.StringVar()
    size_y=tk.Entry(tab_list[3], textvariable=size_y_entry, selectbackground="blue")
    size_y.grid(column=3, row=2, sticky=tk.W, padx=5, pady=5)
    size_y_entry.set(opt_list[0][2])
    
    window_size_label = ttk.Label(tab_list[3], text="Schrift Größe:")
    window_size_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
    
    font_size_entry=tk.StringVar()
    font_size=tk.Entry(tab_list[3], textvariable=font_size_entry, selectbackground="blue")
    font_size.grid(column=3, row=3, sticky=tk.W, padx=5, pady=5)
    font_size_entry.set(opt_list[0][4])
    
    window_color_label = ttk.Label(tab_list[3], text="Farbe:")
    window_color_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
    
    color_label = tk.Label(tab_list[3], text = "Color", fg = "black")
    color_label.grid(column=3, row=4, sticky=tk.W, padx=5, pady=5)
    
    color_button = ttk.Button(tab_list[3], text="Farbe", command =partial(callback, color_label))
    color_button.grid(column=2, row=4, sticky=tk.W, padx=5, pady=5)
    
#===============================================================================
# Tabbelen Optionen
#===============================================================================
    #add empty label in row 0 and column 0
    l0 = tk.Label(tab_list[3], text='     \n   ', bg = 'black')
    l0.grid(column=0, row=5, columnspan=6,sticky=tk.EW,  padx=1, pady=1)

    
    window_Titel_label = ttk.Label(tab_list[3], text="Tabellen Optionen:")
    window_Titel_label.grid(column=0, row=6, sticky=tk.EW, padx=5, pady=5)
    
    window_size_label = ttk.Label(tab_list[3], text="Tabellen Schrift Größe:")
    window_size_label.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
    
    table_font_size_entry=tk.StringVar()
    table_font_size=tk.Entry(tab_list[3], textvariable=table_font_size_entry, selectbackground="blue")
    table_font_size.grid(column=3, row=7, sticky=tk.W, padx=5, pady=5)
    velue = None
    print(velue)
    if velue is None:
        print(table_font_size.get())
        print('variable is null')
        table_font_size_entry.set(opt_list[0][6])
    
    option_enty_list = [entry_x.get(),size_y.get(),font_size.get(), table_font_size.get()]
    return option_enty_list

def save_optionen(tab_list, opt_list):
    
    option_enty_list = add_buttons_option(tab_list, opt_list)
    
    print(opt_list[0][6])
    print(option_enty_list[3])
    
    

def callback(color_label):
    result = askcolor(title = "Color Chooser")
    color_label.configure(fg = result[1])
    print(result[1])
    user = getpass.getuser() #User auslesen
    options_normal_calor((result[1], user))
    
    
    
    
#Python

 '''
Created on 25.12.2022
#!python3
@author: Simon Trottberger
'''
# nötige Imports
import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from tkinter import Entry
import os
import argparse
import webbrowser
import sqlite3
from _functools import partial

from windows_frames import *
from sql_functions import *
from windows_functions import *
from optionen import *

def main_window():
    
   
    create_sql_table()
    opt_list = optionen_table_read_out()
    window = main_window_generate(opt_list)
    tab_list = tab_generate(window)
    option_enty_list = add_buttons_option(tab_list, opt_list)
    
    Treeview = intecreat_Table(tab_list)
    explorer_button_generate(tab_list[0])
    web_explorer_button_generate(tab_list[1])
    

    
    ttk.Button(tab_list[2],text="Neuer Daten Link anlegen", command=partial(new_explorer_link_popup_window, window, tab_list[0], Treeview)).pack()
    ttk.Button(tab_list[2], text="Neuer Web Link anlegen", command =partial(new_webbrowser_link_popup_window, window, tab_list[1], Treeview)).pack()
    ttk.Button(tab_list[2], text="Eintrag Löschen", command =partial(delete_entry, Treeview, tab_list, window)).pack()
    #===========================================================================
    # Optionen Fenster
    #===========================================================================
    
   
    
    save_button = ttk.Button(tab_list[3], text="Speichern", command =partial(save_optionen, tab_list,opt_list))
    save_button.grid(column=3, row=9, sticky=tk.W, padx=5, pady=5)
    
    
    
    window.mainloop()
    
if __name__ == '__main__':
    main_window()

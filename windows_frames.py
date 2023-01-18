'''
Created on 28.12.2022

@author: Simon Trottberger
'''
import tkinter as tk
from tkinter import ttk, Entry
from tkinter import Toplevel
from cgitb import text
from _curses import window
import webbrowser
from sql_functions import *
from Windows_functions import *
from tkinter.ttk import Treeview

def main_window_generate(opt_list):
    
    print(len(opt_list))
    width = opt_list[0][1]
    height = opt_list[0][2]
    window = tk.Tk() # Fenster Erzeugen
    window.title("Link-Verzeichnis") #Fenster Überschrift
    window.geometry(f"{width}x{height}") #Fenster Größe 
    window.config(bg='#050736')

#===============================================================================
# Style
#===============================================================================
 
    mygreen = "#76b3e8"
    myred = "#114d82"

    style = ttk.Style()
    

    style.theme_create( "yummy", parent="alt", settings={
       "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": mygreen },
            "map":       {"background": [("selected", myred)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

    style.theme_use("yummy")

    return window

#===============================================================================
# Tabs Erstellen
#===============================================================================
def tab_generate(window):

    tab_control=ttk.Notebook(window)
        
    explorer_links_frame = ttk.Frame(tab_control) #Explorer Tab hinzufügen
    tab_control.add(explorer_links_frame, text='Explorer links')
        
    webbrowser_links_frame = ttk.Frame(tab_control) #Webbrowser Tab hinzufügen
    tab_control.add(webbrowser_links_frame, text='Webbrowser links')
        
    add_new_links_frame = ttk.Frame(tab_control) #Links-Hinzufügen Tab hinzufügen
    tab_control.add(add_new_links_frame, text='Daten Verwalten')
        
    option_frame = ttk.Frame(tab_control)
    tab_control.add(option_frame, text='Optionen')

    # configure the grid
    option_frame.columnconfigure(0, weight=3)
    option_frame.columnconfigure(1, weight=3)
    
    tab_control.pack(expand=1, fill="both") #tabs sichtbar machen
        
    return explorer_links_frame, webbrowser_links_frame, add_new_links_frame, option_frame

#===============================================================================
# Tabelle erzeugen
#===============================================================================
def intecreat_Table(tab_list):
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure('Treeview', 
        background = 'silver',
        foreground = 'black',
        fieldbackground = 'blue',
        font=('arial', 18, 'italic')
        
        )
    style.map('Treeview', background=[('selected', 'green')])
    tree = ttk.Treeview(tab_list[2], selectmode="browse" , columns=(1,2,3,4), show='headings', height=8)
    tree = table_data_load(tree)
    
    tree.pack()
    return tree

#===========================================================================
# Link-Button Generieren
#===========================================================================
def explorer_button_generate(explorer_links_frame):
    explorer_links = sql_date_to_dictionary("explorer_links_ddp")
    for name, link in explorer_links.items():
        ttk.Button(explorer_links_frame, text=name, command= open_explorer_function_builder(link)).pack()
        
def web_explorer_button_generate(webbrowser_links_frame):
    web_explorer_links = sql_date_to_dictionary("web_explorer_links_ddp")
    for name, link in web_explorer_links.items():
        ttk.Button(webbrowser_links_frame, text=name, command=open_webbrowser_function_builder(link)).pack()
        
#===============================================================================
# Neue Einträge, Fenster
#===============================================================================
def new_explorer_link_popup_window(window, explorer_links_frame, Treeview):

    frame = tk.Tk() # Fenster Erzeugen
    frame.title("Neue Ordner Links Anlegen")
    frame.geometry("300x100")  #Fenster Größe
    frame.columnconfigure(1, weight=1)

#===============================================================================
# Labels erzeugen
#===============================================================================
    lablename = tk.Label(frame, text = "Link-Name:")
    lablename.grid(row = 0, column = 0, sticky = tk.W, pady = 2)
    
    lableurl = tk.Label(frame, text = "URL:")
    lableurl.grid(row = 1, column = 0, sticky = tk.W, pady = 2)
    
#===========================================================================
# Schreib Felder Erzeugen 
#===========================================================================
    new_name_entry = Entry(frame)
    new_name_entry.grid(row = 0, column = 1, pady = 2)
    new_url_entry = Entry(frame)
    new_url_entry.grid(row = 1, column = 1, pady = 2)
#===============================================================================
# Butteon erzeugen
#===============================================================================
    AddButton = ttk.Button(frame, text="Add", command=lambda:add_new_explorer_link(new_name_entry.get(),new_url_entry.get(), frame, explorer_links_frame, Treeview))
    AddButton.grid(row = 2, column = 1, pady = 2)
    
    
def new_webbrowser_link_popup_window(window, webbrowser_links_frame,Treeview):
    frame = tk.Tk() # Fenster Erzeugen
    frame.title("Neue WEB Links Anlegen")
    frame.geometry("300x100")  #Fenster Größe
    frame.columnconfigure(1, weight=1)

    lablename = tk.Label(frame, text = "Link-Name:")
    lablename.grid(row = 0, column = 0, sticky = tk.W, pady = 2)
    
    lableurl = tk.Label(frame, text = "WEB-URL:")
    lableurl.grid(row = 1, column = 0, sticky = tk.W, pady = 2)
    
    new_name_entry = Entry(frame)
    new_name_entry.grid(row = 0, column = 1, pady = 2)
    new_url_entry = Entry(frame)
    new_url_entry.grid(row = 1, column = 1, pady = 2)
    AddButten = ttk.Button(frame, text="Add", command=lambda:add_new_webbrowser_link(new_name_entry.get(),new_url_entry.get(), frame, webbrowser_links_frame, Treeview))
    AddButten.grid(row = 2, column = 1, pady = 2)
    
    
        
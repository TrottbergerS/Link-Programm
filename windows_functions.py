'''
Created on 30.12.2022
Windows_functions
@author: Simon Trottberger
'''
from windows_lib import *
from sql_functions import *
from tkinter.ttk import Treeview
from tkinter import colorchooser
import getpass
import tkinter as tk
from tkinter import *
from tkinter import ttk



 #==============================================================================
 # Öffnen von Daten im Explorer
 #==============================================================================
def open_explorer(link):
    os.startfile(link)
     
#===============================================================================
# Öffnen von Links im Standart Browser
#===============================================================================
def open_webbrowser(link):
    webbrowser.get('firefox').open(link)
    #webbrowser.open(link)
#===============================================================================
# Überprüfen ob der Fileexplorer offen ist
#===============================================================================
def open_explorer_function_builder(link):
    def open_explorer_function():
        open_explorer(link)
    return open_explorer_function
#===============================================================================
# Überprüfen ob der WEBbrowser offen ist
#===============================================================================
def open_webbrowser_function_builder(link):
    def open_webbrowser_function():
        open_webbrowser(link)
    return open_webbrowser_function

#===============================================================================
# Neuer Eintrag Button
#===============================================================================
def add_new_explorer_link(link_name, link, window, explorer_links_frame, Treeview):
#===============================================================================
#  Butten Erzeugen
#===============================================================================
    ttk.Button(explorer_links_frame, text=link_name, command= open_explorer_function_builder(link)).pack()
#==============================================================================
#Daten in SQL-Speichern 
#==============================================================================
    speicherart = "Explorer"
    load_data_at_db("explorer_links_ddp", link_name, link, speicherart, Treeview, explorer_links_frame)

    update_explorer_links(explorer_links_frame)
    window.destroy()

    
def add_new_webbrowser_link(name, link, window, webbrowser_links_frame, Treeview):
    ttk.Button(webbrowser_links_frame, text=name, command=open_webbrowser_function_builder(link)).pack()
    speicherart = "Web"
    load_data_at_db("web_explorer_links_ddp", name, link, speicherart, Treeview, webbrowser_links_frame)
    #update_web_explorer_links(webbrowser_links_frame)
    window.destroy()
#===============================================================================
# Selectiern in Tabelle möglich machen
#===============================================================================
def selectItem(tv, tab_list):
    curItem = tv.focus()
    marktid = tv.item(curItem)["values"][0]
    b1 = ttk.Button(tab_list[3], text="Markierten Link Läschen")
    b1. pack()
    style = ttk.Style()
    style.configure("Notebook", tabposition='n')
    style.theme_use("default")
    style.map("Treeview")
    
    #Configure the Treeview Colors
    style.configure("Treeview", 
        background="#38aecf",
        foreground="#343799",
        rowheight=25,
        fieldbackground="#D3D3D3")
    #Change Selected Color
    style.map('Treeview',
              background=[('selected', "#347083")])
    
#===========================================================================
# Selction der Tabele verwalten
#===========================================================================
    
def delete_entry(Treeview, tab_list, window):
    
    id = Treeview.selection()[0]
    delete_sql_task(id, Treeview, tab_list)
    update_explorer_links(tab_list[0])
    update_web_explorer_links(tab_list[1])
    window.update_idletasks()
    
#==============================================================================
# Butten eintrag regenerieren 
#==============================================================================
def update_explorer_links(frame):
    
    for widget in frame.winfo_children():
        widget.destroy()
        
    conn=create_sql_connection()
    curser = conn.cursor()
    curser.execute("SELECT * FROM explorer_links_ddp")
    inhalt = curser.fetchall()
    counter = 0 
    for name, link, speicherort, id in inhalt:
        ttk.Button(frame, text=inhalt[counter][0], command= open_explorer_function_builder(inhalt[counter][1])).pack()
        counter +=1
    print("Üpdate explorer Links")
def update_web_explorer_links(frame):
    
    for widget in frame.winfo_children():
        widget.destroy()
        
    conn=create_sql_connection()
    curser = conn.cursor()
    curser.execute("SELECT * FROM web_explorer_links_ddp")
    inhalt = curser.fetchall()
    counter = 0 
    for name, link, speicherort, id in inhalt:
        ttk.Button(frame, text=inhalt[counter][0], command= open_explorer_function_builder(inhalt[counter][1])).pack()
        counter +=1
    
    

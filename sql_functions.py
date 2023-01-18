'''
Created on 28.12.2022

@author: Simon Trottberger
'''
import tkinter as tk
from tkinter import ttk
import sqlite3
from unittest import result
from symbol import parameters
from itertools import count
from tkinter.ttk import Treeview
import getpass


#===============================================================================
# Datenbang Connecten 
#===============================================================================
def create_sql_connection():
    # creat a database connection to the SQLite database specifield by the db_file
    
    conn = None
    try:
        conn = sqlite3.connect("link-Samlung.db")
    except Error as e:
        print(e)
    return conn

#===============================================================================
# Eintrag in Datenbank Löschen
#===============================================================================
def delete_sql_task(id, Treeview, tab_list):
    #Delete a task by task id 
    
    conn = create_sql_connection()
    
    sql = 'DELETE FROM web_explorer_links_ddp WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
   
    sql = 'DELETE FROM explorer_links_ddp WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
    conn.close
    print("Eintrag Gelöscht: ")
    print(id)
    Treeview.delete(id)
    
#===============================================================================
# SQL-Datenbank einträge ausdrucken
#===============================================================================
def print_database():
    conn=create_sql_connection()
    curser = conn.cursor()
    curser.execute("SELECT * FROM place=?")
    inhalt = zeiger.fetchall()
    print(inhalt)
    conn.close   

#===============================================================================
# Datenbank Erzeugen wenn noch nicht vorhanden
#===============================================================================
def create_sql_table():
    conn= create_sql_connection()
    cursor= conn.cursor() #Curser Setzen
#===============================================================================
# Web-Explorer Tabelle erzeugen
#===============================================================================
    sql_anweisung = """
    CREATE TABLE IF NOT EXISTS web_explorer_links_ddp (
    name VARCHAR(50), 
    link VARCHAR (200),
    speicherart VARCHAR(20),
    id VARCHAR(20)
    );"""
    cursor.execute(sql_anweisung) #anweisung setzten
    conn.commit() #anweisung übergeben
    
#===============================================================================
# Ordner Tabelle erzeugen
#===============================================================================
    sql_anweisung ="""
    CREATE TABLE IF NOT EXISTS explorer_links_ddp (
    name VARCHAR(50), 
    link VARCHAR (200),
    speicherart VARCHAR(20),
    id VARCHAR(20)
    );"""
    cursor.execute(sql_anweisung) # anweisung setzen
    conn.commit()# anweisung übergeben
    cursor.execute(sql_anweisung) #anweisung setzten
    conn.commit() #anweisung übergeben
#===============================================================================
# Optionen Tabelle erzeugen
#===============================================================================
    sql_anweisung ="""
    CREATE TABLE IF NOT EXISTS options_ddp (
    user VARCHAR(50),
    sizex INTEGER(50), 
    sizey INTEGER(50),
    color VARCHAR (50),
    fontsize INTEGER(3),
    font VARCHAR(20),
    tablefontsize INTEGER(3)
    );"""
    cursor.execute(sql_anweisung) # anweisung setzen
    
    conn = create_sql_connection()
    cursor = conn.cursor()
    sqlleng1 = cursor.execute('''SELECT count(*) FROM options_ddp''')
#===============================================================================
# Überprüfen wenn User nicht vorhanden neuen eintag für User Erzeugen
#===============================================================================

    logged_user = getpass.getuser() #User auslesen
    sql = "SELECT * FROM options_ddp WHERE user=(?)"
    cursor.execute(sql, (logged_user,))
    p = cursor.fetchone()
    
    if p is None:
        print ("Den Nutzer gibt's nicht")
        try:
            sql = f'INSERT OR IGNORE INTO options_ddp (user, sizex, sizey, color,fontsize, font,tablefontsize ) VALUES ("{logged_user}", "800", "400", "#0b0d0b","25","times","25")'
        except sqlite3.IntegrityError as e:
            print('INTEGRITY ERROR\n')
            print(traceback.print_exc())
        cursor.execute(sql)
    else:
        print("Dieser Nutzer existiert")
    
    conn.commit()# anweisung übergeben

    conn.close()
#===============================================================================
# Explorer Links in Dictionary umschreiben
#===============================================================================
def sql_date_to_dictionary(table):
    dicforLinks = {} # Dictionary setzen
    conn = create_sql_connection()
    cursor = conn.cursor()
    query = 'SELECT * FROM {}'.format(table)
    cursor.execute(query)
    explorer_table = cursor.fetchall()
    for dsatz in explorer_table:
        dicforLinks[dsatz[0]] = dsatz[1]
    conn.close()
    return dicforLinks
#===============================================================================
# Daten in SQL-Datenbang eintragen
#===============================================================================
def load_data_at_db(tablename, name, link, speicherart, Treeview, explorer_links_frame):
    
    conn = create_sql_connection()
    cursor = conn.cursor()
    sqlleng1 = cursor.execute('''SELECT count(*) FROM explorer_links_ddp''')
    id = table_lengh_all()
    
    try:
        sql = f'INSERT INTO {tablename} (name, link, speicherart, id) VALUES ("{name}", "{link}", "{speicherart}", "{id}" )'
    except sqlite3.IntegrityError as e:
        print('INTEGRITY ERROR\n')
        print(traceback.print_exc())
    cursor.execute(sql)
    conn.commit()
    conn.close()
    Treeview.insert(parent= '',index = 'end' , iid = id, values=(name, link, speicherart, id))

    
    
#===============================================================================
# Daten von SQL-Datenbank auslessen und in Tabellenvormat Packen
#===============================================================================
def table_data_load(Treeview):
    
    Treeview.heading(1, text="Name")
    Treeview.heading(2, text="Link")
    Treeview.heading(3, text="Speicherart")
    Treeview.heading(4, text="ID")
    
    conn = create_sql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM web_explorer_links_ddp")
    web_table = cursor.fetchall()
    count=0
    for dsatz in web_table:
        Treeview.insert(parent= '',index = 'end' , iid = count, values=(dsatz[0], dsatz[1], dsatz[2], dsatz[3]))
        count += 1
    cursor.execute("SELECT * FROM explorer_links_ddp")
    explorer_table = cursor.fetchall()
    count= len(Treeview.get_children())
    for dsatz in explorer_table:
        Treeview.insert(parent= '',index = 'end' , iid = count, values=(dsatz[0], dsatz[1], dsatz[2], dsatz[3]))
        count += 1
    conn.close()
    
    return Treeview
#===============================================================================
# Tabellen Länge einer einzelnen Tabelle auslesen
#===============================================================================
def table_lengh(tablename):
    
    conn = create_sql_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {tablename}')
    web_table = cursor.fetchall()
    count=0
    for dsatz in web_table:
        count += 1
    conn.close()
    return count
#===============================================================================
# Tabellenlänge der Beiden Tabellen Web- und Explore auslesen
#===============================================================================
def table_lengh_all():
    
    conn = create_sql_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM web_explorer_links_ddp')
    web_table = cursor.fetchall()
    count=0
    for dsatz in web_table:
        count += 1
    cursor.execute(f'SELECT * FROM explorer_links_ddp')
    web_table = cursor.fetchall()
    for dsatz in web_table:
        count += 1
    conn.close()
    return count
#===============================================================================
# Auslesen der Optionen
#===============================================================================
def optionen_table_read_out():
    
    conn = create_sql_connection()
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM options_ddp')
    opt_table = cursor.fetchall()
    conn.close()
    return opt_table

#===============================================================================
# sql Normale Farbe aus datenbank auslessen
#===============================================================================
    
def options_normal_calor(task):
    user = getpass.getuser() #User auslesen
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    conn = create_sql_connection()
    cursor = conn.cursor()
    sql = ''' UPDATE options_ddp
              SET color = ?
              WHERE user = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    conn.close()
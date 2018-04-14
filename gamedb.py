#!/usr/bin/python3
import sqlite3
import datetime
import sys
import datetime 
import os
import termios
import tty
import tkinter

conn = sqlite3.connect("game_db.db")
record_start_time = datetime.datetime.now()
record_end_time = datetime.datetime.now()
record_id = -1
timer_started = False




def create_record(lbl_timer):
    global record_start_time, record_id
    record_start_time = datetime.datetime.now()
    c = conn.cursor()
    qry_max_id = "SELECT MAX(game_record_id) FROM GameRecords;"
    c.execute(qry_max_id)
    max_id = c.fetchone()[0]
    if(max_id == None):
        max_id = 0
    record_id = max_id + 1



def add_game():
    print("adding game")

def add_comment():
    print("adding comment")

def pause_record():
    print("pause record")

def save_record(play_game_page, v_game, v_record_type):
    print("Save record")
    global record_end_time
    qry_save_record = "INSERT INTO"

    record_end_time = datetime.datetime.now()
    duration = record_end_time - record_start_time
    record_type = v_record_type.get() 
    game_id = v_game.get().split()[0]
    
    
    print("duration =", duration)
    print("record type =", record_type)
    print("game_id =", game_id)
    
    play_game_page.destroy()



def play_game():
    game_is_started = False
    play_game_page = tkinter.Tk(className= "Play Game")
    play_game_page.geometry("300x300")
    record_types = ["CG Video", "Fight", "Free Discovery", "Puzzle Solving", "Useless", "Genre-fit gameplay"]

    # fetching gmae info from db
    c = conn.cursor()
    game_names = []
    game_id = []
    qry_game_info = "SELECT game_id, game_name FROM Games;"
    c.execute(qry_game_info)
    result = c.fetchall()
    for row in result:
        game_names.append( str(row[0])+ " " +str(row[1]))

    # drop down menus
    v_game = tkinter.StringVar(play_game_page)
    v_game.set(game_names[0])
    menu_games = tkinter.OptionMenu(play_game_page, v_game, *game_names)
    menu_games.place(anchor = 's',relx = 0.5, rely = 0.3)

    v_record_type = tkinter.StringVar(play_game_page)
    v_record_type.set(record_types[0])
    menu_record_types = tkinter.OptionMenu(play_game_page, v_record_type, *record_types)
    menu_record_types.place(anchor = 's',relx = 0.5, rely = 0.4)

    # buttons 
    label_timer = tkinter.Label(play_game_page, text="00:00")
    label_timer.place(anchor= 's', relx=0.5, rely = 0.2)

    btn_play_game = tkinter.Button(play_game_page, text = "Start Record", command =  lambda: create_record(label_timer))
    btn_play_game.place(anchor = 's',relx = 0.25, rely = 0.6)

    btn_add_game = tkinter.Button(play_game_page, text = "Add New Game", command = add_game)
    btn_add_game.place(anchor = 's',relx = 0.75, rely = 0.6)

    btn_pause_game = tkinter.Button(play_game_page, text = "Pause", command = pause_record)
    btn_pause_game.place(anchor = 's',relx = 0.25, rely = 0.7)

    btn_add_comment = tkinter.Button(play_game_page, text = "Add Comment", command = add_comment)
    btn_add_comment.place(anchor = 's',relx = 0.75, rely = 0.7)


    btn_play_game = tkinter.Button(play_game_page, text = "Save", command = lambda: save_record(play_game_page,v_game, v_record_type))
    btn_play_game.place(anchor = 's',relx = 0.5, rely = 0.9)


    play_game_page.mainloop()

def close_db():
    exit(0)

def browse_data():
    print("asdf")

def main_menu(conn):
    main_page = tkinter.Tk(className="GameDB")
    main_page.geometry("200x200")
    btn_play_game = tkinter.Button(main_page, text = "Play Game", command = play_game)
    btn_play_game.place(anchor = 's',relx = 0.5, rely = 0.4)
    
    btn_close = tkinter.Button(main_page, text = "Browse Game Data", command = browse_data)
    btn_close.place(anchor = 's',relx = 0.5, rely = 0.6)

    btn_close = tkinter.Button(main_page, text = "Close", command = close_db)
    btn_close.place(anchor = 's',relx = 0.5, rely = 0.8)
    
    main_page.mainloop()

def main():
    
    choice = 0
    main_menu(conn)
    '''
    choice = main_menu()
    if(choice == 1):
        play_game(conn)
    elif(choice == 2):
        browse_data()
    else:
        print("Terminating program...")
        exit(0)
    '''

main()
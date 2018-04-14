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
    global conn
    global record_start_time, record_id
    record_start_time = datetime.datetime.now()
    c = conn.cursor()
    qry_max_id = "SELECT MAX(game_record_id) FROM GameRecords;"
    qry_create_record = "INSERT INTO GameRecords VALUES(?,?,?,?,?,?);"
    c.execute(qry_max_id)
    max_id = c.fetchone()[0]
    if(max_id == None):
        max_id = 0
    record_id = max_id + 1
    values = [record_id, record_start_time.strftime("%B %d, %Y %I:%M%p") ,\
              record_start_time.strftime("%B %d, %Y %I:%M%p"), "NA",\
              record_start_time.strftime("%I:%M%p"), -1]
    c.execute(qry_create_record,values)
    conn.commit()
    print("Record created")




def add_game():
    print("-----adding game-----")

def save_comment(page, comment_type, score, comment, game_id, record_id, level):
    print("-----comment saved-----")
    c = conn.cursor()
    qry_max_id = "SELECT MAX(comment_id) FROM Comments;"
    c.execute(qry_max_id)
    max_id = c.fetchone()[0]
    if(max_id == None):
        max_id = 0
    comment_id = max_id + 1
    qry_save_comment = "INSERT INTO Comments VALUES(?,?,?,?,?,?,?,?,?);"

    value_list = [comment_id, datetime.datetime.now().strftime("%B %d, %Y %I:%M%p")\
                  ,comment_type, score, game_id, 0, comment, level, record_id]
    c.execute(qry_save_comment, value_list)
    conn.commit()


    page.destroy()



def add_comment(level, game_id, record_id):
    print("-----adding comment-----")
    page_add_comment = tkinter.Tk(className="Adding Comment")
    page_add_comment.geometry("300x300")
    print(level)
    # textbox
    v_comment_type = tkinter.StringVar(page_add_comment)
    v_comment_type.set("type")
    tb_comment_type = tkinter.Entry(page_add_comment, bd = 2, textvariable=v_comment_type)
    tb_comment_type.place(anchor = 's', relx=0.5, rely = 0.2)

    v_score = tkinter.StringVar(page_add_comment)
    v_score.set("1")
    tb_score = tkinter.Entry(page_add_comment, bd = 1, textvariable=v_score)
    tb_score.place(anchor = 's', relx=0.5, rely = 0.3)

    #v_comment = tkinter.StringVar(page_add_comment)
    tb_comment = tkinter.Text(page_add_comment, width=20, height=7)
    tb_comment.place(anchor = 'n', relx=0.5, rely = 0.33)

    # button
    btn_cancel = tkinter.Button(page_add_comment, text="Cancel", command=page_add_comment.destroy)
    btn_cancel.place(anchor= 'n', relx=0.75, rely=0.8)
    btn_save = tkinter.Button(page_add_comment, text="Save", command=lambda:save_comment(page_add_comment, \
                              v_comment_type.get(), int(v_score.get()), tb_comment.get(1.0, "end-1c"), game_id, \
                              record_id, level))
    
    btn_save.place(anchor= 'n', relx=0.25, rely=0.8)


    page_add_comment.mainloop()

def pause_record():
    print("-----pause record-----")

def save_record(play_game_page, v_game, v_record_type):
    global record_end_time,conn
    c = conn.cursor()
    qry_save_record = "UPDATE GameRecords SET end_time = ?, duration = ?, game_id = ?, record_type = ?\
                       WHERE game_record_id = ?;"

    record_end_time = datetime.datetime.now()
    duration = record_end_time - record_start_time
    record_type = v_record_type.get() 
    game_id = int(v_game.get().split()[0])

    print("duration =", duration)
    print("record type =", record_type)
    print("game_id =", game_id)
    c.execute(qry_save_record, [record_end_time.strftime("%B %d, %Y %I:%M%p"), str(duration), game_id, record_type, record_id])
    conn.commit()
    print("-----Save record-----")
    play_game_page.destroy()



def play_game():
    game_is_started = False
    play_game_page = tkinter.Tk(className= "-----Play Game-----")
    play_game_page.geometry("300x400")
    record_types = ["CG Video", "Fight", "Free Discovery", "Puzzle Solving", "Useless", "Genre-fit gameplay"]

    # fetching gmae info from db
    c = conn.cursor()
    game_names = []
    game_id = []
    level = "1"
    qry_game_info = "SELECT game_id, game_name FROM Games;"
    c.execute(qry_game_info)
    result = c.fetchall()
    for row in result:
        game_names.append( str(row[0])+ " " +str(row[1]))

    # textbox
    v_level = tkinter.StringVar(play_game_page)
    tb_level = tkinter.Entry(play_game_page, bd = 3, textvariable=v_level)
    tb_level.place(anchor = 's', relx=0.5, rely = 0.5)


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

    btn_add_comment = tkinter.Button(play_game_page, text = "Add Comment", command = lambda: add_comment(v_level.get(),\
                                     int(v_game.get().split()[0]), record_id))
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
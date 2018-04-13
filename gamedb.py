#!/usr/bin/python3
import sqlite3
import datetime
import sys
import time 
import os
import termios
import tty
import tkinter

conn = sqlite3.connect("game_db.db")
'''
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def print_menu(menu_title, list_to_print):
    os.system("clear")
    print("--------", menu_title, "--------")
    for i in range(len(list_to_print)):

def main_menu():
    menu = ["Play Game", "Browse Game Data", "Quit"]
    print_menu("Main Menu", menu)
    while True:
        char = getch()
        if (char in "123"):
            choice = int(char)
            break
    return choice

def add_new_game(conn):
    title = "Adding New Game"


# play_status: 0 = unplayed, 1 = playing, 2 = finished
def play_game(conn):
    c = conn.cursor()
    query = "SELECT game_id, game_name \
             FROM Games\
             WHERE play_status = 1; "
    menu_title = "Play Game"
    game_id = []
    game_names = []
    choice_list = []
    c.execute(query)
    results = c.fetchall()
    for row in results:
        print(row[0], row[1])
    game_names.append("Add a new game")
    print_menu(menu_title,game_names)
    choice_list = [i+1 for i in range(len(game_names))]

    while True:
        choice = int(input("Your Choice: "))
        if choice in choice_list:
            break
    if (choice == choice_list[-1]):
        add_new_game(conn)    

def browse_data():
    print("Browse game data")

'''

def play_game():
    play_game_page = tkinter.Tk(className= "Play Game")
    play_game_page.geometry("600x300")


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
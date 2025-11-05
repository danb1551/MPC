from lib import *
import tkinter as tk
from tkinter import ttk
import os
import curses
from canvalib import Canvas
from dotenv import load_dotenv


CONFIG_FILE = "CONFIG.cfg"
DEFAULT_CONFIG = """
music_dir = ./test
last_played = 0 # index of last played song in playlist
"""
MUSIC_DIR: str
LAST_PLAYED: int


################# function defining #################

def init():
    try:
        if not os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "w") as f:
                f.write(DEFAULT_CONFIG)
        else:
            load_dotenv()
            MUSIC_DIR = os.getenv("MUSIC_DIR")
            LAST_PLAYED = os.getenv("LAST_PLAYED")
    except Exception as e:
        print(f"SORRY bro but something unexpected broke: {e}")

def play_music(*args):
    player.play()

def add_dir_to_playlist(*args, dir: str = os.path.expanduser("~/Hudba")):
    for items in os.listdir(dir):
        if items.endswith(".mp3") or items.endswith(".wav"):
            player.add_to_playlist(os.path.join(dir, items))

def stop_music(*args):
    player.stop()

def next(*args):
    player.next()

def show_help():
    pass

def prev():
    player.prev()

################# declaring variables #################

player = MusicPlayer()

################# main loop #################

def clear_screen():
    print("\033[H\033[J", end="")

def main(stdscr):
    init()
    stdscr.nodelay(True)

    c = Canvas()
    c.add_text(10, 10, "ddddddddddddddd")
    c.render()

    while True:
        key = stdscr.getch()
        if key == -1:
            continue

        before = list(c.rows)

        if key in (ord("p"), ord("s")):
            play_music()
        elif key == ord("h"):
            show_help()
        elif key == ord("a"):
            add_dir_to_playlist()
        elif key == curses.KEY_UP:
            prev()
        elif key == curses.KEY_DOWN:
            next()
        elif key == ord("q"):
            break

        if c.rows != before:
            clear_screen()
            c.render()


curses.wrapper(main)
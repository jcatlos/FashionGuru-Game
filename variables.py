from tkinter import *

NAME = "Fashion Guru"
FPS = 60
FREQ = 1000//FPS

GAME_HEIGHT = 10
GAME_WIDTH = 10

BAR_TOTAL_LEN = GAME_WIDTH

BG_COLOR = "Black"
FONT_SIZE = 30
NORMAL_FONT = "Courier "+str(FONT_SIZE)+" bold"
FONT_COLOR = "White"
COLORS = ["Red", "Green", "Blue", "Yellow"]

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 900
BAR_HEIGHT = FONT_SIZE
LOWER_HEIGHT = FONT_SIZE * 6
UPPER_HEIGHT = SCREEN_HEIGHT - LOWER_HEIGHT - BAR_HEIGHT

MOVES = {'w':[-1, 0], 's':[1,0], 'a':[0,-1], 'd':[0,1]}
COLOR_CHANGES = {'g':0, 'h':1, 'j':2, 'k':3}
COLOR_CHANGES_KEYS = ['g', 'h', 'j', 'k']
SHAPE_CHANGES = {'v':0, 'b':1, 'n':2, 'm':3}
SHAPE_CHANGES_KEYS = ['v', 'b', 'n', 'm']
STATE_CAHNGE = 'q'

PLAYER_CHAR = 'x'
LEVEL_CHAR = '#'
BAR_CHAR = '#'

LEVELS = ['PONOŽKY V SANDÁLOCH', 'ROZGAJDANÉ TEPLÁKY', 'CROCSY', 'SLIPY NA NOHAVICIACH', 'FEDORA']

ROOT = Tk()
ROOT.title = NAME
ROOT.resizable(False, False)



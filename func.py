from tkinter import *
from random import randint
from pygame import init, mixer

from variables import *

state = []
shapes = []
shapesCanvas = []
player_color = 0
total_score = 0
score = 0
level = 0


init()
mixer.init(channels=2)
mixer.music.load('background.wav')
mixer.music.play(-1)

lvl_sound = mixer.Sound('levelup.wav')
sound1 = mixer.Sound('sound1.wav')
sound2 = mixer.Sound('sound2.wav')

def LtoS(table):
  output = ''
  for row in table:
    for char in row:
      output += char
  return output

def killall():
  for widget in ROOT.winfo_children():
      widget.destroy()

def help():
  def back():
    screen.destroy()
    menu()

  screen = Frame(ROOT, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg=BG_COLOR) 
  with open('help.txt') as f:
    input_text = str(f.read())
  title = Label(screen, text="Nápoveda", font=NORMAL_FONT,
          bg=BG_COLOR, fg=COLORS[3])
  napoveda = Text(screen, width=70, height=30, bg=BG_COLOR, 
             fg=FONT_COLOR, font='Monospace 15', highlightthickness=0, bd=0)
  napoveda.insert(END, input_text)
  back_button = Button(screen, text="Späť", command=back, bg=BG_COLOR, 
                font="Monospace 20 bold", fg=COLORS[0], relief="flat", activeforeground=FONT_COLOR,
                activebackground=BG_COLOR, highlightthickness=0, bd=0)

  title.place(anchor='n', x=SCREEN_WIDTH//2, y=25)
  napoveda.place(anchor='n', x=SCREEN_WIDTH//2, y=100)
  back_button.place(anchor='s', x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT-30)
  screen.pack()

  screen.mainloop()

def game_over():
  global total_score, level
  killall()
  screen = Frame(ROOT, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, 
           bg=BG_COLOR) 
  gameover = Label(screen, text="Prehral si :(", font=NORMAL_FONT, 
             bg=BG_COLOR, fg=COLORS[0])
  lose_text = "Nahral si "+str(total_score)+" bodov, neprekonal si "+LEVELS[level].lower()
  score_label = Label(screen, text=lose_text, font="Monospace 15 bold", 
                bg=BG_COLOR, fg=FONT_COLOR)
  back_button = Button(screen, text="Vypnúť hru", command=ROOT.quit, bg=BG_COLOR, 
                font="Monospace 20 bold", fg=COLORS[3], relief="flat", activeforeground=FONT_COLOR,
                activebackground=BG_COLOR, highlightthickness=0, bd=0)

  gameover.place(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//3, anchor='center')
  score_label.place(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2, anchor='center')
  back_button.place(anchor='s', x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT-30)
  screen.pack()
  screen.mainloop()

def you_won():
  killall()
  screen = Frame(ROOT, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg=BG_COLOR) 
  win = Label(screen, text="Vyhral si!", font=NORMAL_FONT, bg=BG_COLOR, 
        fg=COLORS[3])
  wintext="Stal si sa odborníkom na módu, zbalil si svoju vytúženú \na obaja ste žili šťastne až do rozvodu..."
  win_text = Label(screen, text=wintext, font="Monospace 15 bold", 
             bg=BG_COLOR, fg=FONT_COLOR)
  win.place(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//3, anchor='center')
  win_text.place(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2, anchor='center')
  screen.pack()
  screen.mainloop()

def play():
  player_list = []
  score = 0
  
  def generatePlayer(size):
    global player 
    pos = [0,0]
    player = []
    player.append([0,0])
    for i in range(size + randint(0,2)-1):
      index = randint(0,1)
      pos[index] += 1
      player.append([pos[0],pos[1]])

  def generateColors():
    player_colors = []
    for i in range(len(player)):
      player_colors.append(randint(0,3))
    return player_colors

  def generateState():
    global state
    state = []
    for h in range(GAME_HEIGHT):
      row = []
      for w in range(GAME_WIDTH):
        row.append(randint(0,3))
      state.append(row)
    #return(state)

  def renderBar(score):
    global level
    bar = ""
    for i in range(score):
      bar += BAR_CHAR
    screen.itemconfig(bar_canvas, text=bar)
    screen.itemconfig(level_canvas, text=LEVELS[level])

  def renderBottom(shapes, shapesCanvas):
    it = 0
    for shape in shapes:
      act_shape = []
      for i in range(4):
        row = []
        for j in range(4):
          if [i,j] in shape:
            row.append(PLAYER_CHAR)
          else:
            row.append(' ')
        row.append('\n')
        act_shape.append(row)
      act_shape_str = LtoS(act_shape)
      try:
        screen.itemconfig(shapesCanvas[it], text=act_shape_str)
      except IndexError:
        shape_x = SCREEN_WIDTH * (it+1) // 4 - (FONT_SIZE*4)
        shape_y = SCREEN_HEIGHT - (LOWER_HEIGHT // 2) -20
        shapesCanvas.append(screen.create_text(shape_x, shape_y, text=act_shape_str, font=NORMAL_FONT, fill=FONT_COLOR))
      it += 1

  def renderState(state, player):
    global player_text, red_text, green_text, blue_text, yellow_text
    red = []
    green = []
    blue = []
    yellow = []

    for row in state:
      red_row = []
      green_row = []
      blue_row = []
      yellow_row = []
      for c in row:
        #print(c)
        if c == 0:
          red_row.append(LEVEL_CHAR)
          green_row.append(' ')
          blue_row.append(' ')
          yellow_row.append(' ')
        elif c == 1:
          red_row.append(' ')
          green_row.append(LEVEL_CHAR)
          blue_row.append(' ')
          yellow_row.append(' ')
        elif c == 2:
          red_row.append(' ')
          green_row.append(' ')
          blue_row.append(LEVEL_CHAR)
          yellow_row.append(' ')
        elif c == 3:
          red_row.append(' ')
          green_row.append(' ')
          blue_row.append(' ')
          yellow_row.append(LEVEL_CHAR)
      red_row.append('\n')
      green_row.append('\n')
      blue_row.append('\n')
      yellow_row.append('\n')
      red.append(red_row)
      green.append(green_row)
      blue.append(blue_row)
      yellow.append(yellow_row)
        
    player_list = []

    for i in range(GAME_HEIGHT):
      player_row = []
      for j in range(GAME_WIDTH):
        player_row.append(' ')
      player_row.append('\n')
      player_list.append(player_row)

    for coords in player:
       player_list[coords[0]][coords[1]] = PLAYER_CHAR

    try:
      screen.itemconfig(player_text, text=LtoS(player_list))
      screen.itemconfig(red_text, text=LtoS(red))
      screen.itemconfig(green_text, text=LtoS(green))
      screen.itemconfig(blue_text, text=LtoS(blue))
      screen.itemconfig(yellow_text, text=LtoS(yellow))
    except NameError:
      red_text = screen.create_text(SCREEN_WIDTH//2, 
                 UPPER_HEIGHT//2-20, text=LtoS(red), 
                 font=NORMAL_FONT, fill=COLORS[0])
      green_text = screen.create_text(SCREEN_WIDTH//2, 
                   UPPER_HEIGHT//2-20, text=LtoS(green), 
                   font=NORMAL_FONT, fill=COLORS[1])
      blue_text = screen.create_text(SCREEN_WIDTH//2, 
                  UPPER_HEIGHT//2-20, text=LtoS(blue), 
                  font=NORMAL_FONT, fill=COLORS[2])
      yellow_text = screen.create_text(SCREEN_WIDTH//2, 
                    UPPER_HEIGHT//2-20, text=LtoS(yellow), 
                    font=NORMAL_FONT, fill=COLORS[3])
      player_text = screen.create_text(SCREEN_WIDTH//2, 
                    UPPER_HEIGHT//2-20, text=LtoS(player_list), 
                    font=NORMAL_FONT, fill=COLORS[player_color])
   
  def checkState():
    global player_color, state
    for coords in player:
      if not state[coords[0]][coords[1]] == player_color:
        return False
    return True

  def changePlayer(key):
    global player, shapes
    diff0 = player[0][0]
    diff1 = player[0][1]
    for coords in player:
      coords[0] -= diff0
      coords[1] -= diff1
    tmp = shapes[SHAPE_CHANGES[key]]
    shapes[SHAPE_CHANGES[key]] = player
    player = tmp
    renderState(state, player)
    renderBottom(shapes, shapesCanvas)

  def move(key):
    player_list = []

    for i in range(GAME_HEIGHT):
      player_row = []
      for j in range(GAME_WIDTH):
        player_row.append(' ')
      player_row.append('\n')
      player_list.append(player_row)

    for coords in player:
      coords[0] = (coords[0] + MOVES[key][0])%GAME_HEIGHT
      coords[1] = (coords[1] + MOVES[key][1])%GAME_WIDTH
    for coords in player:
       player_list[coords[0]][coords[1]] = PLAYER_CHAR
    screen.itemconfig(player_text, text=LtoS(player_list))

  def changeColor(key):
    global player_color
    player_color = COLOR_CHANGES[key]
    screen.itemconfig(player_text, fill=COLORS[player_color])

  def changeState(key):
    global state, score, level, shapes, total_score
    if checkState():
      mixer.Channel(0).play(sound1)
      if score == GAME_WIDTH:
        mixer.Channel(1).play(lvl_sound)
        total_score += score
        score = 0
        level += 1
        shapes = []
        for i in range(4):      
          generatePlayer(level+1)
          shapes.append(player)
        renderBottom(shapes, shapesCanvas)
        if level == len(LEVELS):
          you_won()
      else:
        score += 1
      renderBar(score)
    else:
      mixer.Channel(0).play(sound2)
      score -= 1
      if score == -1:
        game_over()
      renderBar(score)
    generateState()
    renderState(state, player)
  
  def keypress(event):
    global player
    key = event.char
    if key in MOVES:
      move(key)
    elif key in COLOR_CHANGES:
      changeColor(key)
    elif key == STATE_CAHNGE:
      changeState(key)
      generatePlayer(level+1)
      renderState(state, player)
    elif key in SHAPE_CHANGES:
      changePlayer(key)

  ''' MAIN: '''
  generateState()
  for i in range(4):      
    generatePlayer(level+1)
    shapes.append(player)
  generatePlayer(score+1)
  screen = Canvas(ROOT, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, 
           bg=BG_COLOR)
  screen.focus_set()
  screen.bind("<Key>", keypress)
  screen.pack()
  
  pos_x = (SCREEN_WIDTH//2)-FONT_SIZE*(GAME_WIDTH//2 - 1)
  pos_y = UPPER_HEIGHT-2*FONT_SIZE-100

  level_canvas = screen.create_text(SCREEN_WIDTH//2, 20, text=LEVELS[level], 
                 font=NORMAL_FONT, fill=FONT_COLOR, anchor='n')
  bar_canvas = screen.create_text(pos_x, pos_y, text="", 
               font=NORMAL_FONT, fill=FONT_COLOR, anchor='nw')

  for i in range(4):
    letter_x = SCREEN_WIDTH * (i+1) // 4  - (FONT_SIZE*4)
    letter_y = SCREEN_HEIGHT - (LOWER_HEIGHT // 2) - (FONT_SIZE*4) - 40
    screen.create_text(letter_x, letter_y, text=SHAPE_CHANGES_KEYS[i], 
    font=NORMAL_FONT, fill=FONT_COLOR, anchor='center')
    screen.create_text(letter_x, letter_y-50, text=COLOR_CHANGES_KEYS[i], 
    font=NORMAL_FONT, fill=COLORS[i], anchor='center')

  renderBottom(shapes, shapesCanvas)
  renderState(state, player)
  renderBar(score)
def menu():
  def go_play():
    screen.destroy()
    play()

  def go_settings():
    #NASTAVENIA - DOROBIT
    pass
  def go_help():
    screen.destroy()
    help()

  screen = Canvas(ROOT, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg=BG_COLOR)
  game_title = Label(screen, text=NAME, bg=BG_COLOR, 
                font="Monospace 70 bold", fg=FONT_COLOR,)
  play_button = Button(screen, text="Hraj", command=go_play, bg=BG_COLOR, 
                font=NORMAL_FONT, fg=COLORS[0], relief="flat", activeforeground=FONT_COLOR,
                activebackground=BG_COLOR, highlightthickness=0, bd=0)
  settings_button = Button(screen, text="Nastavenia", command=go_settings, bg=BG_COLOR, 
                    font=NORMAL_FONT, fg=COLORS[1], relief="flat", activeforeground=FONT_COLOR,
                    activebackground=BG_COLOR, highlightthickness=0, bd=0)
  help_button = Button(screen, text="Nápoveda", command=go_help, bg=BG_COLOR, 
                font=NORMAL_FONT, fg=COLORS[2], relief="flat", activeforeground=FONT_COLOR,
                activebackground=BG_COLOR, highlightthickness=0, bd=0)
  quit_button = Button(screen, text="Vypnúť hru", command=ROOT.quit, bg=BG_COLOR, 
                font=NORMAL_FONT, fg=COLORS[3], relief="flat", activeforeground=FONT_COLOR,
                activebackground=BG_COLOR, highlightthickness=0, bd=0)

  game_title.place(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//3, anchor='center')
  play_button.place(x=SCREEN_WIDTH//2, y=1.5*SCREEN_HEIGHT//3, anchor="center")
  settings_button.place(x=SCREEN_WIDTH//2, y=1.5*SCREEN_HEIGHT//3+FONT_SIZE*2, anchor="center")
  help_button.place(x=SCREEN_WIDTH//2, y=1.5*SCREEN_HEIGHT//3+FONT_SIZE*4, anchor="center")
  quit_button.place(x=SCREEN_WIDTH//2, y=1.5*SCREEN_HEIGHT//3+FONT_SIZE*6, anchor="center")
  screen.pack()

  screen.mainloop()
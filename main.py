from turtle import Screen,Turtle
from sudo_solver import Solver
import turtle 
import math

# ------------------------ waiting screen ---------------- #
john = Turtle()
john.penup()
john.hideturtle()
john.goto(-50,215)
john.write("Getting Sudoku grid ready...",align="left",font= ("Arial",15,"normal"))

screen = Screen()
screen.setup(width=500 , height= 500)
screen.bgpic(picname="Waiting.gif")
screen.bgcolor("Gray")

# -------------------- solved ---------------------------#
solved = Solver()
correct_rows = solved.rows

# --------------------- numbers given -------------------- #
screen.clearscreen()
screen.bgcolor("Gray")
with open("Example.txt","r") as file:
  content = file.readlines()
  rows = [[int(num) for num in item.split()] for item in content]

# Width = 51*9
StartWidth = -230
EndWidth = 229

# Height = 51*9
StartHeight = 230
EndHeight = -229

# -------------------- dictionaries ----------------- #
# if a square is clicked for example the first empty square it will use 1 as the key for all the dictionaries below
rows_indexes = {}
columns_indexes = {}
block_indexes = {}
x_cords = {}
y_cords = {}
turtles = []  # a turtle for each open square on the card
tim = Turtle()

# ---------------- white square -------------- #
def white_square():
  tim.penup()
  tim.hideturtle()
  tim.goto(-230,230)
  tim.color("white","white")
  tim.begin_fill()
  tim.speed("fastest")
  for i in range(4):
    tim.forward(51*9)
    new_h = tim.heading() -90
    tim.setheading(new_h)
  tim.end_fill()

# ------------------ horizontal lines ----------------- #
def horizontal_lines():
  x_line = 0
  for i in range(StartWidth,EndWidth+1,51):
    if x_line%3 == 0:
      tim.pensize(width=3)
    else:
      tim.pensize(width=1)
    tim.goto(i,230)
    tim.pendown()
    tim.pencolor("black")
    tim.setheading(270)
    tim.forward(51*9)
    tim.penup()
    x_line += 1

# ------------------ vertical lines ------------------- #
def vertical_lines():
  tim.pensize(width=1)
  y_line = 0
  for j in range(StartHeight,EndHeight-1,-51):
    if y_line%3 == 0:
      tim.pensize(width=3)
    else:
      tim.pensize(width=1)
    tim.goto(-230,j)
    tim.pendown()
    tim.pencolor("black")
    tim.setheading(0)
    tim.forward(51*9)
    tim.penup()
    y_line+=1

# --------------------- card display ----------------- #
def card_setup():
  square_index = 1
  row_list_index = 0
  block_key = 0
  for j in range(StartHeight-1,EndHeight-1,-51):
    row_index = 0
    for i in range(StartWidth+1,EndWidth+1,51):
      add_block = 0
      if 2>=row_list_index>=0:
        add_block = 0
      elif 5>=row_list_index>=3:
        add_block = 2
      elif 8>=row_list_index>=6:
        add_block = 4
      
      block_key = math.floor(row_index/3)+math.floor(row_list_index/3) + add_block
      
      jim = Turtle()
      jim.hideturtle()
      jim.penup()
      if rows[row_list_index][row_index] != 0:      # if the index in rows is not 0 it goes to the position of the number and displays it on the card
        jim.speed("fastest")
        jim.goto(i+26,j-50)
        jim.write(f"{rows[row_list_index][row_index]}",align="center",font=("Arial",30,"normal"))
      else:
        tur_square = Turtle()
        tur_square.hideturtle()
        turtles.append(tur_square)          # appends a turtle for every open square
        x_cords[square_index] = [i,i+50]
        y_cords[square_index] = [j,j-50]
        rows_indexes[square_index] = [row_list_index, row_index]
        columns_indexes[square_index] = [row_index, row_list_index]
        block_indexes[square_index] = [block_key,row_list_index%3,row_index%3]    
        square_index += 1
      row_index += 1
    
    row_list_index += 1

# ----------------------- mouse cords --------------------- #
def get_mouse_coor(x,y):
  global turtles, screen
  screen.update()
  for item in x_cords:
    x_cords_list = x_cords[item]
    y_cords_list = y_cords[item]
    if x_cords_list[0]< x <x_cords_list[1] and y_cords_list[0]> y >y_cords_list[1]:
      jerry = turtles[item-1]
      jerry.hideturtle()
      jerry.penup()
      jerry.goto(x_cords_list[0]+26,y_cords_list[0]-50)
      # usercolour = screen.textinput(title="Colour",prompt="Choose a colour:")
      jerry.clear()
      usernumber = screen.textinput(title= "Number",prompt="Choose a number from 1 to 9:")
      jerry.pencolor(f"black")
      try:            # to ensure that the user inputs a valid number and if nothin is typed in it won't give an error message
        if usernumber != None and 9 >= int(usernumber) >= 0:
          user_rows_indexes = rows_indexes[item] 
          if correct_rows[user_rows_indexes[0]][user_rows_indexes[1]] == int(usernumber):
            jerry.pencolor("spring green")
          else:
            jerry.pencolor("tomato")
          jerry.write(f"{usernumber}",align="center",font=("Arial",30,"normal"))
          rows[user_rows_indexes[0]][user_rows_indexes[1]] = int(usernumber)
        else:
          break
      except:
        pass
  if rows == correct_rows:
    screen.clearscreen()
    Cena = Turtle()
    Cena.hideturtle()
    Cena.penup()
    Cena.goto(0,-20)
    Cena.write("You have completed\n     Soduko grid!", align="center",font=("MS Serif",30,"italic"))
    screen.bgpic("Winner.gif")

screen.tracer(0)
white_square()
horizontal_lines()
vertical_lines()
card_setup()
turtle.onscreenclick(get_mouse_coor)

turtle.mainloop()
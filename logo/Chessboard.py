from tealight.logo import move, turn, color

def square(side):
  for i in range(0, 4):
    move(side)
    turn(90)
   

def chessboard():
  for i2 in range(0,64):
    
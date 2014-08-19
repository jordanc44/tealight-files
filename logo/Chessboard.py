from tealight.logo import move, turn, color

def square(side):
  
  for i in range(0, 4):
    move(side)
    turn(90)
    
for k in range(0, 8):
  move(50)
  for n in range(0, 8):
   square(50)
   move(50)
from tealight.logo import move, turn, color

def square(side):
  for i in range(0, 4):
    move(side)
    turn(90)
  def spiral(size):
  
  if size > 300:
    return
  
  move(size)
  turn(90)
  spiral(size + 5)
  
  spiral(0)
    
    
square(50)
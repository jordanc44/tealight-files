from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
def go():
  while touch()=="fruit":
   move()
    
  if touch()!="fruit":
    turn (1)
    go()
  
  if left_side() and right_side() and touch() !="fruit":
    move()
  
    
   
go()

  
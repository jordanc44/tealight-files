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
    
   
  
  
  if right_side()=="fruit":
    turn(1)
    go()
    
    
go()

  
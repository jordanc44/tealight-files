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
    elif left_side()=="fruit":
      turn(3)
      move()
   
  
  
  if right_side()=="fruit":
    turn(1)
    go()
    
  if left_side()=="fruit":
    turn(3)
    go()
    
  if left_side()!="fruit" and right_side!="fruit":
    move()
    go()
    
    
go()

  
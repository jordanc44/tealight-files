from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def go():
  while touch()=="fruit":
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
    
  if touch()=="wall"
    turn(1)
      
    
    
go()

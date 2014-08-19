from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,250):
  move(i)
  turn(6)
  color(colors[i%3])
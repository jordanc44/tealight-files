from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,250):
  move(i)
  turn(76)
  color(colors[i%3])
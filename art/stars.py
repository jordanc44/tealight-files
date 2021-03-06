from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, x_rad, y_rad, spines):
  
  color(c)
  
  angle = 30
  
  for i in range(0, spines):
    x0 = x + (x_rad * cos(angle))
    y0 = y + (y_rad * sin(angle))
    x1 = x + (x_rad * cos(angle + (2* pi / spines))) 
    y1 = y + (y_rad * sin(angle + (2* pi / spines))) 
    
    
    line(x1, y1, x0, y0)
    
    angle = angle + (2* pi / spines)

star(300, 300, "blue", 100, 200, 40)
star(600, 400, "purple", 200, 200, 15)
star(450, 200, "orange", 125, 200, 30)
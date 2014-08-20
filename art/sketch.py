from tealight.art import (color, line, spot, circle, box, image, text, background)

lastx = 1
lasty = 10

color("purple")

def handle_mousedown(x,y):
  global lastx, lasty
  
  lastx = x
  lasty = y

def handle_mousemove(x,y,button):
  global lastx, lasty
  
  if button == "left":
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
 
  
def handle_mousedown(button):
  if button =="left":
    color("green")
    
  
from tealight.art import (color, line, spot, circle, box, image, text, background)

background ("yellow")

def handle_mousedown(x,y):
  color("blue")
  spot(x,y,20)
  
def handle_mousemove(x,y,button):
  if button == "left":
    color("red")
    circle(x,y,10)
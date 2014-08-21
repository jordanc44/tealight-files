from tealight.art import (color, line, spot, circle, box, image, text, background)


from random import shuffle

p = range(200)
q = range(400)
shuffle (p)
shuffle (q)

Cards=[i for i in range(8)]+[i for i in range(8)]

x = 100
y = 300

image(x,y, "animals/Ant.png")


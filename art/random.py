from tealight.art import (color, line, spot, circle, box, image, text, background)


from random import shuffle

p = range(10)
q = range(400)
shuffle (p)
shuffle (q)

Cards=[i for i in range(8)]+[i for i in range(8)]

x = shuffle(p)
y = shuffle(q)

image(x,y, "animals/Ant.png")


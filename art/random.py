from tealight.art import (color, line, spot, circle, box, image, text, background)


from random import shuffle

x = range(24) + range(24)

shuffle(x)

print x




i = random.randrange(100, 200)
j = random.randrange(100, 200) 

image(i, j, "animals/Ant.png")
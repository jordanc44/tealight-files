from tealight.art import (color, line, spot, circle, box, image, text, background)

import random
from random import shuffle

x = range(24) + range(24)

shuffle(x)

print x




i = random.randrange(500)
j = random.randrange(500) 

image(i, j, "animals/Ant.png")
image(j, i, "animals/Horse.png")
image(i, 200, "animals/Fish1.png")
image(i, j, "animals/Lion.png")
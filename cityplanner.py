
# we need to generate this <a-box position="-1 0.5 -3" width="4" height="4" depth="3" color="#4CC3D9"></a-box>
#                                           x   z   y         a            b        c
#                          <a-box position="-16 -44 8" width="10" hight="16" depth="6" color="#4CC3D9"></a-box>
# z = b/2
# 

import math
import random

for i in range(1000):
    x = random.randint(-200, 200)    
    y = random.randint(-200, 200) 
    a = random.randint(0, 10) 
    b = random.randint(0, 100) 
    c = random.randint(0, 10) 
    z = math.floor(b/2)

    colour = random.randint(0,16777216)
    colour = str(hex(colour).lstrip("0x"))

    # print(str(x) + " " + str(y) + " " + str(z) + " " + str(a) + " " + str(b) + " " + str(c))
    building = ""
    building+= "<a-box position=\""
    building+= str(x) + " "
    building+= str(z) + " "
    building+= str(y) + "\" "
    building+= "width=\"" + str(a) + "\" "
    building+= "height=\"" + str(b) + "\" "
    building+= "depth=\"" + str(c) + "\" "
    building+= "color=\"#"+ colour.upper() +"\"></a-box>"

    print(building)
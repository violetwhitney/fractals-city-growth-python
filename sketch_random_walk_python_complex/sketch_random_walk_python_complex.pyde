import random

def setup():
    global x, y
    
    size(500,500)
    stroke(0)

    x, y = width/2, height/2
        
def draw():
    global x, y
        
    for i in range(10):
        (dx, dy) = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        x += dx
        y += dy
        
        print (x,y)
        point (x,y)

            
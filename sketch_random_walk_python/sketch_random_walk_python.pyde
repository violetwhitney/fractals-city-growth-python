import random
def setup():
    global x, y
    
    size(500,500)
    stroke(0)

    x = width/2
    y = height/2
        
def draw():
    global x, y
        
    for i in range(1):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step =='N':
            y=y+1
        elif step == 'S':
            y=y-1
        elif step == 'E':
            x=x+1
        else:
            x=x-1
        
        print (x,y)
        point (x,y)

            
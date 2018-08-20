size(500, 500)
noFill()

ellipseMode(RADIUS)

def circleDraw(x,y,radius):
    
    #x,y,width,height
    ellipse(x, y, radius, radius)
    
    # line(x1, y1, x2 , y2)
    line(x+radius, y, x + lineLength,y)
    line(x-radius, y, x - lineLength,y)
    line(x, y + radius, x,y + lineLength)
    line(x, y - radius, x,y - lineLength)
        
radius = 50
lineLength = radius*2
x = 250
y = 250

while radius < 260:
   radius += 40
   circleDraw(x, y, radius)
   print radius





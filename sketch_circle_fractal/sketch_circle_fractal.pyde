def setup():
    size(1000, 1000)
    background(0)
    stroke(255,0,0)
    
    def circleDraw(x,y,radius):
        stroke(255,0,0)
        fill(0)
        ellipse(x, y, radius, radius)
        if radius > 2:
            circleDraw(x + radius/2, y, radius/2)
            circleDraw(x - radius/2, y, radius/2)
            circleDraw(x, y + radius/2, radius/2)
            # circleDraw(x, y - radius/2, radius/2)
    
    circleDraw(400,400,1000)

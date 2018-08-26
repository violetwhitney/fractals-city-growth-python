def setup():
    size(500, 500)
    fill(0)#this is black
    
    global road, blocksPerNeighborhood, blocksPerRow, blockLength, houseSetbacks, houseSize, houseQuantity
    
    road = 25 
    blocksPerNeighborhood = 9
    blocksPerRow = int(sqrt(blocksPerNeighborhood))
    blockLength = int((width/blocksPerRow)-road)

    houseSetbacks = 9
    houseQuantity = 5
    houseSize = (blockLength/houseQuantity) - houseSetbacks
    
def draw():
    background(255)

    
    #make blocks

    for b in range(blocksPerNeighborhood):
        fill(0, 150, 50)
        stroke(50, 50, 50)
        strokeWeight(3)
        col = b % blocksPerRow
        row = b / blocksPerRow
        xCol = col*(blockLength+road)
        yCol = row*(blockLength+road)
        rect(xCol,yCol,blockLength,blockLength)
        
        #make houses
        fill(0)
        noStroke()
        h = -1
        
        while h < houseQuantity-1:
            h += 1
            rect(xCol+houseSetbacks+0,yCol + (h*(houseSize+houseSetbacks)),houseSize,houseSize)
            print(houseSize)
    
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closestX,colosestY=0,0
        distance=0
        if xCenter<x1:
            closestX=x1
        elif xCenter>x2:
            closestX=x2
        else:
            closestX=xCenter 
        if yCenter<y1:
            closestY=y1
        elif yCenter>y2:
            closestY=y2
        else:
            closestY=yCenter 
        
        distance=((closestX - xCenter)**2 +(closestY - yCenter)**2)**0.5
        if distance**2<=radius**2:
            return True
        else:
            return False
        



        
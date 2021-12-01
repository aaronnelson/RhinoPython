#Random Point Walker
#Prompt user for a start point and number of random points along with a step value
#Starting from the user point create points in random directions using the step interval

import rhinoscriptsyntax as rs
import random

#prompt user for number of total points in walker
numPts = rs.GetInteger("Enter Total Number of Points")

#prompt user for interval between points
stepPts = rs.GetInteger("Enter Steps between Points")

#ask the user to create a starting point
userPt = rs.GetPoint("Please create a point")
pt = rs.AddPoint(userPt)

#create a list a points and append starting pt to the list
pts = []
pts.append(pt)

#walk through the range of points
for  i in range(numPts):
    #create random values for X, Y, and Z.  These can be + or - as long as they fall in our interval range
    xDir = random.uniform(-stepPts, stepPts)
    yDir = random.uniform(-stepPts, stepPts)
    zDir = random.uniform(-stepPts, stepPts)
    #assemble the vector from the constituent components
    vect = (xDir, yDir, zDir)
    
    #create a new point that copys the previous point and moves it along the translation vector 
    newPt = rs.CopyObject(pts[-1], vect)
    #add the point to the list of points
    pts.append(newPt)

#create a curve using the point list
myCurve = rs.AddCurve(pts, 3)

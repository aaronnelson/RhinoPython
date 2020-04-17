#This script creates a point grid and prompts the user to reference a curve.
#the curve is copied from its center points to the new center points as defined by the grid.
#A vector derived from the grid points to the attractor point describes the translation
#for another copy of the curve at a height hard coded into the loop
#the new curve pairs are lofted to create a surface.

import rhinoscriptsyntax as rs

#create an x and y range for the loops
xRange= rs.GetInteger("Please select number of Curves in X", 10)
yRange= rs.GetInteger("Please select number of Curves in Y", 10)

#prompt user for grid spacing
spacing = rs.GetInteger("Please enter spacing", 5)

#ask the user for a curve to reference
myCrv = rs.GetObject("Please select reference curve", 4)

#get the center of the referenced curve
myCtr = rs.CurveAreaCentroid(myCrv)

#ask the user for an attractor point
attrPt = rs.GetObject("Please select attractor", 1)

#loop through the x and y ranges
for x in range(xRange):
    for y in range(yRange):
        
        #decribe a new point based on our position in the x and y loops, this will be the center point
        ctrPt = [x * spacing, y * spacing , 0]
        
        #create a vector between the center of the reference curve and my position in the x, y grid
        crvVect = rs.VectorCreate(ctrPt, myCtr[0])
        #and then copy the reference curve to the new location along the vector
        newCrv = rs.CopyObject(myCrv, crvVect)
        
        #create a new vector from the center point to the attractor
        vect1 = rs.VectorCreate(attrPt, ctrPt)
        #and unitize and multiply by 5
        vect1 = rs.VectorUnitize(vect1) * 5
        
        #create a copy of the curve at the end of the new vector
        movedCrv = rs.CopyObject(newCrv, vect1)
        
        #and create a new lofted surface between the two grid curves
        srf = rs.AddLoftSrf([newCrv, movedCrv])
        
    
    
#This script creates a point grid and prompts the user to reference a planar curve.
#the curve is copied from its center point to the new center points as defined by the grid.
#This will be in an XY plane at the Z height of the input curve's center Z
#A vector derived from the grid points to the attractor point describes the translation
#for another copy of the curve at a specified Z height
#the new curve pairs are lofted and capped to create a polysurface.

import rhinoscriptsyntax as rs

#ask the user for a curve to reference
myCrv = rs.GetObject("Please select reference curve", 4)
#make sure we have a planar curve
while rs.IsCurvePlanar(myCrv) == False:
    rs.MessageBox("Curve must be planar")
    myCrv = rs.GetObject("Please select reference curve", 4)

#get the bounding box and check the max length of the box sides, we use this to set default spacing
bBox = rs.BoundingBox(myCrv)
#bounding boxes are rectangular so we only need to compare one set of adjacent sides
spacing = max(rs.Distance(bBox[0], bBox[1]), rs.Distance(bBox[1], bBox[2]))

#get the center of the referenced curve
myCtr = rs.CurveAreaCentroid(myCrv)

#Command Line prompt the user for an x and y range for the loops
xRange= rs.GetInteger("Please select number of Curves in X", 10)
yRange= rs.GetInteger("Please select number of Curves in Y", 10)

#prompt user to overide grid spacing
spacing = rs.GetReal("Please enter spacing", spacing)

#ask the user for an attractor point
attrPt = rs.GetPoint("Please select attractor", (0, 0, 20))

#validate and check if attractor lies in same plane as the curve
#attractor should be above or below the plane of the curve
while attrPt == None or attrPt[2] == myCtr[0][2]:
    rs.MessageBox("Attractor must be above or below the plane of the curve")
    attrPt = rs.GetPoint("Please select an attractor point", (0, 0, 20))

#prompt user for height for loft
height = rs.GetInteger("Enter height of lofted shapes", 5)

#loop through the x and y ranges
for x in range(xRange):
    for y in range(yRange):
        
        #decribe a new point based on our position in the x and y loops, this will be the center point
        ctrPt = [x * spacing, y * spacing , myCtr[0][2]]
        
        #create a vector between the center of the reference curve and my position in the x, y grid
        crvVect = rs.VectorCreate(ctrPt, myCtr[0])
        
        #and then copy the reference curve to the new location along the vector
        newCrv = rs.CopyObject(myCrv, crvVect)
        
        #create a new vector from the center point to the attractor
        vect1 = rs.VectorCreate(attrPt, ctrPt)
        
        #unitize and multiply by height
        vect1 = rs.VectorUnitize(vect1) * height
        
        #create a copy of the curve at the end of the new vector
        movedCrv = rs.CopyObject(newCrv, vect1)
        
        #and create a new lofted surface between the two grid curves can cap
        srf = rs.AddLoftSrf([newCrv, movedCrv])
        rs.CapPlanarHoles(srf)
    
    

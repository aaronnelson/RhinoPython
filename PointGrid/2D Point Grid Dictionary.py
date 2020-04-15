#2D Point Matrix with Attractor

import rhinoscriptsyntax as rs

#set spacing between points, this could also be a .GetInteger
spacing = 3

#dictionary for points
pts = {}
#list for lines (these are really curves)
lines = []

#prompt user for input
iMax = rs.GetInteger("Please enter max number of points in x", 20)
jMax = rs.GetInteger("Please enter max number of points in y", 20)

#select attractor pt, must exist in Rhino document
attPt = rs.GetObject("Select attractor point", 1)

#loop through x and y ranges, use i and j as iterators to use as the dictionary keys
for i in range(iMax):
    for j in range(jMax):
        
        #define x,y,(z)
        x = i * spacing
        y = j * spacing
        z = 0
        
        #store all the point x,y,z locations in the dictionary with i,j keys
        pts[(i, j)] = [x, y, z]
        #pt = rs.AddPoint(pts[(i, j)])
        #rs.AddTextDot((i,j), pt)
        #rs.AddLine(pts[(0,0)], pts[(2,3)])

#loop throught all the points
for i in range(1, iMax):
    for j in range(1, jMax):
        
        #L - Shapes
        #lines.append(rs.AddCurve([pts[(i-1, j)], pts[(i, j)], pts[(i, j-1)]], 1))
        
        #closed curves (boxes)
        lines.append(rs.AddPolyline([pts[(i, j)], pts[(i-1, j)], pts[(i-1, j-1)], pts[(i, j-1)], pts[(i, j)]]))

#looping through the list of curves
for i in range(len(lines)):
    
    #find the distance from the center of the curve to the attractor point
    stPt = rs.CurveMidPoint(lines[i])
    dist = rs.Distance(attPt, stPt)
    
    #rotate box based on distance from the attractor
    lines[i] = rs.RotateObject(lines[i], stPt, dist)







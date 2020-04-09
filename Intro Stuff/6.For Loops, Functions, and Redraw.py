#For Loops, Functions, and Redraw

#import RhinoScript and refer as 'rs'
import rhinoscriptsyntax as rs

#define a Python function with 4 parameters
def createColoredPoint(x, y, z, color):
    
	#add a point to the Rhino document at X, Y, and Z
    pt = rs.AddPoint(x, y, z)
	#Color the point we just added
    rs.ObjectColor(pt, color)

#EnableRedraw disables updating the document
rs.EnableRedraw(False)

#variable to control the spacing of the points
step = 10

#Nested For loop iterating through X, Y, and Z ranges
for x in range(0, 256, step):
    for y in range(0, 256, step):
       for z in range(0, 256, step):
		   #call our function and add a point at X, Y, and Z, with a color based of position (colors are tuples)
           createColoredPoint(x, y, z, (x, y, z))

#Redraw updates the document		   
rs.Redraw()
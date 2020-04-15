#2D Point Grid with Circles generated with an Attractor Point
#This script will create a 2D grid of points and circle centered on each point.
#Circle radius is driven by the distance from the attractor to the point defining the center of the circle.

import rhinoscriptsyntax as rs

#spacing variable sets distance between points
spacing = 3

#Dictionary to hold points
pts = {}

#Prompt user to set X and Y extents, default of 20
iMax = rs.GetInteger("Please enter max number of points in x", 20)
jMax = rs.GetInteger("Please enter max number of points in y", 20)

#select an attractor pt.  This will drive the size of the circles
attPt = rs.GetObject("Select attractor point", 1)

#nested For loops for X and Y Domains
for i in range(iMax):
    for j in range(jMax):
        
        #define x,y,(z)
        x = i * spacing
        y = j * spacing
		#z will always be 0 for a 2D Grid
        z = 0
        
		#Store the points in the dictionary using the iterators as the reference keys
        pts[(i, j)] = [x, y, z]


#Loop through all of the sorted points in the Dictionary
for key, pt in sorted(pts.iteritems()):
	
	#print out the key and value for debugging
    #print key, value
    
	#calculate the straight line distace between the attractor point and the current point in the loop
    dist = rs.Distance(pt, attPt)
	
	#print out the distance for debugging
    #print dist
    
	#Create a radius value based on the scaled distance
    radius = dist/20
    
	#If our circle gets too large or small, constrain it to a value between half the spacing and 0.4 units
    if radius > spacing/2:
        radius = spacing/2
    elif radius < 0.4:
        radius = 0.4
    
	#Add the circle to the Rhino document using the calculated radius
    rs.AddCircle(pt, radius)







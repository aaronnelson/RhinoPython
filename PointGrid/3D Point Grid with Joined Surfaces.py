#Warping a point grid with and attractor point
#Creates a grid based on the created point's distance from a defined attractor point

import rhinoscriptsyntax as rs

#define base spacing beween points
spacing = 10

#dictionary for points
pts = {}

#prompt user for input
iMax = rs.GetInteger("Please enter max number of points in x", 5)
jMax = rs.GetInteger("Please enter max number of points in y", 5)
kMax = rs.GetInteger("Please enter max number of points in z", 5)

#select attractor pt
point = rs.GetObject("Select attractor point", 1)

#loop through three ranges for x, y ,and z
for i in range(iMax):
    for j in range(jMax):
        for k in range(kMax):
            
            x = i * spacing
            y = j * spacing
            z = k * spacing
            
			#get distance from current position in the loop and check distance to the attractor
            dist = rs.Distance((x,y,z), point)
			
			#scale the x, y, and z locations based on distance divided by a scalar
            x *= (dist/20)
            y *= (dist/20)
            z *= (dist/20)
            
			#store the points in the dictionary with keys i, j , and k
            pts[(i, j, k)] = [x, y, z]
			#add a Point3D object to the document
            pt = rs.AddPoint(pts[(i, j, k)])
            #rs.AddTextDot((i, j, k), pt)
            
#loop through our points			
for i in range(1, iMax):
    for j in range(1, jMax):
        for k in range(1, kMax):
            
			#create list for the surfaces we will create
            srfs = []
            
            #add Surface from points (select points in counter clockwise direction) and store in srfs list
            srfs.append(rs.AddSrfPt([pts[(i, j, k)], pts[(i-1, j, k)], pts[(i-1, j-1, k-1,)], pts[(i, j-1, k)]]))
            
            srfs.append(rs.AddSrfPt([pts[(i, j, k)], pts[(i, j-1, k)], pts[(i, j-1, k-1)]]))
            
            srfs.append(rs.AddSrfPt([pts[(i-1, j, k)], pts[(i, j, k)], pts[(i-1, j, k-1)]]))
            
			#join all of the surfaces in the list
            rs.JoinSurfaces(srfs, True)
            
#                #reversed normals(clockwise point selection)
#                rs.AddSrfPt([pts[(i, j, k)], pts[(i, j-1, k)], pts[(i-1, j-1, k-1,)], pts[(i-1, j, k)]])







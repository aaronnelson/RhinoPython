import rhinoscriptsyntax as rs

#set spacing between points to 10 units
spacing = 10

#define the PointMatrix function
def PointMatrix():
    
	#dictionary for point locations
    pts = {}
	#list for any curves created
    lines = []
    
	#prompt user for input
    iMax = rs.GetInteger("Please enter max number of points in x", 5)
    jMax = rs.GetInteger("Please enter max number of points in y", 5)
    kMax = rs.GetInteger("Please enter max number of points in z", 5)
    
	#three nested for loops give us values for x, y, and z
    for i in range(iMax):
        for j in range(jMax):
            for k in range(kMax):
                
                x = i
                y = j
                z = k
                
                #define x, y, z
                x = i * spacing
                y = j * spacing
                z = k * spacing                
                
				#add the point components to the dictionary using, i, j, and k as keys
                pts[(i, j, k)] = [x, y, z]
				#add a 3D point object to the document
                pt = rs.AddPoint(pts[(i, j, k)])
    
	#loop through the points
    for i in range(1, iMax):
       for j in range(1, jMax):
            for k in range(1, kMax):
                #add Surface from points (select points in clockwise direction for normals facing +Z)
                rs.AddSrfPt([pts[(i, j, k)], pts[(i-1, j, k)], pts[(i-1, j-1, k-1,)], pts[(i, j-1, k)]])


#call the function we just wrote
PointMatrix()


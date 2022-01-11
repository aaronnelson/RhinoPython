import rhinoscriptsyntax as rs
#from the RhinoPythonPrimer Rev 3
#I cleaned it up a bit an rearranged things

#calculates length of path as a polyline from a list of points
def polylineLength(vertices):
    length = 0.0
    for i in range(0, len(vertices) - 1):
        length = length + rs.Distance(vertices[i], vertices[i + 1])
    return length

#input vertices are averaged to subdivide the polyline
def subdivPolyline(vertices):
    #where we store our new points
    verticesSubD = []
    
    #loop through all the vertices except for the last one
    for i in range(0, len(vertices) - 1):
        #store the current vertex in the new list
        verticesSubD.append(vertices[i])
        #new point is average of vertex with the next vertex in the old list
        pt = (vertices[i] + vertices[i+1]) * 0.5
        #store it in the new list
        verticesSubD.append(pt)
    #we skip the last vertex in the loop so add it here
    verticesSubD.append(vertices[len(vertices) - 1])
    return verticesSubD

#creates a path on a surface between two UV points (R2 space)
def getr2PathOnSurface(surface, segments, prompt1, prompt2):
    startPt = rs.GetPointOnSurface(surface, prompt1)
    if not startPt:
        return
    
    endPt = rs.GetPointOnSurface(surface, prompt2)
    if not endPt:
        return
    
    #if our start and end points are coincedents, why bother?
    if rs.Distance(startPt, endPt) == 0.0:
        return
    
    #GetPointOnSurface returns a Point3D, to get the UV coords, we need to SCP to the Point3D
    uva = rs.SurfaceClosestPoint(surface, startPt)
    uvb = rs.SurfaceClosestPoint(surface, endPt)
    
    #store our new vertices for the path in a list
    path = []
    
    #the shortest path between two points is a straight line, but in our case this 
    #needs to follow the contours of the surface.  We divide the straight path into
    #segments and check each vertex of the segments and find the closest corrisponding point
    #on the surface itself
    #range is non inclusive in python, I had to add 1 here to get the last point to align
    #with the last point selected
    for i in range(segments + 1):
        
        #we will decompose the UV r2 space into U and V r1 spaces and find where we
        #are using a single parameter at each segment vertex
        t = i / segments
        
        # U and V parameters are calculated by taking the individual U and V domains
        # and multiplying them by the t value.  The t paramter is added to the start of
        #both domains. SCP will return a list of values [0] is the U and [1] is the V
        u = uva[0] + t * (uvb[0] - uva[0])
        v = uva[1] + t * (uvb[1] - uva[1])
        
        #get that closes point on the surface and add it to the path list of vertices
        pt = rs.EvaluateSurface(surface, u, v)
        path.append(pt)
    return path

#projects the vertices of a polyline onto a surface
def projectPolyline(vertices, surface):
    #new list for new polyline vertices
    polyline = []
    
    #step through list and get the closest on the BREP (will work for trimmed srf)
    for vertex in vertices:
        pt = rs.BrepClosestPoint(surface, vertex)
        #if we have a closest point, append to the new list, if not just move on
        if pt:
            polyline.append(pt[0])
    return polyline

#takes in the vertices of a polyline and averages three points to created a
#"smoothed" version of the polyline
def smoothPolyline(vertices):
    
    #store the new smoothed set of vertices in a list
    smooth = []
    
    #we will store the start and endpoints as is, they were selected by the user
    #and should be coincident with the surface to begin with.
    smooth.append(vertices[0])
    
    #loop throught all the vertices, skiping the first and last, getting the
    #neighbors for each vertex and averaging them to smooth the polyline
    for i in range(1, len(vertices) - 1):
        prev = vertices[i - 1]
        this = vertices[i]
        next = vertices[i + 1]
        pt = (prev + this + next) / 3.0
        #add this new point to the smoothed list
        smooth.append(pt)
    #have to get the last point in the original list.  I think there is a
    #misprint in the Primer and I had to make sure we were not getting an
    #out of bounds index error on the list
    smooth.append(vertices[len(vertices) - 1])
    return smooth

#function that does the fitting using the combo of functions above
def geodesicFit(vertices, surface, tolerence):
    
    #start by getting the length of the current set of vertices
    length = polylineLength(vertices)
    
    #do this recursively
    while True:
        #smooth the line then project it toward the surface
        vertices = smoothPolyline(vertices)             
        vertices = projectPolyline(vertices, surface)
        
        #get the length of the new line
        newLength = polylineLength(vertices)
        #check to see if the new line is shorter, once our line is not getting any
        #appreciably shorter (within the tolerence), give us the new vertices
        if abs(newLength - length) < tolerence:
            return vertices
        else:
            length = newLength

#main subroutine that puts it all together
def geodesicCurve():
    #get a surface
    surface = rs.GetObject("Select Surface to Fit Curve", 8, True, True)
    if not surface:
        return
    
    maxLines = rs.GetReal("Enter Maximum Number of Segments", 500, 10, 1000)
    
    #get the vertices for the shortest r2 path with 10 sample points
    vertices = getr2PathOnSurface(surface, 10, "Start Point for Curve", "End Point for Curve")
    if not vertices:
        return
    
    #set the tolerence for 1/10 of the tolerence of the model space
    tolerence = rs.UnitAbsoluteTolerance() * 0.1
    #set a big and small starting value for our length tests
    length = 1e300
    newLength = 0.0
    
    #do this recursivly
    while True:
        print("Solving for %d samples" % len(vertices))
        #run the vertices into the fitting subroutine
        vertices = geodesicFit(vertices, surface, tolerence)
        
        #check our length here, if we are with acceptable tolerence we should go
        newLength = polylineLength(vertices)
        if abs(newLength - length) < tolerence:
            break
        #if for some reason we still haven't found a solution and have over 1000
        #vertices we should also go
        if len(vertices) > maxLines + 1:
            break
        
        #subdivide the polyline to double the number of samples and get ready to
        #start the fitting again
        vertices = subdivPolyline(vertices)
        length = newLength
    
    #once we are fit within tolerence, add the line to the document and prompt user
    rs.AddPolyline(vertices)
    print("added line")

#run the damn thing
def main():
    geodesicCurve()
    
    
if __name__ == "__main__":
    main()
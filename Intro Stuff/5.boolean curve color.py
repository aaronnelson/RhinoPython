#Create alternating sine curves with alternating colors

#import both RS and math libraries
import rhinoscriptsyntax as rs
import math

#Boolean switch
flip = True

#Create two colors, colors are tuples (R, G, B)
color01 = (0, 255, 255)
color02 = (255, 0, 255)

#For loops with frange(start, stop, step)
for x in rs.frange(0.0, 10.0, 0.1):

    #create the list here, we create a new list once we exhaust Y coords. to create individual sets of points in the Y Direction
    ptsForCurve = []
    for y in rs.frange(0.0, 10.0, 0.1):
	#Z coords based on product of sines
        z = math.sin(x) * math.sin(y)
        
	#store each point as a tuple with X, Y, and Z and append to the point list
        pt = (x, y, z)
        ptsForCurve.append(pt)
    #once we have all the points, create a curve using those points and add it to the Rhino Document
    curve = rs.AddCurve(ptsForCurve)
	
    #Alternating colors using boolean switch
    if flip:
        rs.ObjectColor(curve, color01)
        flip = not flip
    else:
        rs.ObjectColor(curve, color02)
        flip =  not flip

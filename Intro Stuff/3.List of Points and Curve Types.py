# Lists of Points and Curve Types

#import the Rhinoscript Library and set the reference to 'rs'
import rhinoscriptsyntax as rs

#create and empty list to store points
ptList = []

#prompt user to select points
ptList = rs.GetPoints(True, True, "Please select start point", "Select next point, Enter When finished")

#print contents of list
print(ptList)

#Create some Curves of different types from our Point List
myPolyLine = rs.AddPolyline(ptList)
myCurve = rs.AddCurve(ptList)
myIntpCurve = rs.AddInterpCurve(ptList)

#output type and GUID
print type(myPolyLine)
print myCurve
print myIntpCurve

#Color Curves
#Colors are tuples
color01 = (255, 0, 0) #red
color02 = (0, 255, 0) #green
color03 = (0, 0, 255) #blue

#Change Color of Curves
rs.ObjectColor(myPolyLine, color01)
rs.ObjectColor(myCurve, color02)
rs.ObjectColor(myIntpCurve, color03)

#Add the points into the Rhino document, points in the point list are just point3D objects
for pt in ptList:
    rs.AddPoint(pt)


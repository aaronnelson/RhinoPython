# Lists of Points and Curve Types

import rhinoscriptsyntax as rs

ptList = []

ptList = rs.GetPoints(True, True, "Please select start point", "Select next point, Enter When finished")


print(ptList)

#Some Curves from our Point List
myPolyLine = rs.AddPolyline(ptList)
myCurve = rs.AddCurve(ptList)
myIntpCurve = rs.AddInterpCurve(ptList)

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

#Add the points
for pt in ptList:
    rs.AddPoint(pt)


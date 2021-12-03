#Finding Curve Parameters---------------------------------------------------------------
#Curve parameters are different than the physical length of the curve
#Find the midpoint of the curve (midpoint of length) and a user defined
#parameter within the curve domain then label with TextDot

import rhinoscriptsyntax as rs

#prompt user for curve to examine
crv = rs.GetObject("Please Select Curve", 4)

#get the curve domain
crvDom = rs.CurveDomain(crv)
rs.MessageBox("The domain of the curve is: " + str(crvDom))

#place the text label at the curve length midpoint using the curvature vector as a guide
vect1 = rs.CurveCurvature(crv, rs.CurveClosestPoint(crv, rs.CurveMidPoint(crv)))[4]
vect1 = rs.VectorUnitize(vect1) * 2

#create the label
dotPt = rs.CopyObject(rs.CurveMidPoint(crv), vect1)
rs.AddTextDot("Midpoint", dotPt)
rs.ObjectColor(rs.AddLine(rs.CurveMidPoint(crv), dotPt), (255, 0, 0))
rs.ObjectColor(rs.AddPoint(rs.CurveMidPoint(crv)), (255, 0, 0))

#Prompt user for curve parameter default at mid (curve domains do not always start at 0)
param = rs.GetReal("Enter Curve Parameter, default is mid", (crvDom[1] - crvDom[0])/2, crvDom[0], crvDom[1])

#evaluate the curve at the middle parameter and place a dot
crvPt = rs.EvaluateCurve(crv, param)
rs.ObjectColor(rs.AddPoint(crvPt), (0, 0, 255))

#place the text label at the curve parameter using the curvature vector as a guide
vect1 = rs.CurveCurvature(crv, param)[4]
#reversing this vector places it at the opposite side of the curve for readbility
vect1 = rs.VectorReverse(rs.VectorUnitize(vect1) * 2)

#draw the label
dotPt = rs.CopyObject(crvPt, vect1)
rs.AddTextDot("Parameter", dotPt)
rs.ObjectColor(rs.AddLine(crvPt, dotPt), (0, 0, 255))


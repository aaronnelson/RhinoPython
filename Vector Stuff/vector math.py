#some vector math stuff with user prompts
#vector add + sub + dot + cross
#command line prompts, message box, listbox

import rhinoscriptsyntax as rs

#create and origin point, the default is 0, 0, 0
origin = rs.GetPoint("Select Origin", (0, 0, 0))
#if we don't get an origin for some reason, make it 0, 0, 0
if origin == None:
    origin = rs.CreatePoint(0, 0, 0)
originPt = rs.AddPoint(origin)

#prompt user for a first point
pt1 = rs.GetPoint("Pick First Point", origin)
rs.AddPoint(pt1)

#create a vector between the origin and the point, represent this with a colored line
vector1 = rs.VectorCreate(pt1, origin)
rs.ObjectColor(rs.AddLine(origin, pt1), (255, 0, 0))

#prompt the user for a second point
pt2 = rs.GetPoint("Pick a second point", origin)
rs.AddPoint(pt2)

#create a vector between the origin and the point, represent this with another colorerd line
vector2 = rs.VectorCreate(pt2, origin)
rs.ObjectColor(rs.AddLine(origin, pt2), (0, 0, 255))

#create some options for Vector operations and prompt user for input with List of options
options = ("Vector Addition", "Vector Subtraction", "Vector Dot Product", "Vector Cross Product")
if options:
    result = rs.ListBox(options, "Pick a Vector Math Operation")
    #output the result with a message box (this prompts the user for an OK)
    if result: rs.MessageBox(result + " was selected")
    
    #prompt user in command line for vector unitization (this is more like standard Rhino commands
    unit = rs.GetString("Unitize Vector?", "Yes", ["Yes", "No"])
    #if we are unitizing, give the user the option of scaling the vector
    if unit == "Yes":
        #by default, out scale values will start at 1 (no scaling)
        scale = rs.GetReal("Scale value for unit vector?", 1)
    
    #Addition of Two Vectors
    if result == "Vector Addition":
        vector3 = rs.VectorAdd(vector1, vector2)
        if unit == "Yes":
            vector3 = rs.VectorUnitize(vector3) * scale
        #copy the origin and move it along the new vector
        newPt = rs.CopyObject(originPt, vector3)
        #visualize the vector with a green line
        rs.ObjectColor(rs.AddLine(origin, newPt), (0, 255, 0))
    
    #Subtraction of Two Vectors
    elif result == "Vector Subtraction":
        vector3 = rs.VectorSubtract(vector1, vector2)
        if unit == "Yes":
            vector3 = rs.VectorUnitize(vector3) * scale
        #copy the origin point and move along new vector
        newPt = rs.CopyObject(originPt, vector3)
        #visualize the vector with a green line
        rs.ObjectColor(rs.AddLine(origin, newPt), (0, 255, 0))
    
    elif result == "Vector Dot Product":
        vector3 = rs.VectorDotProduct(vector1, vector2)
        #dot product is just a scalar value print it to screen for now
        print vector3
    
    elif result == "Vector Cross Product":
        vector3 = rs.VectorCrossProduct(vector1, vector2)
        if unit == "Yes":
            vector3 = rs.VectorUnitize(vector3) * scale
        newPt = rs.CopyObject(originPt, vector3)
        rs.ObjectColor(rs.AddLine(origin, newPt), (0, 255, 0))
        

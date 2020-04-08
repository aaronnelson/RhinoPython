# if elif and else

#import the rhinoscript library and refer as 'rs'
import rhinoscriptsyntax as rs

#Create some colors, colors are tuples (R, G, B)
color01 = (255, 0, 255)  #magenta
color02 = (0, 255, 255)  #teal
color03 = (125, 38, 205) #purple

#Two for loops give us X and Y coordinates, here loop from 0 - 9 (range function is non inclusive)
for x in range(10):
    for y in range(10):
        
		#add points to the Rhino document and color based on their place in the sequence
        pt = rs.AddPoint(x, y, 0)
        if x % 3 == 0 and y % 5 == 0:
            rs.ObjectColor(pt, color01)
        elif x % 3 == 0 or y % 5 == 0:
            rs.ObjectColor(pt, color02)
        else:
            rs.ObjectColor(pt, color03)
    


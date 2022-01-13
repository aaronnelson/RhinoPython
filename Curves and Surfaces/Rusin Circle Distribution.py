import rhinoscriptsyntax as rs
import math

#adapted from RhinoPython Primer V3.  I think the phi and theta names are 
#reversed based on all of the math documentation describing spherical coordinates
#that I read, but I will leave that from someone smarter than me.  I think in Physics
#the tendancy is to reverse these as here?  I dunno.

def DistributeCirclesOnSphere():
    
    #get a bunch of stuff from the user
    center_point = rs.GetPoint("Center of Sphere", (0, 0, 0))
    if not center_point:
        print("Center Point Needed!")
        return
    
    sphere_radius = rs.GetReal("Radius of Sphere", 10.0, 0.01)
    if not sphere_radius:
        print("Sphere Radius Needed!")
        return
    
    circle_radius = rs.GetReal("Radius of Circles", 0.05 * sphere_radius, 0.001, 0.5 * sphere_radius)
    if not circle_radius:
        print("Circle Radius Needed!")
        return
    
    #this gives the number of circles that will fit along the seam. The centers of the seam
    #circles will also be the "bands" of circles around the sphere.  The length of the seam
    #is half of the circumference (1/2C = pi * r).  Divide that space by the diameter of the
    #circles we want to lay along it.  Casting as INT drops the decimal (round down).
    vertical_count = int((math.pi * sphere_radius)/(2 * circle_radius))
    
    rs.EnableRedraw(False)
    
    #phi is the variable that will set the elevation of the bands above and below
    #the equator.  The domain of this space will be -0.5 pi to 0.5 pi.  Each step
    #will be in an increment determined by the number of circles that fit along the seam.
    phi = -0.5 * math.pi
    phi_step = math.pi / vertical_count
    
    #step throught the "bands" around the sphere until we reach the bottom 
    while phi < 0.5 * math.pi:
        
        #the number of circles we can fit in each "band" is the diameter of the sphere at each
        #angle of phi divided by the diameter of a single circle.  Casting as an INT will drop
        #the decimals (round down)
        horizontal_count = int((2 * math.pi * math.cos(phi) * sphere_radius) / (2 * circle_radius))
        #the only case to round UP is if we accidentially rounded down to 0 (we can't have 0 circles)
        if horizontal_count == 0:
            horizontal_count = 1
        #theta is the angle around the center of the circle at the equator.  We intitalize
        #for each "band" and determine the step increment based on the number of circles
        #we can fit in each band
        theta = 0
        theta_step = 2 * math.pi / horizontal_count
        
        #this is where we look through all the positions on each "band"
        #the origianl author of this script subtracts a small value from 2 PI
        #to keep there from being an overlapped circle at the end.  I am not
        #sure that it is needed here, but I am leaving it in as I have not
        #tested the script that much
        while theta < 2 * math.pi - 1e-8:
            
            #convert our spherical coordinates into cartesion that Rhino understands
            #this is 3D Pythagorean Theorum
            circle_center = (sphere_radius * math.cos(theta) * math.cos(phi) + center_point[0], sphere_radius * math.sin(theta)* math.cos(phi) + center_point[1], sphere_radius*math.sin(phi) + center_point[2])
            #subtracting the point coordinates from the origin give us a vector that points 
            #away from the center
            circle_normal = rs.PointSubtract(circle_center, center_point)
            #proxy place to place the circle, we don't care about orientation
            circle_plane = rs.PlaneFromNormal(circle_center, circle_normal)
            rs.AddCircle(circle_plane, circle_radius)
            #increment Theta angle
            theta += theta_step
        #increment Phi angle
        phi += phi_step
    rs.EnableRedraw(True)


def main():
    DistributeCirclesOnSphere()

if __name__ == "__main__":
    main()
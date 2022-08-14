#importing the needed modules
import math
import sys

#Check if the user knows how to use the program
if len(sys.argv) != 4:
    print ("Usage:")
    print ("    ", end = "")
    print("python conegeometry.py <height> <radius> <area_or_volume>")
    quit()

#if everything is plugged in right
else:

    #Variables
    height = float(sys.argv[1])
    radius = float(sys.argv[2])
    area_or_volume = str(sys.argv[3])
    pi = 3.14159

    #Make sure the variable's input is not case sensitive
    Case_Sensitive = area_or_volume.lower()


    #if is found in the "area or volume" input
    if ("area") in sys.argv[3]:
        #calculate area and print result
        area = pi * radius * (radius + math.sqrt((height**2)+(radius**2)))
        print("The surface area of a cone of radius %i" % height, end = " " )
        print("and height %i" % radius, end = " ")
        print("is %f" % area)

    #if volume is found in the "area or volume" input
    elif ("volume") in Case_Sensitive:
        #calculate volume and print result
        volume = pi * (radius**2) * (height/3)
        print("The volume of a cone of radius %i" % height, end = " " )
        print("and height %i" % radius, end = " ")
        print("is %f" % volume)

    else:
        #if anything else is entered in the "area or volume" input
        print ("Usage:")
        print ("    ", end = "")
        print("python conegeometry.py <height> <radius> <area_or_volume>\n")
        print("    area_or_volume:   must be area or  volume")
        quit()





#Questions:
#Do height and radius have to be ints or floats?
#for usage do I have to print the usage in the terminal or can it be as a string?

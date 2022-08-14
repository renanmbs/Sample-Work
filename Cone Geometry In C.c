
//Import Modules
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//Main function
int main(int argc ,char *argv[]){
    
    //Checking if the user knows how to use the program
    if (argc != 4) {
        printf("Usage: \n");
        printf("    ./conegeometry <height> <radius> <area_or_volume>\n");
        return 0;
    }
        
    /*VARIABLES*/
    //Getting input from the user and converts the string to floats
    double height = atof(argv[1]);
    double radius = atof(argv[2]);
   
    
    /*Checks if the user wants the area calculated
    strcmp -> compares if area is equal as the third input,
    if it is, the function returns 0 */
    if (strcmp(argv[3], "area") == 0){
    
        /*CALCULATIONS OF THE AREA
         Area of cone = pi * radius * (radius + sqrt(height^2 + radius^2))*/
        double x = 3.1415926535 * radius;
        double z = (radius * radius) + (height * height);
        double y = radius + sqrt(z);
        double multiplication = x * y;
        
        //Printing results
        printf( "The Surface Area of a Cone of Radius %f and Height %f is %f \n",radius,height,multiplication);
    }
    
    //Checks if the user wants the volume calculated
    else if ((strcmp(argv[3], "volume")) == 0){
        
        /*CALCULATIONS OF THE VOLUME
         Volume of cone = pi * radius^2 * (height/3) */
        double volume = 3.1415926535 * (radius * radius) * (height/3);
        
        //Printing results
        printf( "The Volume of a Cone of Radius %f and Height %f is %f \n",radius,height,volume);
    }
    
    //If neither Area nor Volume is entered
    else{
        printf("Usage:");
        printf("    ./conegeometry <height> <radius> <area_or_volume>\n");
        printf("    area_or_volume:   must be area or volume");
        return 0;
        }

return 0;

}

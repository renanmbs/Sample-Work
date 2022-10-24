#Importing Modules
import numpy as np
import matplotlib.pyplot as plt
import time
import math


#Variables
x = 37.7
z = np.deg2rad(2) #2 degrees to radians
theta = np.arange(0, 18.84956, 0.03490658503988659) #Range to test theta (from 0 to 1080 degrees, step of 90 degrees - transformed into radians)
result = [] #Container to hold the result

#Calculate values for theta
for k in (theta):

    sine = math.sin((k)) #Take sine of theta
    equation = (x * (0.8 - (1.01 * sine)))

    result.append(equation)

#Plot result
plt.figure()
plt.plot(theta, result, "r")
plt.title("Sinusoidal Block Diagram Result")
plt.xlabel("Theta")
plt.ylabel("Result")
plt.show()

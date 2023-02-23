#Importing Modules
import numpy as np
import matplotlib.pyplot as plt
import math


#Variables
x = np.deg2rad(0.1) #0.1 degrees to radians
z = np.deg2rad(360) #360 degrees to radians
theta = np.arange(0, z, x) #Range to test theta (from 0 to 360 degrees, step of 0.1 degrees - transformed into radians)

peResult = [] #Container to hold the result of pe

paResult = [] #Container to hold the result of pa

#Calculate values for theta
for k in (theta):

    pe = 2.2222222222222222222222222222222222222222222 * math.sin(k) #Calculate pe

    pa = 1 - pe #Calculate pa

    peResult.append(pe) #Add PE's calulation to the result container

    paResult.append(pa) #Add PA's calculation to the result container

#Plot result
plt.figure()

#Plot grid
plt.grid();

#Plot PE
plt.plot(theta, peResult, "r", label='PE')

#Plot PM
plt.axhline(y = 1, color = 'g', label='PM')

#Plot PA
plt.plot(theta, paResult, "b", label='PA')

#Plot title
plt.title("PM,PE,PA")

#Plot X label
plt.xlabel("Radiano")

#Plot Y label
plt.ylabel("MW")

#Plot graph description
plt.legend();


plt.show()

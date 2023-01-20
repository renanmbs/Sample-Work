#Importing Modules
import numpy as np
import matplotlib.pyplot as plt
import math


#Variables
result2 = [] #Container to hold the result
theta2 = np.arange(0, 1, 0.001) #Time sample (0 to 1, 0.001 increment)

r = 1 #Resistor value - 1 ohm
l = 100e-3 #Inductor value - 100 mA
left = 1/r #Left side of equation
rl = (-r)/l #Exponent calculation

#Calculate values for t
for t in (theta2):

    equation = left * (1 - np.exp((rl) * t)) #Calculation

    result2.append(equation) #Add value to container

#Plot figure
plt.figure()
plt.plot(theta2, result2, "r") #plt(x,y)
plt.title("Resultado Circuito RL")
plt.xlabel("Tempo (t)")
plt.ylabel("I (A)")
plt.show()

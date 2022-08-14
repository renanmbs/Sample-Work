#Importing modules
import matplotlib.pyplot as plt
import numpy as np
import math

#Function to make Power into dBm
def power_to_dbm(power):

    #Calculation
    calculation = 10 * (np.log10(power/1e-3))

    return calculation

#Function to make dBm into Power
def dbm_to_power(dbm):

    #Calculation
    ratio = (dbm / 10)
    calculation = 10 ** (ratio)

    return calculation

#Budget Calculation
def budget(bh, bt, esp01, adpt, servo, esp32, power_supply, printing):

    bh_single = math.ceil((bh)/12)
    print("Battery Clip cost: $%d" % (bh_single))
    bt_clip = int(bt/2)
    print("The Cost Of A Single Battery Clip Is: $%d" % (bt_clip))
    esp01_single = math.ceil((esp01/6))
    print("The Cost Of A Single ESP8266-01 Is: $%d" % (esp01_single))
    servo_single = math.ceil((servo/4))
    print("The Cost Of A Single Servo Is: $%d" % (servo_single))
    esp32_single = math.ceil((esp32/3))
    print("The Cost Of A Single ESP32 Is: $%d" % (esp32_single))
    power_supply_single = math.ceil((power_supply/24))
    print("The Cost Of A Single Battery Is: $%d" % (power_supply_single))

    total = int((bh_single + bt_clip + esp01_single + adpt + servo_single + esp32_single + power_supply_single + printing))

    return total

#Budget Calculation
def budget_final(shipping, bt, servo, esp32, power_supply, printing):

    servo_single = math.ceil((servo/4))
    print("Servo cost: $%d" % (servo_single))
    esp32_single = math.ceil((esp32*2))
    print("ESP cost (2x): $%d" % (esp32_single))
    print("3D printing cost (2x): $%d" % (printing))
    bt_clip = int(bt)
    print("Battery clip cost (2x): $%d" % (bt_clip))
    power_supply_single = math.ceil((power_supply*2))
    print("Battery cost (2x): $%d" % (power_supply_single))
    print("Battery shipping cost: $%d" % (shipping))

    total = int((bt_clip + servo_single + esp32_single + power_supply_single + printing + shipping))

    return total

 #Calling Budget function
price = int(budget_final(5,9,11,10,5,5))
print("The Cost Of A Single Product Is: $%d" % price)
print("The (2x) components are already considered in the final price")


#Parameters
distance_in_dbm = np.array([0,-10,-45,-55,-65,-85,-100])
distance_in_meters = np.array([0,1,2,4,6])
powers = np.array([1e-3,0.1e-3,0.01e-3,0.001e-3,0.0001e-3,0.00001e-3,0.000001e-3])

#Separation of Data
distance_in_dbm_open = np.array([0,-10,-45])
distance_in_dbm_nothing = np.array([-45,-55,-65])
distance_in_dbm_close = np.array([-65,-75,-85])
distance_in_meters_open = np.array([0,1,2])
distance_in_meters_nothing = np.array([2,4,6])
distance_in_meters_close = np.array([6,8,25])


#PLOTTING

#DISTANCE SCALES
#meters x dbm
plt.plot(distance_in_meters_open, distance_in_dbm_open, "g", marker = '.')
plt.plot(distance_in_meters_nothing, distance_in_dbm_nothing , "y", marker = '*')
plt.plot(distance_in_meters_close, distance_in_dbm_close, "r", marker = 'o')
plt.title("Range Illustration")
plt.xlabel("Distance - Meters")
plt.ylabel("Signal Strength - dBm")
plt.show()

#dbm x meters
plt.plot(distance_in_dbm_open, distance_in_meters_open, "g", marker = '.')
plt.plot(distance_in_dbm_nothing, distance_in_meters_nothing , "y", marker = '*')
plt.plot(distance_in_dbm_close, distance_in_meters_close, "r", marker = 'o')
plt.title("Range Illustration")
plt.xlabel("Signal Strength - dBm")
plt.ylabel("Distance - Meters")
plt.show()


#Pie chart of costs
prices = np.array([9,3,20,10,5,5])
mylabels = ["Battery Clips","Servo","ESP32","Batteries","Shipping batteries","3D Printing"]
mycolors =  ["#fcc981","#000000","#af8a69","#fcc981","#af8a69","#000000"]
myexplode = [0,0,0.2,0,0,0]
plt.pie(prices, labels = mylabels, explode = myexplode, colors = mycolors)
plt.show()


#POWER TO DBM

#Calling functions
print("Main Desired dBm Points")
print(distance_in_dbm)
wanted_power = dbm_to_power(distance_in_dbm)
print("Main Desired dBm Points In Power (mW): ")
print(wanted_power)
main_dbm_points = power_to_dbm(powers)
print("Important Points In dBm: ")
print(main_dbm_points)
print("Important Points In Power (mW): ")
print(powers)


#Setting grid for subplots
figure_2, axes_2 = plt.subplots(2)

#Printing main title
figure_2.suptitle("Power to dBm Scale")

#First Plot
axes_2[0].set_title('Main points')  #Title
axes_2[0].set(xlabel = 'Power (mW) - Logarithmic Scale', ylabel = 'dBm') #Axis
axes_2[0].semilogx(wanted_power, distance_in_dbm, "r", marker = '.') #What to plot

#Second Plot
axes_2[1].set_title('Important Project Points')  #Title
axes_2[1].set(xlabel = 'Power (mW) - Logarithmic Scale', ylabel = 'dBm') #Axis
axes_2[1].semilogx(powers, main_dbm_points, "g", marker = '.') #What to plot

#Make Plots Tight
figure_2.tight_layout()
#Show Plot
plt.show()

#ESP Now
esp_now_dbm = np.array([-10,-30,-35,-45,-50,-55,-60,-65,-70,-75])
esp_now_in_meters = np.array([0,1,2,3,5,8,10,15,20,24])

#Separation of Data
esp_now_dbm_open = np.array([-10,-30,-35,-45])
esp_now_dbm_nothing = np.array([-45,-50,-55,-60])
esp_now_dbm_close = np.array([-60,-65,-70,-75])
esp_now_in_meters_open = np.array([0,1,2,3])
esp_now_in_meters_nothing = np.array([3,5,8,10])
esp_now_in_meters_close = np.array([10,15,20,24])

esp_now_close_closer = np.array([-45,-50,-55,-60,-65,-70,-75])
esp_now_in_meters_close_closer = np.array([3,5,8,10,15,20,24])

#Container for data
dbms = []

#Loop through the length of the array
for i in range(len(esp_now_dbm)):

    dbms.append(dbm_to_power(esp_now_dbm[i])) #Append Power values in container after calling DBM -> Power function


#Meters x dbm
plt.semilogx(esp_now_in_meters, esp_now_dbm, "g", marker = '.') #Semilog table on X axis
plt.title("Meters and Signal Strength Relation")
plt.xlabel("Distance - Meters")
plt.ylabel("Signal Strength - dBm")
plt.show()

#Meters x Power
plt.semilogy(esp_now_in_meters, dbms, "r") #Semilog table on Y axis
plt.title("Meters and Power Relation")
plt.ylabel("Distance - Meters")
plt.xlabel("Power - Milliwatt")
plt.show()

#Range Illustration
plt.plot(esp_now_in_meters_open, esp_now_dbm_open, "g", marker = '.')
plt.plot(esp_now_in_meters_nothing, esp_now_dbm_nothing , "y", marker = '*')
plt.plot(esp_now_in_meters_close, esp_now_dbm_close, "r", marker = 'o')
plt.title("Range Illustration - Normal Functionality")
plt.xlabel("Distance - Meters")
plt.ylabel("Signal Strength - dBm")
plt.show()

#Range Illustration
plt.plot(esp_now_in_meters_open, esp_now_dbm_open, "g", marker = '.')
plt.plot(esp_now_in_meters_close_closer, esp_now_close_closer, "r", marker = '*')
plt.title("Range Illustration - Closer Mode Functionality")
plt.xlabel("Distance - Meters")
plt.ylabel("Signal Strength - dBm")
plt.show()

#Setting grid for subplots
figure_2, axes_2 = plt.subplots(2)

#Printing main title
figure_2.suptitle("Range Illustration")

#First Plot
axes_2[0].set_title('Normal Functionality')  #Title
axes_2[0].set(xlabel = 'Distance - Meters', ylabel = 'Signal Strength - dBm') #Axis
axes_2[0].plot(esp_now_in_meters_open, esp_now_dbm_open, "g", marker = '.', label = "Open Door") #What to plot
axes_2[0].plot(esp_now_in_meters_nothing, esp_now_dbm_nothing , "y", marker = '*', label = "Do Nothing Region")
axes_2[0].plot(esp_now_in_meters_close, esp_now_dbm_close, "r", marker = 'o', label = "Close Door")

#Second Plot
axes_2[1].set_title('Closer Mode Functionality')  #Title
axes_2[1].set(xlabel = 'Distance - Meters', ylabel = 'Signal Strength - dBm') #Axis
axes_2[1].plot(esp_now_in_meters_open, esp_now_dbm_open, "g", marker = '.', label = "Open Door")
axes_2[1].plot(esp_now_in_meters_close_closer, esp_now_close_closer, "r", marker = 'o', label = "Close Door")

#Make Plots Tight
figure_2.tight_layout()
axes_2[0].legend(["Open Door","Do Nothing Region","Close Door"])
axes_2[1].legend(["Open Door","Close Door"],)
#Show Plot
plt.show()

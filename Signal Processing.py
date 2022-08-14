#Importing Modules
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time


#---------/Functions/------------------------------#

#Function for part 1B
def different_f0(f0):
    #Parameters
    steps = 80
    phi = 0
    fs = 8e3
    A = 1
    x = 10e-3 / steps
    t = np.arange(0, 10e-3, x)
    sampling = int((fs * 10e-3))
    #Container to hold results
    result = []

    #Equation for part 1
    for k in range(sampling):
        kt = (A * np.sin(2 * np.pi * k * (f0 / fs) + phi))
        result.append(kt)

    return result

#Part 1C function
def different_f0_1c(f0, t, phi):

    #Samples per second
    fs = 44100

    #Attenuation
    atten = 0.3

    #A
    A = 1

    #Numpy to calculate waveform
    k_array = np.arange(t * fs)
    waveform = (A * np.sin(2 * pi * k_array * (f0 / fs) + phi))
    waveform_quiet = waveform * atten

    #Play on speakers
    sd.play(waveform_quiet, fs)
    time.sleep(t)
    sd.stop()

    return waveform_quiet

def different_f0_1d(f0, t, phi):

    #Samples per second
    fs = 44100

    #Attenuation
    atten = 0.3

    #A
    A = 1

    #Numpy to calculate waveform
    k_array = np.arange(t * fs)
    waveform = (A * np.sin(2 * pi * k_array * (f0 / fs) + phi))
    waveform_quiet = waveform * atten

    return waveform_quiet

#Part 2 Function
def part_2(fs, f1, u):

    #Parameters
    t = 8
    atten = 0.3

    #Numpy to calculate waveform
    k_array = np.arange(t * fs)
    waveform = np.cos((np.pi * u * ((k_array / fs) ** 2)) + 2 * np.pi * f1)
    waveform_quiet = waveform * atten

    #Play on speakers
    sd.play(waveform_quiet, fs)
    time.sleep(t)
    sd.stop()

    return waveform_quiet

#---------/Parameters/------------------------------#

#Part 1 parameters
steps = 80
phi = 0
f0 = 300
fs = 8e3
A = 1
pi = np.pi
x = 10e-3 / steps
t = np.arange(0, 10e-3, x)
sampling = int((fs * 10e-3))
#Container to hold results
result = []


#---------/Part 1A/------------------------------#

#Equation for part 1
for k in range(sampling):
    kt = (A * np.sin(2 * pi * k * (f0 / fs) + phi))
    result.append(kt)

#Plotting for part 1A
plt.figure()
plt.stem(t, result, "r--")
plt.title("Sinusoid Part 1-A")
plt.xlabel("Time")
plt.ylabel("x(Kt)")
plt.show()


#---------/PART 1B/------------------------------#

#F0 = 300
f300 = different_f0(300)
plt.subplot(3,3,1)
plt.plot(t, f300, "r")
plt.xlabel("Time")
plt.ylabel("x(Kt)")

#F0 = 500
f500 = different_f0(500)
plt.subplot(3,3,3)
plt.plot(t, f500, "b")
plt.xlabel("Time")
plt.ylabel("x(Kt)")

#F0 = 700
f700 = different_f0(700)
plt.subplot(3,3,7)
plt.plot(t, f700, "y")
plt.xlabel("Time")
plt.ylabel("x(Kt)")

#F0 = 900
f900 = different_f0(900)
plt.subplot(3,3,9)
plt.plot(t, f900, "g")
plt.xlabel("Time")
plt.ylabel("x(Kt)")

#Plot title
plt.suptitle("Sinusoid Part 1B")
plt.show()


#---------/PART 1C/------------------------------#

#Samples per second
fs = 44100

#Frequency / pitch
f0 = 440.0

#Duration
t = 5.0

#Attenuation
atten = 0.3

#Phi
phi = 0

#A
A = 1

#Numpy to calculate waveform
k_array = np.arange(t * fs)
waveform = (A * np.sin(2 * pi * k_array * (f0 / fs) + phi))
waveform_quiet = waveform * atten

#Play on speakers
print("Playing sound one")
sd.play(waveform_quiet, fs)
time.sleep(t)
sd.stop()
print("Done playing sound one, Phi: %i" % phi)

#Playing with a different PHI
print("Playing sound two")
different_f0_1c(440, 5, 1000)
print("Done playing sound two, Phi: 1000")


#---------/PART 1D/------------------------------#

#Setting arrays of waveforms
array_1 = np.array(different_f0_1d(300,1,0))
array_2 = np.array(different_f0_1d(500,1,0))
array_3 = np.array(different_f0_1d(700,1,0))
array_4 = np.array(different_f0_1d(900,1,0))

#Putting sounds together
concatenation = np.hstack((array_1,array_2,array_3,array_4))

#Play on speakers
print("Playing sound three")
sd.play(concatenation, fs)
time.sleep(t)
sd.stop()
print("Done playing sound three, Phi: 0")


#---------/PART 1E/------------------------------#

#F0 = 7700
print("Playing sound four")
different_f0_1c(7700, 5, 0)
print("Done playing sound four, F0 = 7700, Phi = 0")

#F0 = 7500
print("Playing sound five")
different_f0_1c(7500, 5, 0)
print("Done playing sound five, F0 = 7500, Phi = 0")

#F0 = 7300
print("Playing sound six")
different_f0_1c(7300, 5, 0)
print("Done playing sound six, F0 = 7300, Phi = 0")

#F0 = 7100
print("Playing sound seven")
different_f0_1c(7100, 5, 0)
print("Done playing sound seven, F0 = 7100, Phi = 0")


#---------/PART 2/------------------------------#

#Parameters
f1 = 100
fs = 32e3
u = 2000
t = np.arange(0, 0.0625, 3.125e-5)

#Function
ct = np.cos((np.pi * u * t * t) + 2 * np.pi * f1)

#---------/PART 2A/------------------------------#
#Plotting for part 2A
plt.figure()
plt.plot(t, ct, "r--")
plt.title("Chirp Signal")
plt.xlabel("Time")
plt.ylabel("C(t)")
plt.show()

#Part 2A sound
print("Playing sound eight")
part_2(32e3, 100, 2000)
print("Done playing sound eight, FS = 32k, f1 = 100, u = 2000")

#---------/PART 2B/------------------------------#
#Part 2B Sound
#Fs = 16k
print("Playing sound nine")
part_2(16e3, 100, 2000)
print("Done playing sound nine, FS = 16k, f1 = 100, u = 2000")

#Fs = 8k
print("Playing sound ten")
part_2(8e3, 100, 2000)
print("Done playing sound ten, FS = 8k, f1 = 100, u = 2000")

#F1 = 500
print("Playing sound eleven")
part_2(32e3, 1000, 2000)
print("Done playing sound eleven, FS = 32k, f1 = 500, u = 2000")

#U = 5000
print("Playing sound twelve")
part_2(32e3, 100, 5000)
print("Done playing sound twelve, FS = 32k, f1 = 100, u = 5000")

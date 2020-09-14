import matplotlib.pyplot as plt
import numpy as  np

f = open('termokopper.txt', 'r')
lines = f.readlines()

time = np.zeros(len(lines))
temp1 = np.zeros(len(lines))
temp2 = np.zeros(len(lines))

for i in range(len(lines)):
    split = lines[i].split()
    time[i] = split[0]
    temp1[i] = split[1]
    temp2[i] = split[2]

plt.plot(time,temp1,time,temp2)
plt.legend(["Temperfect", "Bodum"])
plt.title("Temperature of liquid in cups")
plt.xlabel("Time [s]")
plt.ylabel("Temperature [°C]")
#plt.savefig("cuptemp.png", dpi = 400)
plt.show()


N = 0
q = 0
W = 
kb = 1
S = kb*np.log()

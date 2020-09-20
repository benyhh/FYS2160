import matplotlib.pyplot as plt
import numpy as  np
from scipy.special import comb
from scipy.misc import derivative

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

def multiplicity(q):
    W = comb(N-1+q, q, repetition = True)
    return W
N = 100
q = np.arange(20)
kb = 1
epsilon = 1

W = multiplicity(q)
U = q*epsilon
S = kb*np.log(W)

def diff(A,B): #Derivative by midpoint method
    D = np.zeros(len(A))
    D[0] = (A[1]-A[0])/(B[1]-B[0])

    for i in range(1, len(A)-1):
        D[i] = (A[i+1]-A[i-1])/(B[i+1]-B[i-1])

    D[-1] = (A[-1]-A[-2])/(B[-1]-B[-2])
    return D


T = 1/diff(U,S)
Cv = diff(U,T)

def mult(N,q):
    W = ((N+q)/q)**q*((N+q)/N)**N
    return W

T_a = epsilon / k / np.log(1 + N * epsilon / U)
U_a = N*epsilon/(np.exp(epsilon/k/T)-1)
Cv_a = epsilon**2 * N * np.exp(epsilon/k/T) / ( (np.exp(epsilon/k/T)-1)**2 * k * T**2 )

plt.plot(T,Cv)
plt.show()

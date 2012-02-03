# -*- coding: utf-8 -*-
"""
@author: antoanne
"""
from numpy import *

N=float(100000)
m = float(float(1) / (float(70)*float(365)))
alfa = float(0.8)
beta = float(0.25)

deltaT = float(0.01)
numDias = float(100)

itera = numDias / deltaT

S = zeros(itera)
I = zeros(itera)
R = zeros(itera)
T = zeros(itera)
for x in range(int(itera)):
    T[x] = (x*deltaT)
    
I[0]=5
R[0]=0
S[0]=N-I[0]-R[0];

for k in range(int(itera-1)):
    S[k+1] = S[k] + (-m * S[k] - alfa * S[k] * I[k] / N + m * N) * deltaT
    I[k+1] = I[k] + (-m * I[k] + alfa * S[k] * I[k] / N - beta * I[k]) * deltaT
    R[k+1] = R[k] + (-m * R[k] + beta * I[k]) * deltaT

plot(T,S, label='S')
plot(T,I, label='I')
plot(T,R, label='R')
legend()
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np               # librarie scrisa in C, eficienta, folosita deseori pt umplere de vectori
import matplotlib.pyplot as plt  # pt grafice
import math                      # pt mate (pt baza ln)

R = float(input("R = "))
C = float(input("C = "))
tau = R * C
print("Tau =", tau)
v_in = 0
v_out = 5
T = 1
time = 10

if 3 * tau < T:
    print ("Cazul 3𝜏 < T")
else: 
    print ("Cazul 3𝜏 > T")

# figura 1
x_in = np.arange(0, time * 2, T * 2)
y_in = []

step = 0
for i in range(0, time * 2, T * 2):
    if step % 2 == 0:
        y_in.append(v_out)
    elif step % 2 == 1:
        y_in.append(v_in)
    step += 1

figin = plt.figure()
ax = figin.add_subplot(111)
ax.step(x_in, y_in) 
ax.set_xlabel('Timp') 
ax.set_ylabel('V_in')
ax.set_xlim((0, time)) 
ax.set_title('Semnal de intrare cu R = {} si C = {}'.format(R, C)) 


# figura 2
x_in = np.arange(0, time * 2, 0.1)
y_in = []
front = 1 
t = 0
p = T * 2
t_total = 0 
first_y_desc = v_out 
last_y_asc = v_out * (1 - math.e ** (- p / tau)) 
while t_total < time * 2:
    if front == 1:
        y_in.append(v_out * (1 - math.e ** (- t / tau)))
    elif front == -1:
        y_in.append(v_out * (math.e ** (- t / tau)) - (first_y_desc - last_y_asc))
    t += 0.1
    t_total += 0.1
    if t > p:
        front *= -1
        t = 0 


figout = plt.figure()
bx = figout.add_subplot(111)
bx.plot(x_in, y_in)
bx.set_xlabel('Timp')
bx.set_ylabel('V_out')
bx.set_xlim((0, time))
bx.set_ylim((0, v_out + 1))
bx.set_title('Semnal de iesire cu R = {} si C = {}'.format(R, C))

figin.savefig("semnal_intrare_r={}_c={}.png".format(R, C)) 
figout.savefig("semnal_iesire_r={}_c={}.png".format(R, C))
plt.show() 


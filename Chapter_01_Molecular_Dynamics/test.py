# %%
import numpy as np 
from matplotlib import pyplot as plt

N = 2000
dt = 0.1
k = 0.1
m = 1

x = np.zeros(N)
V = np.ones(N)

for t in range(N-1):
    x[t+1] = x[t] + V[t]*dt                 # Harmonic oscillator position equation, Euler
    V[t+1] = V[t] - k*x[t]/m*dt             # Harmonic oscillator velocity equation, Euler

plt.figure(figsize=(15,5))
plt.plot(x)

x_Euler = x      # saves the trajectory for later
V_Euler = V      # saves the velocity for later

x  = np.zeros(N)
xh = np.zeros(N)
V  = np.ones(N)

for t in range(N-1):
    xh[t] = x[t] + 0.5*V[t]*dt      # Harm. osc. position eq., intermediate step, leapfrog
    V[t+1] = V[t] - k*xh[t]/m*dt    # Harm. osc. velocity eq., leapfrog
    x[t+1] = xh[t] + 0.5*V[t+1]*dt  # Harm. osc. position eq., final step, leapfrog

plt.plot(x)
plt.legend(['Euler','Leap-frog'])
plt.ylabel('$x$')
plt.xlabel('$t$')
plt.title('Harmonic oscillator')
plt.rcParams.update({'font.size': 18})


x_leapfrog = x   # saves the trajectory for later
V_leapfrog = V   # saves the velocity for later

# %%
# here calculate kinetik energy, potential energy, and plot total energy

                                        # Euler
Ekin = np.zeros(N)
Upot = np.zeros(N)
for t in range(N):
    Ekin[t] = 0.5*m*V_Euler[t]*V_Euler[t]  # kinetik energy (from Euler trajectory)
    Upot[t] = 0.5*k*x_Euler[t]*x_Euler[t]  # potential energy (from Euler traj.)
    
Ekin_Euler = Ekin   
Upot_Euler = Upot


                                        # leapfrog
Ekin = np.zeros(N)
Upot = np.zeros(N)
for t in range(N):
    Ekin[t] = 0.5*m*V_leapfrog[t]*V_leapfrog[t]  # kinetik energy (from leapfrog trajectory)
    Upot[t] = 0.5*k*x_leapfrog[t]*x_leapfrog[t]  # potential energy (from leapfrog traj.)
    
Ekin_leapfrog = Ekin   
Upot_leapfrog = Upot


                                        # now plot
plt.figure(figsize=(15,5))
plt.plot(Ekin_Euler+Upot_Euler)
plt.plot(Ekin_leapfrog+Upot_leapfrog)
plt.legend(['Euler','leapfrog'])
plt.ylabel('$E$')
plt.xlabel('$t$')
plt.title('Harmonic oscillator - Total Energy')
plt.rcParams.update({'font.size': 18})




# %%




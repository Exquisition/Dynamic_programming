'''
visualization of the chaotic behavior of double pendulum
adapted from matplotlib example

# Double pendulum formula translated from the C code at
# http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c

Written by: Andy Zhou
Dec 29, 2018
'''



from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

# parameters
G = 9.81  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 2.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 2.0  # mass of pendulum 2 in kg

# initial conditions
# th1 and th2 are the initial angles (degrees)
# w1 and w2 are the initial angular velocities (degrees per second)
th1 = 190.0
w1 = 10
th2 = -180.0
w2 = 2


def derivs(state, t):
    """

    :param state: 4 element vector with [theta1, w1, theta2, w2]
    :param t:
    :return: 4 element vector dydx with [theta1dot, w1dot, theta2dot, w2dot], derivative of state vector
    """

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    del_ = state[2] - state[0]
    den1 = (M1 + M2)*L1 - M2*L1*cos(del_)*cos(del_)
    dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_) +
               M2*G*sin(state[2])*cos(del_) +
               M2*L2*state[3]*state[3]*sin(del_) -
               (M1 + M2)*G*sin(state[0]))/den1

    dydx[2] = state[3]

    den2 = (L2/L1)*den1
    dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_) +
               (M1 + M2)*G*sin(state[0])*cos(del_) -
               (M1 + M2)*L1*state[1]*state[1]*sin(del_) -
               (M1 + M2)*G*sin(state[2]))/den2

    return dydx


dt = 0.01
t = np.arange(0.0, 50, dt)



# initial state
state = np.radians([th1, w1, th2, w2])

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

# y is a matrix of shape (len(t), len(state)=4)
# we only care about columns 0 and 2 to get theta1, theta2 respectively

x1 = L1*sin(y[:, 0])    # x position of pendulum 1
y1 = -L1*cos(y[:, 0])   # y position of pendulum 1

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1


# -----------------------PLOTTING--------------------------------------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-4, 4), ylim=(-4, 4))


line, = ax.plot([], [], 'o-', lw=3, markersize=10)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

trail_x, trail_y = [], []
trail, = ax.plot([], [], lw=0.5, color='m')


def init():
    line.set_data([], [])
    time_text.set_text('')
    trail.set_data([], [])
    return line, time_text, trail


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    trail_x.append(x2[i])
    trail_y.append(y2[i])


    line.set_data(thisx, thisy)
    trail.set_data(trail_x, trail_y)

    time_text.set_text(time_template % (i*dt))
    return line, time_text, trail

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
                              interval=1, blit=True, init_func=init)


plt.show()


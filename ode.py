import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def grad(xy, t, alpha, beta, gamma, delta):
    '''
    Calculates gradient of Lotka-Volterra model
    Inputs:
            xy: state of the system xy[0] = population density of prey 
                                    xy[1] = population density of predator
            t: current time
            alpha: birth rate of the prey
            beta: the effect of the predator of the preys growth rate
            gamma: the effect of the prey on the preodators growth rate
            delta: the predators death rate
    Outputs:
            the gradient of the predator prey model
    '''
    dxdt = (alpha*xy[0])-(beta*xy[0]*xy[1])
    dydt = (delta*xy[0]*xy[1])-(gamma*xy[1])
    grad = [dxdt, dypdt]

    return grad

def solve_equations(xy0, t_max, alpha, beta, gamma, delta):
    '''
    Solves the Lotka-Volterra model
    '''
    t = np.linespace(0, t_max)
    LotkaVolterra = odeint(grad, xy0, t, (alpha, beta, gamma, delta))
    return LotkaVolterra, t


def plot_lv(t, data):
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(t, data[:,0], label = 'X(t)')
    ax2 = fig.add_subplot(212)
    ax2.plot(t, data[:,1], label = 'Y(t)')
    plt.show()
import matplotlib.pyplot as plt
from scipy.intergrate import odeint
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
    dx/dt = (alpha*xy[0])-(beta*xy[0]*xy[1])
    dy/dt = (delta*xy[0]*xy[1])-(gamma*xy[1])
    grad = [dx/dt, dy/dt]

    return grad

def solve_equations(xy0, t_max, alpha, beta, gamma, delta):
    '''
    Solves the Lotka-Volterra model
    '''
    t = np.linespace(0, t_max)
    Lotka-Volterra = odeint(grad, xy0, t, (alpha, beta, gamma, delta))
    return Lotka-Volterra, t
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import argparse

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
    grad = [dxdt, dydt]
    grad = [dxdt, dydt]

    return grad

def solve_equations(xy0, t_max, alpha, beta, gamma, delta):
    '''
    Solves the Lotka-Volterra model
    '''
    t = np.linespace(0, t_max)
    lotkavolterra = odeint(grad, xy0, t, (alpha, beta, gamma, delta))
    return lotkavolterra, t

def plot_lv(t, data):
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(t, data[:,0], label = 'X(t)')
    ax2 = fig.add_subplot(212)
    ax2.plot(t, data[:,1], label = 'Y(t)')
    plt.show()

def main():
    if len(args) < 2:
        print("Error: Please provide input file paths.")
        return
    
    output = ""
    for files in args[1:]:
        sequence = read_file(files)
        output += f"Sequence from file: {files}\n"
    
parser = argparse.ArgumentParser(description='lotka volterra system')
parser.add_argument('--initial', action='store_true')
parser.add_argument('--alpha', action='store_true')
parser.add_argument('--beta', action='store_true')
parser.add_argument('--delta', action='store_true')
parser.add_argument('--gamma', action='store_true')
parser.add_argument('--save_plot')

args = parser.parse_args()
initial = args.initial 
alpha = args.alpha 
beta = args.beta
delta = args.delta
gamma = args.gamma
save_plot = args.save_plot 
=======




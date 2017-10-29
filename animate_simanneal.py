# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 14:00:05 2017

@author: teo
"""

import argparse

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as mpatches

# The polynomial to minimize
poly = [
    np.poly1d([0.25, 7/15, -0.8, -0.8, 2.0]),  # example
    np.poly1d([1, -2, -5]),  # 1 minima
    np.poly1d([13/90, -0.3, -101/45, 13/15, 4]),  # 2 minima
    np.poly1d([0.0000476742, -0.000332066, -0.00217427, 0.0175017,
               0.0234317, -0.300376, 0.111949, 1.95424, -1.63325,
               -2.67103, 2.5])  # 3 minima
]

xranges = [(-3, 2), (-3.5, 3.5), (-5, 5), (-5, 4)]  # Ranges

# Position of the text labels.
text_positions = [(-2, 4), (0, 10), (-3.5, -5), (-3.5, 8)]

if __name__ == "__main__":

    # Parse arguments from command line
    parser = argparse.ArgumentParser(description="Visualizes Simulated Annealing")
    parser.add_argument("-minima", choices=[0, 1, 2, 3], type=int, default=0,
                        help="select polynomial based on minima.\
                        For 0 it select ths example 7.7")
    # Anneal Parameters
    parser.add_argument("-T0", type=float, default=128.0, help="Initial Temperature")
    parser.add_argument("-T1", type=float, default=0.01,  help="Stopping temperature")
    parser.add_argument("-CF", type=float, default=0.5,   help="Cooling factor")
    parser.add_argument("-CS", type=int,   default=100,
                        help="Cooling Schedule, how often to apply the cooling")
    parser.add_argument("-d", type=float,  default=3.0,
                        help="Neighborhood to look for new candidates")
    #  parser.add_argument("-SF", type=float, default=0.6,
    #                      help="Shrink Factor: how much to shrink the neighborhood")
    #  parser.add_argument("-SS", type=float, default=np.Inf,
    #                      help="Number of rejections required to shirnk the neighborhood")

    # Animation Parameters
    parser.add_argument("--delay", type=int, default=100, help="delay between frames in ms")

    args = parser.parse_args()

    # Get the Polynomial
    p = poly[args.minima]
    def V(x): return np.polyval(p, x)

    # Base Plot
    xmin, xmax = xranges[args.minima]
    x_array = np.linspace(xmin, xmax, 500)
    y_array = np.polyval(p, x_array)
    fig, ax = plt.subplots()
    ax.plot(x_array, y_array, 'k-')
    plt.xlabel("x")
    plt.ylabel("V(x)")
    ax.grid(True)

    # legend
    blue_dot = mpatches.Patch(fc='blue', label='current')
    cyan_dot = mpatches.Patch(fc='cyan', label='candidate')
    red_dot = mpatches.Patch(fc='red', label='best')
    ax.legend(handles=[blue_dot, cyan_dot, red_dot], loc=0)

    # Animated Parts
    #  region = ax.axvspan(-3.5, 3.5, color='red', alpha=0.25, animated=True)
    points = ax.scatter([0]*3, [V(0)]*3, s=50, color=['blue', 'cyan', 'red'],
                        animated=True)
    text_x, text_y = text_positions[args.minima]
    text_art = ax.text(text_x, text_y,
                       "Temperature: %.2f\nStep: %d" % (args.T0, 0),
                       fontsize=14, animated=True)

    def anneal():
        global args

        # Temperature parameters
        Temp = args.T0
        Temp_min = args.T1
        cool_factor = args.CF
        cool_schedule = args.CS

        # Neighborhood Parameters
        delta = args.d

        # Initialize values
        steps = 0
        x = np.random.uniform(-3.5, 3.5)  # first choice
        Vx = V(x)
        xbest, Vbest = x, Vx

        # Main loop
        while Temp > Temp_min:
            steps += 1
            if steps == cool_schedule:
                Temp *= cool_factor
                steps = 0

            xnew = x + np.random.uniform(-delta, delta)
            Vnew = V(xnew)

            yield (x, xnew, xbest), (Vx, Vnew, Vbest), Temp, delta, steps

            if xnew < xmin or xnew > xmax:
                # don't go off screen!
                continue

            if np.log(np.random.rand()) < -(Vnew - Vx) / Temp:
                x, Vx = xnew, Vnew
                if Vx < Vbest:
                    xbest, Vbest = x, Vx


    def updatefig(data):
        Xs, Vs, Temp, dx, steps = data
        x, xnew, xbest = Xs
        Vx, Vnew, Vbest = Vs
        points.set_offsets(np.array([[x, Vx], [xnew, Vnew], [xbest, Vbest]]))
        text_art.set_text("Temperature: %.3f\nStep: %d" % (Temp, steps))

        return points, text_art,

    anim = animation.FuncAnimation(fig, updatefig, anneal,
                                   blit=True, interval=args.delay, repeat=False)

    plt.show()


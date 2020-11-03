import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def draw_plot(wavelength, value, result):

    fig, ax = plt.subplots()
    ax.plot(wavelength, value)
    right = 1
    top = 1
    font = {'family': 'serif',
            'color':  'darkred',
            'weight': 'normal',
            'size': 16,
            }
    amplitude = result['amplitude']
    info = f'Amplitude: {amplitude}.'

    ax.text(right, top, info,
            horizontalalignment='right',
            verticalalignment='top',
            transform=ax.transAxes,
            fontdict=font)
    ax.set(xlabel='Wavelength (nm)', ylabel='absorbance ([a.u.])',
           title=filename)
# ax.grid()
    fig.savefig("test.png")
    plt.show()


wavelength = [3.1, 3.2, 3.3, 3.4, 3.5]
value = [386.0, 346.0, 228.0, 482.0, 399.0]
result = {'minimum': 228.0,
          'maximum': 482.0,
          'amplitude': 254.0
          }
filename = 'test.csv'
draw_plot(wavelength, value, result)

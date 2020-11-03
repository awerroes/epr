import os

import csv

import magic

#filename = '/home/jazon/project/epr/data/raw/test_data/testB.csv'

def open_spectre(filename):

    """Check row structure amd return x amd y vals as lists"""

    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter = "\t")
        wavelength = []
        value = []
        for row in reader:
            try:   
                if ((type(float(row[0])) is float) and (type(float(row[1])) is float)):
                    wavelength.append(float(row[0]))
                    value.append(float(row[1]))
            except:
                continue
    # sortowanie?
    return wavelength, value


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def draw_plot(wavelength, value, result, filename):

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
    fig.savefig(filename + '.png')
    plt.show()
    plt.close()


#wavelength = [3.1, 3.2, 3.3, 3.4, 3.5]
#value = [386.0, 346.0, 228.0, 482.0, 399.0]
result = {'minimum': 228.0,
          'maximum': 482.0,
          'amplitude': 254.0
          }
#filename = 'test.csv'
#draw_plot(wavelength, value, result)

path = '/home/jazon/project/epr/data/raw/test_data'

os.chdir(path) 
     
for filename in os.listdir():
    print(filename)
    if magic.from_file(filename, mime=True) == 'text/plain':
        open_spectre(filename)
        draw_plot(open_spectre(filename)[0], open_spectre(filename)[1], result, filename)
    else:
        continue
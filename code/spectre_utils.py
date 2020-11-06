import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def draw_plot(wavelength, value, result, filename):

    """Zwraca wykres"""

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

import csv

def open_spectre(filename):

    """Otwiera plik z danymi potrzebnymi do sporzadzenia wykresu"""

    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter = "\t")
        spectre = []
        wavelength = []
        value = []
        for row in reader:
            try:   
                if ((type(float(row[0])) is float) and (type(float(row[1])) is float)):
                    spectre.append(row)
                    #wavelength.append(float(row[0]))
                    #value.append(float(row[1]))
            except ValueError:
                print(f"Niepoprawny plik: {filename}".filename)
            finally:
                continue
    
    spectre.sort(key = lambda x: x[0])
    wavelength = [float(item[0]) for item in spectre]
    value = [float(item[1]) for item in spectre]
    
    return wavelength, value

import os

def check_location(path):

    """Sprawdza poprawnosc sciezki dostepu"""

    docstring_ornament = '###------------------------------------###'
    try:
        os.chdir(path)
        return True
    except IOError:
        print(docstring_ornament)
        print("Sprawdz polozenie plikow.")
        print(docstring_ornament)
        return False

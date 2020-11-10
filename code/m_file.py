import csv
import os

import magic
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#filename = '/home/jazon/project/epr/data/raw/test_data/testB.csv'


def open_spectre(filename):
    """Otwiera plik z danymi potrzebnymi do sporzadzenia wykresu"""

    with open(filename, newline='') as f:
        reader = csv.reader(f, delimiter="\t")
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

    spectre.sort(key=lambda x: x[0])
    wavelength = [float(item[0]) for item in spectre]
    value = [float(item[1]) for item in spectre]

    return wavelength, value

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
# result = {'minimum': 228.0,
#           'maximum': 482.0,
#           'amplitude': 254.0
#           }
#filename = 'test.csv'
#draw_plot(wavelength, value, result)

def analyse_dpph(value):

    try:
        amplitude = max(value) - min(value)
        return {'minimum': min(value),
                'maximum': max(value),
                'amplitude': amplitude}
    except ValueError:
        raise print("Lista wartosci jest pusta!")


path = '/home/jazon/project/epr/data/raw'

def check_location(path):
    docstring_ornament = '###------------------------------------###'
    try:
        os.chdir(path)
        return True
    except IOError:
        print(docstring_ornament)
        print("Sprawdz polozenie plikow!")
        print(docstring_ornament)
        return False

def istextfile(filename):

    """Sprawdza czy element folderu jest plikiem tekstowym"""
    
    if os.path.isfile(filename):
        if magic.from_file(filename, mime=True) == 'text/plain':
            return True
        else:
            return False
    else:
        return False

if check_location(path):
    f= open("wyniki.txt","w+")
    files_list = os.listdir()
    files_list.sort()
    for filename in files_list:
        #print(filename)
        if istextfile(filename):
            data = open_spectre(filename)
            result = analyse_dpph(data[1])
            draw_plot(data[0], data[1], result, filename)
            line = filename + "\t" + str(result['minimum']) + "\t" + str(result['maximum']) + "\t" + str(result['amplitude']) + "\n"
            f.write(line)
        else:
            continue
    f.close()

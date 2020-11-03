import csv

filename = '/home/jazon/project/epr/data/raw/test_data/testB.csv'

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

import numpy as np

def load_ecg_csv(path):
    return np.loadtxt(path, delimiter=",", skiprows=1)


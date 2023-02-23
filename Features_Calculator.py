import numpy as np
import neurokit2 as nk
from scipy import stats


def ApEn(data):
    return nk.entropy_approximate(data)[0]


def Entropy(data):
    _, counts = np.unique(data, return_counts=True)
    return stats.entropy(counts)


import numpy as np

def rand_index(length, number=10):
    return list(np.random.choice(length, number, replace=False))
    
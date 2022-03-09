import numpy as np


def generate(value):
    return 2**value


arr = np.array([])

for value in range(0, 6):
    arr = np.append(arr, [generate(value)])
print(arr)

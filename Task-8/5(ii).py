import numpy as np

dimension = int(input("Enter the dimension of identitiy matrix: "))
identity_matrix = np.identity(dimension, dtype="int")
print(identity_matrix)

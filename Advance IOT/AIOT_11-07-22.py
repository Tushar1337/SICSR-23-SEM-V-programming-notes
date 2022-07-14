import numpy as np

a = np.array([1, 2, 3, 4])  # 1d array
b = np.array([[1, 2, 3, 4], [1, 2, 4, 5]])  # 2d array
c = np.array([[[1, 2, 3, 4], [1, 2, 'er', 5]], [[1, 2, 3, 4], [1, 2, 4, 5]]])  # 3d array

d = np.zeros(3)  # using np.zeros function which creates arrays filled with elements as zeros
e = np.zeros((3, 3))
f = np.zeros((3, 3, 3))

print(a.ndim)
print(b.ndim)
print(c[0, 1, 2])  # print third element of second column (still not clear)
print(c.ndim)
print(d.ndim)
print(e.ndim)
print(f.ndim)
#Tushar
import numpy as np

arr = np.array([range(4), range(10,14)])

print "array shape = ",arr.shape

print "array size = ", arr.size

print "array max = ", arr.max()

print "array min = ", arr.min()

print "reshaped array below\n", np.reshape(arr, (2,2,2))

print "the same array transposed looks like\n", np.transpose(arr)

print "array as float using .astype\n", np.float64(arr)



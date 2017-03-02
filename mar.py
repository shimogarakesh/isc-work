import numpy.ma as ma

m1 = ma.masked_array(range(1,9))

print m1

m2 = m1.reshape(2,4)

print m2

m3 = ma.masked_greater(m2, 6)

print m3

res = m3 - np.ones((2,4))

print res

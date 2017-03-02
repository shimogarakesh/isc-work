import numpy.ma as ma

# print dir(ma)

mrr = ma.masked_array(range(10), fill_value = -999)

print mrr

mrr[2] = ma.masked

print mrr
print mrr.mask


narr = ma.masked_where(mrr >6, mrr)

print narr


x = ma.filled(narr)

print x

print type(x)

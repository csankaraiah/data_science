import numpy as np;

a = np.array([1,4,5])

b = np.array([[1,4,5],[2,6,8]])

c = np.array([[1,4,5,6],[2,6,8,5],[3,7,9,11]])

d = np.array([[[1,4,5],[2,6,8]],[[3,7,9], [3,7,10]]])

e = np.array([[[1,4,5],[2,6,8]],[[3,7,9], [3,7,10]], [[3,7,9], [3,7,10]]])

print ('a')
print (a.ndim)
print (a.size)

print ('b')
print (b.ndim)
print (b.size)
print (b.shape)

print ('d')
print (d.ndim)
print (d.size)
print (d.shape)

print ('e')
print (e.ndim)
print (e.size)
print (e.shape)
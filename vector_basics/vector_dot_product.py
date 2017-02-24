import numpy as np;

## dot product of two vectors is multiplication of magnitude of each vector with cosine of angle between them. It a number
## in order to calculcate in a simpler way we can say dot product of two vectors is sum of multiplication of
## each cordinates of the vector
## dot product is also know as inner product

#v = np.array([7.887,4.138])
#w = np.array([-8.802,6.776])

v = np.array([1,2,-1])
w = np.array([3,1,0])

dot_vw = np.dot(v,w)
print(dot_vw)


a = np.array([-5.995,-4.904,-1.874])
b = np.array([-4.496,-8.755,7.103])

dot_ab = np.dot(a,b)
print(dot_ab)



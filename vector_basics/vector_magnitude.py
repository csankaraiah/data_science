import numpy as np;

## magnitude of a vector is ||v|| = square root of ((square of x codinate difference) + (square of y cordinate difference))
## its same as the hypotenous of a triangle


a = np.array([-0.221, 7.437])
b = np.array([8.813,-1.331,-6.247])

mag_a = np.linalg.norm(a)
mag_b = np.linalg.norm(b)

print("magnitude of vectors")
print(mag_a)
print(mag_b)

### calculate the direction of a vector

c = np.array([5.581,-2.136])
d = np.array([1.996,3.108,-4.554])

## Direction of a vector is a vector divided by its magnitude.

##A unit vector is a vector with magnitude of 1 and a vectors direction can represented by a unit vector
## When we have a unit vector for a given vector its also called a normalized vector

mag_c = np.linalg.norm(c)
print("Magnitude of a vector")
print(mag_c)
dir_c = (1/mag_c)*c

print("direction of vectors")
print(dir_c)

mag_d = np.linalg.norm(d)
dir_d = (1/mag_d)*d
print(dir_d)











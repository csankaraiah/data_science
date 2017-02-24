import numpy as np;

## radian between two vectors is

v = np.array([3.183,-7.627])
w = np.array([-2.668,5.319])

mag_v = np.linalg.norm(v)
mag_w = np.linalg.norm(w)
dot_vw = np.dot(v,w)

radian = (dot_vw/(mag_v*mag_w))

print(radian)

## Degree between two vectors


a = np.array([7.35,0.221,5.188])
b = np.array([2.751,8.259,3.985])

mag_a = np.linalg.norm(a)
mag_b = np.linalg.norm(b)
dot_ab = np.dot(a,b)

radian1 = (dot_ab/(mag_a*mag_b))

Angle = np.arccos(radian1)

print(radian1)
print (Angle)


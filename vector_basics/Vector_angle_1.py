import numpy as np;
import math;


## radian between two vectors is

v = np.array([1,2,-1])
w = np.array([3,1,0])

mag_v = np.linalg.norm(v)  ## this is the magnitude of a vector v
mag_w = np.linalg.norm(w)
dot_vw = np.dot(v,w) ## dot product of two vectors
v1 = (dot_vw/(mag_v*mag_w))
radian = np.arccos(v1)
print("radian between two vectors: " + str(radian))
angle = math.degrees(radian)
print("angle between two vectors: " + str(angle))
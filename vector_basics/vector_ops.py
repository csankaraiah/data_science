import numpy as np;

def array_add(a, b):
    c = a + b
    return c

def array_sub(d, e):
    f = d - e
    return f


def array_multi(g, h):
    i = g * h
    return np.around(i,3)


a = np.array([8.218, -9.341])
b = np.array([-1.129, 2.111])

d = np.array([7.119, 8.215])
e = np.array([-8.223, 0.878])

g = np.array([7.41])
h = np.array([1.671,-1.012,-0.318])

print ("array addition :" + str(array_add(a, b)))
print ("array substraction :" + str(array_sub(d, e)))
print ("array multiplication :" + str(array_multi(g, h)))

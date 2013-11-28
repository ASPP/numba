from numba2 import jit

@jit
def f(a, b):
    return a < b

print f(10, 20)
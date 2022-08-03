# np-arrays

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    reverse_arr = [i for i in arr[::-1]]
    return numpy.array(reverse_arr, dtype = float)
arr = input().strip().split(' ')
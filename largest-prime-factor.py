import numpy as np

def largest_prime(limit):

    array = np.ones(1000000,dtype=bool)
    array[0:2] = False

    for i in range(2,int(np.sqrt(limit))):

        if array[i] == True:
            array[i*i::i] = False

    arr = np.array(np.nonzero(array)[0].tolist())
    return max(np.where(limit%arr==0,arr,0).tolist())

print(largest_prime(600851475143)) #output 6857
import numpy as np
def sieve_of_eratosthenes(limit):

    array = np.ones(limit,dtype=int) #generate an array of numbers up to a limit 

    array[0:2] = False #set the first two numbers to False

    for i in range(2,int(np.sqrt(limit))): #loop from 2 to square root of limit

        if array[i] == True: #if array[i] == True 
            array[i*i::i] = False #we map the array with step of i and set it to False 

    return np.nonzero(array)[0].tolist() #here we generate a list of indexes of all nonzero



import math

def find_lcm(x,y):

    return abs(x*y) // math.gcd(x,y)

def find_lcm_range(num_range):

    current_lcm = 2

    for i in range(2,num_range+1):
        
        current_lcm=find_lcm(current_lcm,i)

    return current_lcm

print(find_lcm_range(20)) #232792560
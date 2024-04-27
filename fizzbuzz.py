#code by paullilian

"""
    solving the fizzbuzz challenge on devsplug

"""


def fizzbuzz(number):


    if type(number) != int:

        raise ValueError("this function only works with digits")

    for i in range(number):
        
        if (i%5==0 and i%3==0):
            print("fizzbuzz",end="-")
        elif i % 5 == 0 :
            print("buzz",end="-")
        elif i % 3 == 0:
            print("fizz",end="-")
        else:
            print(i,end="-")


fizzbuzz(15) #output fizzbuzz-1-2-fizz-4-buzz-fizz-7-8-fizz-buzz-11-fizz-13-14-
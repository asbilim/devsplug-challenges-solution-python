#code by paul lilian
#lambda function to check if two numbers are divisible
#https://devsplug.com

can_devide = lambda divisor,dividend: divisor%dividend == 0

print(can_devide(10,7)) #False
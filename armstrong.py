def is_armstrong_number(number):

    number_to_list = list(str(number))
    number_len = len(number_to_list)
    result = 0

    for i in number_to_list:
        result += int(i) ** number_len

    return result == number

for i in range(1000):

    if is_armstrong_number(i):

        print(i,end=" ") 

#output for the 1st 1000 numbers: 0 1 2 3 4 5 6 7 8 9 153 370 371 407
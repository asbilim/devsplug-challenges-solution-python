#code by paulilian


"""
    solving the counting bits in binary challenge on devsplug

"""

def binary_2_decimal(number):

    """
        -function to convert a decimal number to its binary representation
    
    """
    
    final = ""

    while number > 0:

        if number % 2 == 0:
            final = "0" + final
        else:
            final = "1" + final
        number = number // 2

    return final

def count_bit(number):

    """
        this functions takes a number as parameter then:
        -convert it to its binary representation
        -count the number of 1s in the binary representation
    """

    binary_number = binary_2_decimal(number)
    print(binary_number)
    count = 0

    for  i in binary_number:

        if i == "1":
            count+=1

    return count


print(count_bit(5),count_bit(11),sep=";") #result 2;3
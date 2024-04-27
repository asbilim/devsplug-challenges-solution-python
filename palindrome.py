#code by paul_lilian


numbers = [
    121, 1331, 45654, 12321, 78987, 
    11211, 14741, 52325, 99999, 24242, 
    13531, 32323, 40804, 56765, 10101, 
    12345, 67890, 23432, 45678, 11234, 
    98765, 32123, 56789, 12389, 67832, 
    14250, 99801, 10112, 21012, 35653
]


def is_palindrome(number):

    if len(str(number)) %2 == 0:
        half = len(str(number)) // 2
        if str(number)[half:] == str(number)[:half] :
            return True;

    return str(number) == str(number)[::-1]
    

# for number in numbers:

#     print(is_palindrome(number))

print(is_palindrome(32123))
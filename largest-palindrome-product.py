def is_palindrome(number):

    original_number = number
    reversed_number = 0

    while number > 0:

        reversed_number = reversed_number * 10 + number % 10
        number = number // 10

    return original_number == reversed_number

def largest_palindrome_product(size=6):

    if size > 6: #we stop at million
        raise ValueError("size too large")
    
    largest_palindrome = 0

    for i in range((10**size)-1,(10**(size-1))-1,-1):
        for j in range(i,(10**(size-1)-1),-1):

            product = i*j
            if product < largest_palindrome:
                break

            if is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome


print(largest_palindrome_product(5)) #output 999000000999



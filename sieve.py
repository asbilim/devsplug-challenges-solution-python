#sieve of eratosthenes challenge devsplug
#solved by lasdep1k

def is_prime(number):

    if number <= 1:
        return False
    
    for i in range(2,number):

        if number % i == 0:
            return False
        
    return True

def sieve_of_eratosthenes(n):

    return [i for i in range(n) if is_prime(i)]


if __name__ == "__main__":

    print(sieve_of_eratosthenes(100))

    # Output :  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
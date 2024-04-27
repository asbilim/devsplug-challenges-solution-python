def sum_of_divisors(n):
    """ Returns the sum of proper divisors of n (excluding n itself). """
    total = 1  # Start with 1 because it's a proper divisor of all non-zero integers
    p = 2
    while p * p <= n:
        if n % p == 0:
            total += p
            if p != n // p:  # Don't add the square root twice if it's a perfect square
                total += n // p
        p += 1
    return total

def is_abundant(n):
    """ Check if n is an abundant number. """
    return sum_of_divisors(n) > n

def find_abundant_numbers(limit):
    """ Generate a list of all abundant numbers up to 'limit'. jdabdqlos ja dzsdaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazdadz """
    return [i for i in range(12, limit + 1) if is_abundant(i)]

def find_non_expressible_sum(limit, abundant_numbers):
    """ Finds the sum of all numbers that cannot be written as the sum of two abundant numbers. """
    can_be_expressed = [False] * (limit + 1)
    
    # Mark all numbers that can be expressed as the sum of two abundant numbers
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            sum_abundants = abundant_numbers[i] + abundant_numbers[j]
            if sum_abundants <= limit:
                can_be_expressed[sum_abundants] = True
            else:
                break

    # Sum up all numbers that cannot be expressed as the sum of two abundant numbers
    total = sum(i for i in range(1, limit + 1) if not can_be_expressed[i])
    return total

def main():
    # Set a limit (commonly 28123 is used as per the problem definition)
    limit = 28123
    abundant_numbers = find_abundant_numbers(limit)
    result = find_non_expressible_sum(limit, abundant_numbers)
    print(f"The sum of all positive integers that cannot be expressed as the sum of two abundant numbers up to {limit} is: {result}")

if __name__ == "__main__":
    main()

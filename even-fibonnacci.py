def even_fibonacci(limit):

    sum = 0
    if limit == 0:
        return 0
    if limit == 1:
        return 1
    
    previous_number , current_number = 0,1
    for _ in range(2,limit+1):
        previous_number , current_number = current_number , (previous_number+current_number)
        if current_number >=limit:
            break
        if current_number % 2 ==0:
            sum+=current_number

    return sum

print(even_fibonacci(400))

def even_fibonacci(limit):

    if limit == 0:
        return 0
    if limit == 1:
        return 1
    
    previous_number , current_number = 0,1
    print("[",end="")

    for _ in range(2,limit+1):
        previous_number , current_number = current_number , (previous_number+current_number)
        if current_number % 2 ==0:
            print(current_number,end=",")

    print("]",end="") #output [2,8,34,144,610,2584,10946,46368,196418,832040,3524578,14930352,63245986,267914296,1134903170,4807526976,]

even_fibonacci(50)

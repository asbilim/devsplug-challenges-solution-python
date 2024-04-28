#code by paul lilian


def substring(string):

    """
        Create a function that takes a string as input and returns a list of all substrings of that string. 
        Each substring is a sequence of characters that are contiguous in the given string. 
        The function should consider substrings of all possible lengths, from one character up to the length of the entire string.
    """

    result = []
    
    for i in range(len(string)):
        for j in range(i, len(string)):
            result.append(string[i:j+1])
    return result
        


    print(my_list)
    # return my_list

print(substring("abc")) #['a', 'ab', 'abc', 'b', 'bc', 'c']
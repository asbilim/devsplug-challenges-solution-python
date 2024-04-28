def is_anagram(string,candidate):

    if len(string) != len(candidate):

        return False
    
    string,candidate = list(string.lower()),list(candidate.lower())
    string.sort()
    candidate.sort()

    if string != candidate:
        
        return False
         
    return True


print(is_anagram("listen","silent")) #output: True
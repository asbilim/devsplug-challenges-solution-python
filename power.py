from random import randint

test_array = [1,2,3,4]

def remove_duplicate(array):

    new_array = []

    for element in array:
        if not element in new_array:
            new_array.append(element)

    return new_array
def generate_subset(array=[]):

    print(array)
    result = []

    for i in range(0,len(array)):
        for j in range (1,len(array)+1):
            result.append(array[i::j])
            result.append(array[i:j])

    return remove_duplicate(result)
def main():

    print(generate_subset(test_array))

if __name__ == '__main__':

    main()
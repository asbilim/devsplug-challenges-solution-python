from random import randint


test_array = [randint(-10,9) for i in range(10)]


def sliding_window(array=[],k=3):
    result = []

    for i in range(0,len(array)-1):
        print(array[i:i+k])
        result.append(max(array[i:i+k]))

    return result

def main():

    print(sliding_window(test_array,3))

if __name__=="__main__":
    main()
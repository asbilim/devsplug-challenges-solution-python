# code by lasdep1k
# devsplug challenge set matrix zeroes based on conditions

import random

mat_rows = 5
mat_cols = 5

def generate_matrix(rows,cols):

    return [[random.randint(0,9) for i in range(rows)] for i in range(cols)]

def extract_zeroes(matrix,rows,cols):

    zero_indexes = []

    for i in range(cols):
        for j in range(rows):
            if(matrix[i][j]==0):
                zero_indexes.append((i,j))
     
    
    return zero_indexes

def display_matrix(matrix,rows,cols):

    for i in range(cols):
        for j in range(rows):
            print(f"{matrix[i][j]}",end=" ")
        print("\n")


def set_matrix_zeroes(matrix,rows,cols):

    display_matrix(matrix,rows,cols)

    print("*"*25)

    zero_indexes = extract_zeroes(matrix,rows,cols)

    for x,y in enumerate(zero_indexes):
        for i in range(cols):
            matrix[i][y[1]]=0
            for j in range(rows):
                matrix[y[0]][j]=0

    display_matrix(matrix,rows,cols)


if __name__=="__main__":

    matrix = generate_matrix(mat_rows,mat_cols)

    set_matrix_zeroes(matrix,mat_rows,mat_cols)



